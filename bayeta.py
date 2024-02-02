from pydantic import Json
from mongo import MongoDBManager as mongo


def frotar(n_frases: int = 1) -> list:
    """
    Obtiene un número especificado de frases de la base de datos MongoDB.
    """
    return mongo().db_get(n_frases)

def frotar_insertar(frase: Json):
    """
    Inserta una frase en la base de datos MongoDB.
    """
    return mongo().db_insert(frase)

try:
    mongo().db_init()
except:
    print('Error al inicializar la base de datos')