from pymongo import MongoClient
import datetime

musicas = [
                  {
                    "_id": 1,
                    "nome": "Radioactive",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  },
                  {
                    "_id": 2,
                    "nome": "Hear Me",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  },
                  {
                    "_id": 3,
                    "nome": "Demons",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  },
                  {
                    "_id": 4,
                    "nome": "Nothing Left To Say",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  },
                  {
                    "_id": 5,
                    "nome": "Amsterdam",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  }
]

cliente = MongoClient('mongodb://localhost:27017/', username='', password='')
print(cliente)
banco = cliente['test-database']
print(banco)
album = banco['album']
print(album)

album.insert_many(musicas)

