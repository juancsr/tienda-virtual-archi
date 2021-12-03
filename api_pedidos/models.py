from db import db

class Pedido(db.Document):
    codigo = db.StringField(required=True, unique=True)
    cliente_id = db.IntField(required=True)
    productos = db.ListField(db.DictField(), required=True)