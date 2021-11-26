from flask import Flask, request, jsonify, Response
from db import initialize_db
from models import Pedido

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'pedidos',
    'host': 'mongodb_backend_develop',
    'port': 27017,
    'username':'pedidos',
    'password':'pedidos',
    'authentication_source': 'admin'
    
}

initialize_db(app)

@app.route('/<int:idCliente>', methods=['GET'])
def getPedidoByIdCliente(idCliente):
    pedido = Pedido.objects.get(cliente_id=idCliente).to_json()
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