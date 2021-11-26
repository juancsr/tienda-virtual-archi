from flask import Flask, request, jsonify, Response
import requests as req
from db import initialize_db
from models import Pedido
import os

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

@app.route('/cliente/<int:idCliente>', methods=['GET'])
def getPedidoByIdCliente(idCliente):
    pedido = Pedido.objects.get(cliente_id=idCliente).to_json()
    # TODO: Do client request
    # https://stackoverflow.com/questions/6386308/http-requests-and-json-parsing-in-python
    # pedido = Pedido.objects.get(cliente_id=idCliente).to_mongo().to_dict()
    # print(pedido)
    # r = req.get('{}/{}'.format(api_clientes_url, idCliente))
    # print(r.json())
    # pedido.cliente_id = r.json()
    return Response(pedido, mimetype="application/json", status=200)

@app.route('/', methods=['POST'])
def newPedido():
    body = request.get_json()
    Pedido(**body).save()
    return "Ok", 200
@app.route('/', methods=['GET'])
def allPedidos():
    pedidos = Pedido.objects().to_json()
    return Response(pedidos, mimetype="application/json", status=200)
    
@app.route('/<string:codigoPedido>', methods=['DELETE'])
def getPedidoByCodigo(codigoPedido):
    Pedido.objects.get(codigo=codigoPedido).delete()
    return "Ok", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)