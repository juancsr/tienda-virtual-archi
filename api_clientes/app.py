from flask import Flask, jsonify, request
from users import clients
import os
import mysql.connector

mydb = mysql.connector.connect(
  host=os.environ['DB_HOST'],
  user=os.environ['DB_USER'],
  password=os.environ['DB_PASSWORD'],
  database=os.environ['DB_NAME']
)

app = Flask(__name__)

def getAllClients():
    mycursor = mydb.cursor()
    mycursor.execute("select u.id, u.name, u.lastname, u.email, c.name as city, p.number, cl.shippingQuantity, a.address from user u inner join city c on u.id_city=c.id inner join phone_numbers p on u.id=p.id inner join client cl on u.id=cl.client_id inner join addresses a on cl.client_id=a.id;")
    myresult = mycursor.fetchall()
    return myresult

Cls=getAllClients()

def format(results, id):
    Client = {
                    "id": "",
                    "name": "",
                    "surname": "",
                    "email": "",
                    "city": "",
                    "shippingQuantity": "",
                    "phone": "",
                    "address":""
                }
    for result in results:
        if result[0] == id:
            if Client['id']==id:
                if Client['phone']['0']==result[5]:
                    Client['address'][str(len(Client['address']))]=result[7]
                else:
                    Client['phone'][str(len(Client['phone']))]=result[5]
            else:
                Client = {
                    "id": result[0],
                    "name": result[1],
                    "surname": result[2],
                    "email": result[3],
                    "city":result[4],
                    "shippingQuantity":result[6],
                    "phone":{"0":result[5]},
                    "address":{"0":result[7]}
                }
    return Client

#READ
@app.route('/')
def getClients():
    cl=[format(Cls,id) for id in set([c[0] for c in Cls])]
    return jsonify({"Clients":cl})

@app.route('/<int:id>')
def getClient(id):
    cl=format(Cls,id)
    if cl["id"]!="":
        return jsonify({"message":"client found", "Client":cl})
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
    app.run(host='0.0.0.0', debug=True, port=4000)
