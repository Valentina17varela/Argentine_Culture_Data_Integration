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
    
    # Columns of interest for standardization
    columnas = ['cod_localidad', 'id_provincia', 'id_departamento',
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
    
    # Dataframe with total number of columns
    tabla_total = pd.concat([df_museos, df_cines, df_bibliotecas])
    tabla_unica = tabla_total.loc[:, columnas]    
    tabla_unica['fecha_de_carga'] = date.today()
    
    
    # Total number of records by category
    total_categoria = tabla_unica.groupby(['categoría']).size().to_frame(name = 'Registros Categoria')

    # Total number of records by source
    total_fuentes = tabla_total.groupby(['categoría','fuente']).size().to_frame(name = 'Registros Fuente')

    # Number of records by province and category
    total_provincias_categorias = tabla_unica[['categoría', 'provincia']].value_counts().to_frame('Registros Provincia&Categoria')


    # Table for the joint data
    datos_conjuntos = total_categoria.merge(total_fuentes, how='outer',
                                left_index=True, right_index=True)
    datos_conjuntos= datos_conjuntos.merge(total_provincias_categorias, how='outer',
                        left_index=True, right_index=True)
    datos_conjuntos['fecha_de_carga'] = date.today()


    # Information table for cinemas
    tabla_cine = df_cines.loc[:, ['provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']].copy()
    tabla_cine['fecha_de_carga'] = date.today()
    
    
    return tabla_unica, datos_conjuntos, tabla_cine

    
    
    
    
     
    
    

