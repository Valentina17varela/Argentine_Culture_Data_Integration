import pandas as pd
import tabulate
import sqlalchemy


def creacion_DB(tabla,nombre,conexion):
    
    tabla.to_sql(nombre, con = conexion, if_exists = 'replace')
    #print(tabla.to_markdown(tablefmt="fancy_grid"))
    