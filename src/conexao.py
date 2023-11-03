from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def conectar():
    try:
        uri = "mongodb+srv://entregaBranquinho:N4UNMCRomo4fJ3@cluster0.dodulda.mongodb.net/?retryWrites=true&w=majority"        
        cliente = MongoClient(uri, server_api=ServerApi('1'))
        db = cliente.mercado_livre
        return db
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        return None
