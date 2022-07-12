import requests
import os
from datetime import date


def obtener_datos(url, categoria):
    
    informacion = requests.get(url) 
    
    today = date.today()  # Date of file download
    current_date = today.strftime("%d-%m-%Y")
    year_month = today.strftime('%Y-%b')
    
    carpeta = categoria + '/' + year_month
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    archivo = open(categoria 
        + '/'
        + year_month
        + '/' 
        + categoria 
        + '-' 
        + current_date 
        + '.csv', 'wb')
    
    archivo.write(informacion.content)
    archivo.close()
    
    
    
     
    
    

