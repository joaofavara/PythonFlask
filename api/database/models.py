from .db import db

class Music(db.Document):
    # id = db.IntField(require=True)
    nome = db.StringField(required=True)
    banda = db.StringField(required=True)
    categorias = db.ListField(db.StringField(), required=True)