# APLICACION DE API-REST DE PROCESOS


## INSTALACION DEL DRIVER ODBC EN UN SISTEMA OPERATIVO LINUX

1. Actualización del instalador de paquetes de Linux

```
sudo apt-get update

```

2. Instalación de los paquetes de Odbc

```
sudo apt-get install unixodbc unixodbc-dev

```

3. Configura el archivo odbcinst.ini

```
[iSeries Access ODBC Driver]
Description = iSeries Access ODBC Driver
Driver      = /usr/lib/x86_64-linux-gnu/libodbc.so

```

4. Configura el archivo odbc.ini

```
[QDNS_db2]
Description   = My AS400 Connection
Driver        = iSeries Access ODBC Driver
System        = PUB400.COM
UID           = anovillo
PWD           = macs6259
Database      = ANOVILLO1

```

## INSTALACION DEL STRING DE CONEXION

1. Parámetros de la configuración del string de conexión

```
con.host = 'Pub400'
con.serverhost = 'db2'
con.iphost = 'PUB400.COM'
con.usuariohost = 'anovillo'
con.passhost = 'macs6259'
con.schemahost = 'anovillo1'
con.databasehost = 'PUB400'
con.accion = 'add'
con.add_host()

```

2. El valor generado por el script actualizaConexion.py

```
Pub400 = {'server': 'db2', 'ip': 'PUB400.COM', 'usuario': 'anovillo', 'password': 'macs6259', 'database': 'PUB400', 'schema': 'anovillo1', 'strcon': 'db2:pyodbc://DSN=QDSN_db2;UID=anovillo;PWD=macs6259;'} 

```

## ACTUALIZACION DE ANACONDA

1. Verificar la versión de **anaconda**

``` 
conda --version

```

2. Actualización de **conda-forge**

``` 
conda update -n base -c conda-forge conda 

```

3. Configurar **conda-forge**

``` 
conda config --add channels conda-forge 

```

4. Actualización de el propio **conda**

``` 
conda update conda  

```

5. Actualización **anaconda**

``` 
conda update anaconda  

```

6. Actualizar todos los paquetes

``` 
conda update nombre_del_paquete  

```

7. Verificar la versión de **anaconda** nuevamente

``` 
conda --version  

```



## INSTALACION DEL AMBIENTE DE ANACONDA PARA LA APLICACION API-REST

1. Creación de la carpeta 

``` 
ApiRest-Procesos 

```

2. Copiar la aplicacion dentro de la carpeta

3. Generacion del archivo environment.yml

``` 
conda env export --no-builds > environment.yml 

```

4. Generación para un entorno windows

``` 
conda env export --from-history --platform win-64 --no-build -c conda-forge > environment.yml  

```

5. Una vez generado el archivo environment.yml modificar el name con 

``` 
ApiRestProcesos 

```

6. Primero debemos crear el ambiente donde se ejecutara 


```

conda env create -f environment.yml

```

7. Generacion del .exe con el comando pyinstaler del script main.py


## INVOCACION DEL PROCESO DE RECEPCION DE DATOS DE SUCERP

1. El link de invocación del preceso de recepción de datos Sucerp

``` http://mlmsrv:8000/recepciondatossucerp/{uid}/{token}```

2. Una vez realizada la invocacion el usuario recibira una email con la confirmación del lanzamiento del proceso

3. Una vez finalizado el proceso se el usuario recibira un email con el detalle de los archivos procesados




