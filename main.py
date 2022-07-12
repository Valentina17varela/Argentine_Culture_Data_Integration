'''
CHALLENGE DATA ANALYTICS CON PYTHON
Author: Valentina Varela Alzate
'''

import userInterface
import dataCollector


def run():
    
    userInterface.menu_principal()
    
    museos = '''
            https://datos.gob.ar/dataset/cultura-mapa-cultural
            -espacios-culturales/archivo/cultura_4207def0-2ff7
            -41d5-9095-d42ae8207a5d
            '''
    
    cines = ''' 
            https://datos.gob.ar/dataset/cultura-mapa-cultural
            -espacios-culturales/archivo/cultura_392ce1a8-ef11
            -4776-b280-6f1c7fae16ae
            '''
    
    bibliotecas = '''
                https://datos.gob.ar/dataset/cultura-mapa
                -cultural-espacios-culturales/archivo/cultura
                _01c6c048-dbeb-44e0-8efa-6944f73715d7
    
                '''
 
    # Reading and storing data
    dataCollector.obtener_datos(museos,"museos")
    dataCollector.obtener_datos(cines,"cines")
    dataCollector.obtener_datos(bibliotecas,"bibliotecas")
    


if __name__ == '__main__':
    run()