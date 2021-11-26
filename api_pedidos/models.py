from db import db

class Pedido(db.Document):
    # uid = db.UUIDField(required=True, unique=True, binary=False)
    codigo = db.StringField(required=True, unique=True)
    cliente_id = db.IntField(required=True, unique=True)
    productos = db.ListField(db.DictField(), required=True)
    # productos = db.ListField(db.StringField(), required=True)