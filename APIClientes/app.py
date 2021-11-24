from flask import Flask, jsonify, request
from users import clients

app = Flask(__name__)

#READ
@app.route('/')
def getClients():
    return jsonify({"Clients":clients})

@app.route('/<int:id>')
def getClient(id):
    clientFound = [client for client in clients if client['id']==id]
    if len(clientFound) > 0:
        return jsonify({"message":"client found", "Client":clientFound[0]})
    return jsonify({"message":"client not found"})


#CREATE
@app.route("/clients", methods=['POST'])
def addClient():
    newClient = {
        "id": request.json['id'],
        "name": request.json['name'],
        "surname": request.json['surname'],
        "email": request.json['email'],
        "city":request.json['city'],
        "shippingQuantity":request.json['shippingQuantity'],
        "phone": request.json['phone'],
        "address":request.json['address']
    }
    clients.append(newClient)
    return jsonify({"mensaje":"client added succesfully", "Client": clients})

#UPDATE
@app.route('/clients/<int:id>', methods=['PUT'])
def editClient(id):
    clientFound = [client for client in clients if client['id']==id]
    if len(clientFound) > 0:
        clientFound[0]['id']= request.json['id']
        clientFound[0]['name']= request.json['name']
        clientFound[0]['surname']= request.json['surname']
        clientFound[0]['email']= request.json['email']
        clientFound[0]['city']=request.json['city']
        clientFound[0]['shippingQuantity']=request.json['shippingQuantity']
        clientFound[0]['phone']=request.json['phone']
        clientFound[0]['address']=request.json['address']
        return jsonify({"message":"client updated succesfully", "Client":clientFound[0]})
    return jsonify({"message":"client not found"})

#DELETE
@app.route('/clients/<int:id>', methods=['DELETE'])
def deleteClient(id):
    clientFound = [client for client in clients if client['id']==id]
    if len(clientFound) > 0:
        clients.remove(clientFound[0])
        return jsonify({"message":"client deleted succesfully", "Client":clients})
    return jsonify({"message":"client not found"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)