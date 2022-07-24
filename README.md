# DATA ANALYTICS + PYTHON
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=yellow&color=4b8bbe)
![](https://img.shields.io/badge/Code-PostgreSQL-informational?style=flat&logo=postgresql&logoColor=white&color=f29111)
![](https://img.shields.io/badge/Lib-Request-informational?style=flat&logo=python&logoColor=yellow&color=4b8bbe)
![](https://img.shields.io/badge/Lib-PythonDecouple-informational?style=flat&logo=python&logoColor=yellow&color=4b8bbe)
![](https://img.shields.io/badge/Lib-Loggin-informational?style=flat&logo=python&logoColor=yellow&color=4b8bbe)
![](https://img.shields.io/badge/Lib-SQLalchemy-informational?style=flat&logo=python&logoColor=yellow&color=4b8bbe)
![](https://img.shields.io/badge/Lib-Pandas-informational?style=flat&logo=python&logoColor=yellow&color=4b8bbe)



Proyecto que consume datos de 3 fuentes distintas para popular una base de datos con informacion cultural sobre bibliotecas, museos y salas de cines argentinos.
<br><br>
Para mas informacion ver documento [Challenge Alkemy](https://github.com/Valentina17varela/Alkemy/blob/main/Challenge%20Data%20Analytics%20con%20Python.pdf)


## Deploy
- Clonar el siguiente repositorio
```
git clone https://github.com/Valentina17varela/Alkemy.git
```

- Crear el entorno virtual y activarlo
  - Windows:
  ```
  py -m venv env
  .\env\Scripts\activate
  ```
  - Unix/macOS:
  ```
  python3 -m venv env
  source env/bin/activate
  ```

- Instalar las dependencias necesarias
```
pip install -r requirements.txt
```

- Configurar los parametros para conectarse a la base de datos, en el archivo ```.env``` reemplazar el valor de las variables globales con la informacion correspondiente
``` 
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_PASSWORD=
POSTGRES_USER=
POSTGRES_DB=
```

> Si las url's de las fuentes han cambiado reemplazar su valor en las variables que se encuentran en ```.env```

<br>

## Ejecucion
Para dar inicio al programa ejecutar el archivo ```main.py```

<br>

## Implementacion
- main.py: Es el archivo principal donde ocurre la descarga y procesamiento de datos.
- userInterface.py: Le informa al usuario el momento en el que se encuentra el programa.
- dataCollector.py: Descarga la informacion correspondiente de las fuentes y procesa la informacion en tablas.
- baseDatos.py: Carga las tablas de informacion a la base de datos.
