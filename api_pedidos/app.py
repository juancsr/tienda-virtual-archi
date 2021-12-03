from flask import Flask, request, jsonify, Response
import requests as req
from db import initialize_db
from models import Pedido
import os
import sys
import json

app = Flask(__name__)

api_clientes_url = os.environ['API_CLIENTES_URL']
api_productos_url = os.environ['API_PRODUCTOS_URL']

app.config['MONGODB_SETTINGS'] = {
    'db': os.environ['DB_NAME'],
    'host': os.environ['DB_HOST'],
    'port': int(os.environ['DB_PORT']),
    'username': os.environ['DB_USERNAME'],
    'password': os.environ['DB_PASSWORD'],
    'authentication_source': os.environ['DB_AUTH']
}

initialize_db(app)

def info_cliente(id_cliente: int) -> object:
    r = req.get('{}/{}'.format(api_clientes_url, id_cliente))
    cliente = r.json()['Client']
    return cliente

def info_producto(id_producto: int) -> object:
    r = req.get('{}/api/products/{}'.format(api_productos_url, id_producto))
    producto = r.json()
    return producto

def update_producto(producto: object) -> bool:
    url = ('{}/api/products/{}'.format(api_productos_url, producto['Id']))
    r = req.put(url=url,data=json.dumps(producto), headers={'content-type': 'application/json'})
    if r.status_code != 200:
        print(r.status_code, r.json())
        return False
    return True

def checkIfProductExists(id: int) -> bool:
    r = req.get('{}/api/products'.format(api_productos_url))
    for producto in r.json():
        if producto['Id'] == id:
            return True
    return False

@app.route('/cliente/<int:idCliente>', methods=['GET'])
def getPedidoByIdCliente(idCliente):    
    pedido = Pedido.objects.get(cliente_id=idCliente).to_mongo().to_dict()
    pedido['cliente_id'] = info_cliente(idCliente)
    pedido.pop('_id', None)
    productos = []
    for producto in pedido['productos']:
        producto_info =info_producto(producto['id'])
        print(producto, producto_info)
        producto_info['quantity'] = producto['cantidad']
        producto = producto_info
        productos.append(producto)
    pedido['productos'] = productos
    return jsonify(pedido), 200

@app.route('/', methods=['POST'])
def newPedido():
    body = request.get_json()
    try:
        info_cliente(body['cliente_id'])  
    except:
        return "El cliente no existe", 404
    
    i_productos = []
    for producto in body['productos']:        
        print(producto['id'])
        if not checkIfProductExists(producto['id']):
            return "El producto no existe", 404

        i_producto = info_producto(producto['id'])
        
        if i_producto['quantity'] < producto['cantidad']:
            return "No hay suficientes existencias de {} para crear el pedido".format(i_producto['name']), 404
        i_producto['quantity'] = i_producto['quantity'] - producto['cantidad']
        i_productos.append(i_producto)
    Pedido(**body).save()

    for i_producto in i_productos:
        update_producto(i_producto)
    return "Ok", 200

@app.route('/', methods=['GET'])
def allPedidos():
    pedidos = Pedido.objects().values_list()
    response = []
    for pedido in pedidos:
        cliente = info_cliente(pedido.cliente_id)
        pedido.cliente_id = cliente
        response.append(pedido)
        productos = []
        for producto in pedido['productos']:
            producto_info =info_producto(producto['id'])
            producto_info['quantity'] = producto['cantidad']
            producto = producto_info
            productos.append(producto)
        pedido['productos'] = productos
    return jsonify(response), 200
    
@app.route('/<string:codigoPedido>', methods=['DELETE'])
def getPedidoByCodigo(codigoPedido):
    Pedido.objects.get(codigo=codigoPedido).delete()
    return "Ok", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=int(os.environ['PORT']))