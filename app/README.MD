# APLICACION DE API-REST DE PROCESOS

## ACTUALIZACION DE ANACONDA

- Verificar la versión de **anaconda**

``` conda --version  ```

- Actualización de **conda-forge**

``` conda update -n base -c conda-forge conda ```

- Configurar **conda-forge**

``` conda config --add channels conda-forge ```

- Actualización de el propio **conda**

``` conda update conda  ```

- Actualización **anaconda**

``` conda update anaconda  ```

- Actualizar todos los paquetes

``` conda update nombre_del_paquete  ```

- Verificar la versión de **anaconda** nuevamente

``` conda --version  ```



## INSTALACION DEL AMBIENTE DE ANACONDA PARA LA APLICACION API-REST

- Creación de la carpeta 

``` ApiRest-Procesos ```

- Copiar la aplicacion dentro de la carpeta

- Generacion del archivo environment.yml

``` conda env export --no-builds > environment.yml ```

- Generación para un entorno windows

``` conda env export --from-history --platform win-64 --no-build -c conda-forge > environment.yml  ```

- Una vez generado el archivo environment.yml modificar el name con 

``` ApiRestProcesos ```

- Primero debemos crear el ambiente donde se ejecutara 


```conda env create -f environment.yml```

- Generacion del .exe con el comando pyinstaler del script main.py


## INVOCACION DEL PROCESO DE RECEPCION DE DATOS DE SUCERP

- El link de invocación del preceso de recepción de datos Sucerp

``` http://mlmsrv:8000/recepciondatossucerp/{uid}/{token}```

- Una vez realizada la invocacion el usuario recibira una email con la confirmación del lanzamiento del proceso

- Una vez finalizado el proceso se el usuario recibira un email con el detalle de los archivos procesados




