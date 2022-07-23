"""
CHALLENGE DATA ANALYTICS CON PYTHON
Author: Valentina Varela Alzate
"""

import userInterface
import dataCollector
import baseDatos
import logging
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database
from sqlalchemy_utils import database_exists
from decouple import config


MUSEOS = config('URL_MUSEOS')
CINES = config('URL_CINES')
BIBLIOTECAS = config('URL_BIBLIOTECAS')

HOST = config('POSTGRES_HOST')
PORT = config('POSTGRES_PORT')
PASS = config('POSTGRES_PASSWORD')
USER = config('POSTGRES_USER')
NAME = config('POSTGRES_DB')


def run():
    
    logging.info("Inicio del programa, accediendo a las fuentes de informacion")
    
    userInterface.menu_principal()
    
    # Reading and storing data
    museos_csv = dataCollector.obtener_datos(MUSEOS,'museos')
    cines_csv = dataCollector.obtener_datos(CINES,'cines')
    bibliotecas_csv = dataCollector.obtener_datos(BIBLIOTECAS,'bibliotecas')
    logging.info("Se almacena de forma local la informacion obtenida")
    
    # Data processing and table normalization
    unica, conjuntos, info_cines = dataCollector.procesar_datos(museos_csv,cines_csv,bibliotecas_csv)

    userInterface.presentacion_tablas();
    logging.info("Procesamiento de datos y normalizacion de tablas")

    # Creation of tables in the database and visualization
    db = 'postgresql://'+USER+':'+PASS+'@'+HOST+':'+PORT+'/'+NAME
    if not database_exists(db):
        create_database(db)
    SQLengine = create_engine(db)
    logging.info("Conexion exitosa a la base de datos")
    
    baseDatos.creacion_DB(unica,"Tabla normalizada",SQLengine)
    baseDatos.creacion_DB(conjuntos,"Datos conjuntos",SQLengine)
    baseDatos.creacion_DB(info_cines,"Informacion de cines",SQLengine)
    logging.info("Tablas cargadas a la base de datos")
    
    logging.info("Ejecucion finalizada")
    
    
if __name__ == '__main__':
    run()