import requests
import os
from datetime import date
import pandas as pd


def obtener_datos(url, categoria):
    
    informacion = requests.get(url) 
    
    # Date of file download
    today = date.today()  
    current_date = today.strftime("%d-%m-%Y")
    year_month = today.strftime('%Y-%b')
    
    # Folder creation
    carpeta = categoria + '/' + year_month
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    # File script
    subcarpeta = categoria + '/' + year_month + '/' + categoria + '-' + current_date + '.csv'
    archivo = open(subcarpeta, 'wb')
    
    archivo.write(informacion.content)
    archivo.close()
    
    return subcarpeta
    
    
def procesar_datos(museos,cines,bibliotecas):
    
    df_museos = pd.read_csv(museos,encoding='UTF-8')
    df_cines = pd.read_csv(cines,encoding='UTF-8')
    df_bibliotecas = pd.read_csv(bibliotecas,encoding='UTF-8')
    
    #creo una variable con las columnas de interés
    cols_interes = ['cod_localidad', 'id_provincia', 'id_departamento',
                    'categoría', 'provincia', 'localidad', 'nombre',
                    'domicilio', 'código postal', 'número de teléfono',
                    'mail', 'web']


    # Normalization of the information by changing the names of the columns 
    # to create the single table
    
    df_museos.rename(columns = {'Cod_Loc' : 'cod_localidad',
                                'IdProvincia' : 'id_provincia',
                                'IdDepartamento' : 'id_departamento',
                                'categoria' : 'categoría',
                                'direccion' : 'domicilio',
                                'CP' : 'código postal',
                                'telefono' : 'número de teléfono',
                                'Mail' : 'mail',
                                'Web' : 'web'},
                    inplace = True)

    df_cines.rename(columns = {'Cod_Loc' : 'cod_localidad',
                                    'IdProvincia' : 'id_provincia',
                                    'IdDepartamento' : 'id_departamento',
                                    'Categoría' : 'categoría', 
                                    'Provincia' : 'provincia',
                                    'Localidad' : 'localidad',
                                    'Nombre' : 'nombre',
                                    'Domicilio' : 'domicilio',
                                    'CP' : 'código postal',
                                    'Fuente':'fuente',
                                    'Teléfono' : 'número de teléfono',
                                    'Mail' : 'mail',
                                    'Web' : 'web'},
                        inplace = True)

    df_bibliotecas.rename(columns = {'Cod_Loc' : 'cod_localidad',
                                    'IdProvincia' : 'id_provincia',
                                    'IdDepartamento' : 'id_departamento',
                                    'Categoría' : 'categoría', 
                                    'Provincia' : 'provincia',
                                    'Localidad' : 'localidad',
                                    'Nombre' : 'nombre',
                                    'Domicilio' : 'domicilio',
                                    'CP' : 'código postal', 
                                    'Fuente':'fuente',
                                    'Teléfono' : 'número de teléfono',
                                    'Mail' : 'mail',
                                    'Web' : 'web'},
                        inplace = True)
    
    # data frame con el total de columnas
    tabla_unica = pd.concat([df_museos, df_cines, df_bibliotecas])

    #data frame solo con las columnas de interes a normalizar
    tabla_unica = tabla_unica.loc[:, cols_interes]    #contiene solo las columnas de interes a normalizar
    tabla_unica['fecha_de_carga'] = date.today()
    
    print(date.today())
    print(tabla_unica)
    
    
    
    
     
    
    

