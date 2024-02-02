from pydantic import Json
from pymongo import MongoClient

class MongoDBManager:
    def __init__(self, database_url='mongodb://mongo-db:27017/', database_name='bayeta'):
        self.client = MongoClient(database_url)
        self.db = self.client[database_name]
        self.collection = self.db['frases']

    def db_connect(self):
        """
        Conecta a la base de datos MongoDB.
        """
        return self.client, self.collection

    def db_init(self):
        """
        Inicializa la base de datos MongoDB.
        """
        datos = open('frases.txt', 'r', encoding='utf-8').readlines()
        _, coleccion = self.db_connect()
        if coleccion.count_documents({}) == 0:
            coleccion.insert_many([{'frase': frase.strip()} for frase in datos])
        self.client.close()

    def db_get(self, n_frases: int = 1):
        """
        Obtiene un número especificado de frases de la base de datos MongoDB.
        """
        _, coleccion = self.db_connect()

        try:
            frases = list(coleccion.aggregate([{'$sample': {'size': n_frases}}]))
            frases_limpias = [frase['frase'].replace('\n', '') for frase in frases]

            return frases_limpias
        
        finally:
            self.client.close()

    def db_insert(self, frase: Json):
        """
        Inserta una frase en la base de datos MongoDB.
        """
        _, coleccion = self.db_connect()
        coleccion.insert_one({'frase': frase.frase})
        self.client.close()
        