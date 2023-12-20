# Load las bibliotecas necesarias
try:
    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion
    import os
    import datetime
    from pydal import Field

except Exception as e:
    print(f'Falta algun modulo {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# verificacion, creacion , limpieza de los registros de las tablas de la lista de tablas
def controlTablas(tablas, iprod):
    """
    Objetivo:  Es verificar si las DDS existe
               Es crear la tabla si las DDS existen
               Es limpiar la tabla si la tabla existe
    tablas = Es una lista de las tablas controlar
    iprod  = es el objeto de conexion a la iseries para ejecutar los comandos
    msg    = Es la respuesta de la ejecucion del comando donde
             msg[0] Los valores posibles es True o False
             msg[1] en adelante tenemos los mensajes que respondio el os400 ...
    return = msg
    """

    tablas = tablas

    # navegamos por el diccionario
    for elemento in tablas:

        lib = elemento["lib"]
        file = elemento["file"]
        src = elemento["src"]


        # verificamos si el fuente existe
        str = f'CHKOBJ OBJ({lib}/QDDSSRC) OBJTYPE(*FILE) MBR({file})'

        # ejecutamos el comando
        msg = iprod.GetCmdMsg(str)

        #  si no existe el fuente
        if not msg[0]:

            return msg

        # si existe el fuente
        else:

            # verificamos si el objeto existe
            msg = iprod.CheckObjExists(lib, file, type="*FILE")

            # si no existe el objeto
            if not msg[0]:

                # creamos la tabla
                str = f'CRTPF FILE({elemento["lib"]}/{elemento["file"]}) SRCFILE({elemento["lib"]}/{elemento["src"]})'

                # creamos la tabla
                msg = iprod.GetCmdMsg(str)

                # si no hay error
                if msg[0]:
                    print(f'Tabla {file} creada...')

                 # si hay error
                else:
                    print(f'Tabla {file} ERROR...')
                    for error in msg:
                        print(error)

            # si exsite el objeto
            else:

                # eliminamos los registros de la tabla
                str = f'CLRPFM FILE({elemento["lib"]}/{elemento["file"]})'

                # eliminamos registros de la tabla
                msg = iprod.GetCmdMsg(str)

                # si no hay error
                if msg[0]:
                    print(f'Tabla {file} eliminamos los registros...')

                 # si hay error
                else:
                    print(f'Tabla {file} ERROR...')
                    for error in msg:
                        print(error)
    return msg

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Read la tabla de Tipo de Registro
def readTipoRegistro(**data):
    """
     data  = diccionario {'campo'': 'valor'}
                  campo = campo de la tabla a buscar
                  valor   = el valor del campo a buscar

     """
    # busco el registro
    data_list, errores = data_Input.get_RowsWhere(objetoTipoRegistro, **data)

    # generamos una lista con los campos del registro
    data_list = [v for k, v in data_list.items()]

    # retornamos el valor del campo
    return data_list[0]['tiporegistroid']

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Read la tabla de Tipo de Sub Registro
def readTipoSubRegistro(**data):
    """
     data  = diccionario {'campo'': 'valor'}
                  campo = campo de la tabla a buscar
                  valor   = el valor del campo a buscar

     """
    # busco el registro
    data_list, errores = data_Input.get_RowsWhere(objetoTipoSubRegistro, **data)

    # generamos una lista con los campos del registro
    data_list = [v for k, v in data_list.items()]

    # retornamos el valor del campo
    return data_list[0]['tiposubregistroid']

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Read la tabla de Tipo de Origen
def readTipoOrigen(**data):
    data_list, errores = data_Input.get_RowsWhere(objetoTipoOrigen, **data)
    data_list = [v for k, v in data_list.items()]
    return data_list[0]['origenid']

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Read la tabla de Provincias
def readProvincia(**data):

    if data['provincia'].isdigit():
        data['provincia'] = int(data['provincia'])
        data_list, errores = data_Input.get_RowsWhere(objetoProvincia, **data)
        data_list = [v for k, v in data_list.items()]
        return data_list[0]['provinciaid']
    else:
        return None

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Read la tabla de Tipo de Cuerpo
def readTipoCuerpo(**data):
    data_list, errores = data_Input.get_RowsWhere(objetoTipoCuerpo, **data)
    data_list = [v for k, v in data_list.items()]
    return data_list[0]['tipocuerpoid']

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Read la tabla de Tipo de Documento
def readTipoDocumento(**data):
    data_list, errores = data_Input.get_RowsWhere(objetoTipoDocumento, **data)
    data_list = [v for k, v in data_list.items()]
    return data_list[0]['tipodocumentoid']


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Tratamiento para la tabla ENCABEZADO
def tipoRegistroE0():
    try:

        # cargamos el diccionario del registro de la tabla ENCABEZADO
        insertE0 = dict()
        insertE0['tiporegistroid'] = readTipoRegistro(**{'tiporegistro': registro[0:2]})
        insertE0['versionprotocolo'] = registro[2:7]
        insertE0['revisionprotocolo'] = registro[7:12]
        insertE0['codigoorganismo'] = registro[12:20]
        insertE0['numeroenvio'] = registro[20:30]
        insertE0['fechahora'] = datetime.datetime.strptime(registro[31:45].strip(), '%Y%m%d%H%M%S')
        insertE0['ktimestamp'] = datetime.datetime.now()

        # write la tabla ENCABEZADO
        data_Input.campos.clear()
        respuesta = data_Input.add_Dal(objetoEncabezado, **insertE0)

        return respuesta

    except Exception as e:
        print(f'Error en tipoRegistroE0 {e} total {total}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Tratamiento para la tabla INFORMACION DEL VEHICULO
def tipoRegistroC5(totalC):

    try:

        # cargamos el diccionario del registro de la tabla INFORMACION DEL VEHICULO
        insertC5 = dict()

        # ------infvehiculoid--------------------------------------------------
        insertC5['INFVE00001'] = totalC

        # ------TIPO REGISTRO--------------------------------------------------
        insertC5['TIPOR00001'] = readTipoRegistro(**{'TIPOR00001': registro[0:2]})

        # ------TIPO SUB REGISTRO--------------------------------------------------
        insertC5['TIPOS00001'] = readTipoSubRegistro(**{'TIPOS00001': registro[2:3]})

        # ------CODIGO ORGANISMO--------------------------------------------------
        insertC5['CODIG0ORGA'] = None
        if registro[3:11].lstrip().isdigit(): insertC5['CODIG0ORGA'] = int(registro[3:11])

        # -----DOMINIO NUEVO---------------------------------------------------
        insertC5['DOMIN00001'] = None
        if not registro[11:19].isspace(): insertC5['DOMIN00001'] = registro[11:19].lstrip()

        # -----DOMINIO VIEJO---------------------------------------------------
        insertC5['DOMIN00002'] = None
        if not registro[19:27].isspace(): insertC5['DOMIN00002'] = registro[19:27].lstrip()

        # ----CODIGO MTMFMM----------------------------------------------------
        insertC5['CODMTMFNM1'] = None
        if not registro[27:35].isspace():
            insertC5['CODMTMFNM1'] = registro[27:35].lstrip()

        # ----TIPO ORIGEN----------------------------------------------------
        insertC5['ORIGENID01'] = readTipoOrigen(**{'ORIGENID01': registro[35:36]})

        # ----CATEGORIA----------------------------------------------------
        insertC5['CATEG00001'] = None
        if not registro[36:39].isspace(): insertC5['CATEG00001'] = registro[36:39].lstrip()

        # ----MARCA----------------------------------------------------
        insertC5['MARCA00001'] = None
        if not registro[39:99].isspace(): insertC5['MARCA00001'] = registro[39:99].lstrip()

        # ----TIPO VEHICULO----------------------------------------------------
        insertC5['TIPOV00001'] = None
        if not registro[99:159].isspace(): insertC5['TIPOV00001'] = registro[99:159].lstrip()

        # ----MODELO----------------------------------------------------
        insertC5['modelo'] = None
        if not registro[159:259].isspace(): insertC5['modelo'] = registro[159:259].lstrip()

        # ---AÑO MODELO-----------------------------------------------------
        insertC5['yyyymodelo'] = None
        if registro[259:263].lstrip().isdigit(): insertC5['yyyymodelo'] = int(registro[259:263])

        # ---PESO--------------------------------------------------------
        insertC5['peso'] = None
        if registro[263:268].lstrip().isdigit(): insertC5['peso'] = int(registro[263:268])

        # ---CARGA--------------------------------------------------------
        insertC5['carga'] = None
        if registro[268:274].lstrip().isdigit(): insertC5['carga'] = int(registro[268:274])

        # ---CILINDRADA--------------------------------------------------------
        insertC5['cilindrada'] = None
        if registro[274:279].lstrip().isdigit(): insertC5['cilindrada'] = int(registro[274:279])

        # ---VALUACION--------------------------------------------------------
        insertC5['valuacion'] = None
        if registro[279:287].lstrip().isdigit(): insertC5['valuacion'] = int(registro[279:287])

        # ---CODIGO TIPO USO--------------------------------------------------------
        insertC5['codigotipouso'] = None
        if not registro[287:289].isspace(): insertC5['codigotipouso'] = registro[287:289].lstrip()

        # ---DESCRIPCION TIPO USO--------------------------------------------------------
        insertC5['descrtipouso'] = None
        if not registro[289:389].isspace(): insertC5['descrtipouso'] = registro[289:389].lstrip()

        # ---FECHA INSCRIPCION INICIAL--------------------------------------------------------
        insertC5['fechainscripcioninicial'] = None
        if  registro[388:396].lstrip().isdigit():
            if not registro[388:396] == '00000000':
                insertC5['fechainscripcioninicial'] = datetime.datetime.strptime(registro[388:396].strip(), '%Y%m%d')

        # ----FECHA ULTIMA TRANSFERENCIA-------------------------------------------------------
        insertC5['fechaultimatransferencia'] = None
        if  registro[396:404].lstrip().isdigit():
            if not registro[396:404] == '00000000':
                insertC5['fechaultimatransferencia'] = datetime.datetime.strptime(registro[396:404].strip(), '%Y%m%d')

        # ----FECHA ULTIMO MOVIMIENTO-------------------------------------------------------
        insertC5['fechaultimomovimiento'] = None
        if registro[404:412].lstrip().isdigit():
            if not registro[404:412] == '00000000':
                insertC5['fechaultimomovimiento'] = datetime.datetime.strptime(registro[404:412].strip(), '%Y%m%d')

        # ----Estado Dominial-------------------------------------------------------
        insertC5['estadodominial'] = None
        if not registro[413:414].isspace(): insertC5['estadodominial'] = registro[413:414].lstrip()

        # ----FECHA CAMBIO ESTADO DOMINIAL-------------------------------------------------------
        insertC5['fechacambioestadodominal'] = None
        if registro[413:422].lstrip().isdigit():
            if not registro[413:422] == '00000000':
                insertC5['fechacambioestadodominal'] = datetime.datetime.strptime(registro[413:422].strip(), '%Y%m%d')

        # ----GUARDA HABITUAL-------------------------------------------------------
        insertC5['guardahabitual'] = None
        if not registro[422:423].isspace(): insertC5['guardahabitual'] = registro[422:423].lstrip()

        # ----CALLE-------------------------------------------------------
        insertC5['calle'] = None
        if not registro[423:463].isspace(): insertC5['calle'] = registro[423:463].lstrip()

        # ----NUMERO DE PUERTA-------------------------------------------------------
        insertC5['numero'] = None
        if not registro[463:473].isspace(): insertC5['numero'] = registro[463:473].lstrip()

        # ----PISO-------------------------------------------------------
        insertC5['piso'] = None
        if not registro[473:483].isspace(): insertC5['piso'] = registro[473:483].lstrip()

        # ----DEPARTAMENTO-------------------------------------------------------
        insertC5['departamento'] = None
        if not registro[483:493].isspace(): insertC5['departamento'] = registro[483:493].lstrip()

        # ----BARRIO-------------------------------------------------------
        insertC5['barrio'] = None

        # ----LOCALIDAD-------------------------------------------------------
        insertC5['localidad'] = None
        if not registro[493:533].isspace(): insertC5['localidad']  = registro[493:533].lstrip()

        # ----CODIGO POSTAL-------------------------------------------------------
        insertC5['codigopostal'] = None
        if not registro[533:541].isspace(): insertC5['codigopostal'] = registro[533:541].lstrip()

        # ----PROVINCIA-------------------------------------------------------
        insertC5['provinciaid'] = readProvincia(**{'provincia': registro[540:543]})

        # ----CANTIDAD TITULARES-------------------------------------------------------
        insertC5['cantidadtitulares'] = None
        if registro[543:545].lstrip().isdigit(): insertC5['cantidadtitulares'] = int(registro[543:545])

        # ----CODIGO REGISTRO SECCIONAL-------------------------------------------------------
        insertC5['codigoregistroseccional'] = None
        if registro[545:550].lstrip().isdigit(): insertC5['codigoregistroseccional'] = int(registro[545:550])

        # -----RAZON SOCIAL------------------------------------------------------
        insertC5['razonsocial'] = None
        if not registro[550:590].isspace(): insertC5['razonsocial'] = registro[550:590].lstrip()

        # -----FECHA OPERACION------------------------------------------------------
        insertC5['fechaoperacion'] =datetime.datetime.strptime(registro[589:604].strip(), '%Y%m%d%H%M%S')

        # -----RESERVADO------------------------------------------------------
        insertC5['reservado'] = None
        if not registro[604:860].isspace():  insertC5['reservado'] = registro[604:860].lstrip()

        # -----TIMESTAMP------------------------------------------------------
        insertC5['ktimestamp'] = datetime.datetime.now()

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # write la tabla INFORMACION VEHICULO
        data_Input.campos.clear()
        respuesta = data_Input.add_Dal(objetoInfVehiculo, **insertC5)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # obtengo el ultimo id si la respuesta fue exitosa
        if respuesta:
            #if relacion['C'] == None: relacion['C'] = data_Input.ultimoid
            if relacion['C'] == None: relacion['C'] = totalC
        return respuesta

    except Exception as e:
        print(f'Error en tipoRegistroC5 {e} total {total}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Tratamiento para la tabla INFORMACION DEL VEHICULO TITULAR
def tipoRegistroC5Titular(totalT):

    try:

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # cargamos el diccionario del registro de la tabla INFORMACION DEL VEHICULO TITULAR
        insertTitular = dict()

        insertTitular['infvehiculotitularid'] = totalT

        # ----TIPO CUERPO-------------------------------------------------------
        insertTitular['tipocuerpoid'] = readTipoCuerpo(**{'tipocuerpo': registro[0:2]})

        # ----TIPO SUB REGISTRO-------------------------------------------------------
        insertTitular['tiposubregistroid'] = readTipoSubRegistro(**{'tiposubregistro': registro[2:3]})

        # ----TIPO DOCUMENTO-------------------------------------------------------
        insertTitular['tipodocumentoid'] = readTipoDocumento(**{'tipodocumento': int(registro[3:5])})

        # ----NUMERO DOCUMENTO-------------------------------------------------------
        insertTitular['numerodocumento'] = None
        if registro[5:16].lstrip().isdigit(): insertTitular['numerodocumento'] = int(registro[5:16])

        # ----CUIT/CUIL-------------------------------------------------------
        insertTitular['cuitcuil'] = None
        if registro[16:27].lstrip().isdigit(): insertTitular['cuitcuil'] = int(registro[16:27])

        # ----APELLIDO NOMBRE-------------------------------------------------------
        insertTitular['apellidonombre'] = None
        if not registro[27:177].isspace(): insertTitular['apellidonombre'] = registro[27:177].lstrip()

        # ----PORCENTAJE TITULAR-------------------------------------------------------
        insertTitular['porcentajetitularidad'] = None
        if registro[177:180].lstrip().isdigit(): insertTitular['porcentajetitularidad'] = int(registro[177:180])

        # ----CALLE-------------------------------------------------------
        insertTitular['calle'] = None
        if not registro[180:220].isspace(): insertTitular['calle'] = registro[180:220].lstrip()

        # -----NUMERO DE PUERTA------------------------------------------------------
        insertTitular['numero'] = None
        if not registro[220:230].isspace(): insertTitular['numero'] = registro[220:230].lstrip()

        # -----PISO------------------------------------------------------
        insertTitular['piso'] = None
        if not registro[230:240].isspace():  insertTitular['piso'] = registro[230:240].lstrip()

        # -----DEPARTAMENTO------------------------------------------------------
        insertTitular['departamento'] = None
        if not registro[240:250].isspace(): insertTitular['departamento'] = registro[240:250].lstrip()

        # -----BARRIO------------------------------------------------------
        insertTitular['barrio'] = None
        if not registro[250:290].isspace(): insertTitular['barrio'] = registro[250:290].lstrip()

        # -----LOCALIDAD------------------------------------------------------
        insertTitular['localidad'] = None
        if not registro[290:330].isspace(): insertTitular['localidad'] = registro[290:330].lstrip()

        # -----CODIGO POSTAL------------------------------------------------------
        insertTitular['codigopostal'] = None
        if not registro[330:338].isspace(): insertTitular['codigopostal'] = registro[330:338].lstrip()

        # -----PROVINCIA------------------------------------------------------
        insertTitular['provinciaid'] = readProvincia(**{'provincia': registro[338:340]})

        # -----RESERVADO------------------------------------------------------
        insertTitular['reservado'] = None
        if not registro[340:596].isspace(): insertTitular['reservado'] = registro[340:596].lstrip()

        # -----CONTROL SUCERP------------------------------------------------------
        insertTitular['controlsucerp'] = None

        # -----TIMESTAMP------------------------------------------------------
        insertTitular['ktimestamp'] = datetime.datetime.now()



        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # write la tabla INFORMACION VEHICULO TITULAR
        data_Input.campos.clear()
        respuesta = data_Input.add_Dal(objetoInfVehiculoTit, **insertTitular)


        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # obtengo el ultimo id si la respuesta fue exitosa
        if respuesta:
            listaTitulares = list()
            listaTitulares = relacion['T']
            #listaTitulares.append(data_Input.ultimoid)
            listaTitulares.append(totalT)
            relacion['T'] = listaTitulares


        return respuesta

    except Exception as e:
        print(f'Error en tipoRegistroC5 {e} total {total}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Tratamiento para la tabla PIE
def tipoRegistroP0():

    try:

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # cargamos el diccionario del registro de la tabla PIE
        insertPie = dict()

        # ----TIPO REGISTRO-------------------------------------------------------
        insertPie['tiporegistroid'] = readTipoRegistro(**{'tiporegistro': registro[0:2]})

        # ----CANTIDAD DE REGISTROS-------------------------------------------------------
        insertPie['cantidadregistros'] = None
        if registro[2:10].lstrip().isdigit(): insertPie['cantidadregistros'] = int(registro[2:10])

        # ----NOMBRE DE ARCHIVO-------------------------------------------------------
        insertPie['checksum'] = None
        if not registro[10:42].isspace(): insertPie['checksum'] = registro[10:42]

        # -----Tiemstamp------------------------------------------------------
        insertPie['ktimestamp'] = datetime.datetime.now()

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # write la tabla PIE
        data_Input.campos.clear()
        respuesta = data_Input.add_Dal(objetoPie, **insertPie)

        return respuesta

    except Exception as e:
         print(f'Error en tipoRegistroP0 {e} total {total}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# actualiza el titular en la tabla informacion vehiculo
def actualizaTitular():

    # navegamos dentro de la lista de titulares para asignar el vehiculo
    for key in relacion['T']:

        # actualizar la tabla INFORMACION VEHICULO TITULAR
        data = {'infvehiculoid': relacion['C']}
        respuesta = data_Input.upd_Dal(objetoInfVehiculoTit, key, **data)

    relacion['C'] = None
    relacion['T'] = []



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# DEFINIMOS E INICIALIZAMOS LOS OBJETOS A UTILIZAR

# Obtengo la fecha de proceso
fechaproceso = datetime.datetime.now()

# definimos la conexion de datos solo DDS------------------
data_Input_Dds = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_DDS)

# definimos la conexion de datos ------------------
data_Input = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_GX)


# obtenemos el idTabla  y el objeto_dal de TABLA_TIPO_REGISTRO -----------
idTipoCuerpo = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_CUERPO']['numero']
objetoTipoCuerpo = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_CUERPO']['objeto'])

# obtenemos el idTabla  y el objeto_dal de TABLA_TIPO_REGISTRO -----------
idTipoRegistro = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_REGISTRO']['numero']
objetoTipoRegistro = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_REGISTRO']['objeto'])

# obtenemos el idTabla  y el objeto_dal de TABLA_TIPO_SUB_REGISTRO -----------
idTipoSubRegistro = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_SUB_REGISTRO']['numero']
objetoTipoSubRegistro = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_SUB_REGISTRO']['objeto'])

# obtenemos el idTabla  y el objeto_dal de TABLA_TIPO_ORIGEN -----------
idTipoSubRegistro = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_ORIGEN']['numero']
objetoTipoOrigen = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_ORIGEN']['objeto'])

# obtenemos el idTabla  y el objeto_dal de TABLA_TIPO_DOCUMENTO -----------
idTipoDocumento = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_DOCUMENTO']['numero']
objetoTipoDocumento = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_DOCUMENTO']['objeto'])

# obtenemos el idTabla  y el objeto_dal de TABLA_PROVINCIA -----------
idProvincia = ConfigurarAplicacion.LISTA_TABLAS['TABLA_PROVINCIA']['numero']
objetoProvincia = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_PROVINCIA']['objeto'])


# obtenemos el idTabla  y el objeto_dal de TABLA_ENCABEZADO -------------------
idEncabezado = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ENCABEZADO']['numero']
objetoEncabezado = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_ENCABEZADO']['objeto'])

# obtenemos el idTabla  y el objeto_dal de TABLA_TMPINFORMACIONVEHICULO -------------------
idInfVehiculo = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TMPINFORMACIONVEHICULO']['numero']
try:
    objetoInfVehiculo = data_Input_Dds.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_TMPINFORMACIONVEHICULO']['objeto'])
except Exception as e:
    print(f'Falta algun modulo {e}')


#objetoInfVehiculo = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_INFORMACIONVEHICULO']['objeto'])

# obtenemos el idTabla  y el objeto_dal de TABLA_TMPINFORMACIONVEHICULOTITULAR -------------------
idInfVehiculoTit = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TMPINFORMACIONVEHICULOTITULAR']['numero']
try:
    objetoInfVehiculoTit = data_Input_Dds.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_TMPINFORMACIONVEHICULOTITULAR']['objeto'])
except Exception as e:
    print(f'Falta algun modulo {e}')


# obtenemos el idTabla  y el objeto_dal de TABLA_PIE -------------------
idPie = ConfigurarAplicacion.LISTA_TABLAS['TABLA_PIE']['numero']
objetoPie = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_PIE']['objeto'])







# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Establecemos la ruta donde esta el archivo
ruta = os.getcwd() + "\\Archivos_SinProcesar\\MigracionVehiculos"
os.chdir(ruta)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Establecemos el archivo de texto
#archivo_texto = "2481cfcc14ab493c51b9a4d02567bac1FIJO.txt"
archivo_texto = "2481cfcc14ab493c51b9a4d02567bac1PRUEBA.txt"
total,  totalC,  totalT = 0,  0,  0

# diccionario para la relacion entre titulares y vehiculos
relacion = { 'C': None, 'T': [] }

try:
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Open el archivo archivo de texto
    with open(archivo_texto, mode='r', encoding='latin-1') as archivo:

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # read el archivo de texto
        for linea in archivo:

            # acumulo la cantidad de registro
            total += 1

            # asigno el valor de la linea
            registro = linea

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # actualizo la relacion entre titulares y los vehiculos
            if registro[2:3] == 'C':
                if relacion['C'] != None and relacion['T'].__len__() != 0:
                    # actualizamos los titulares
                    actualizaTitular()

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # generamos el registro cabecera
            if registro[0:2] == 'E0':

                # Tratamiento de la cabecera
                respuesta = tipoRegistroE0()

                # verifica si hubo error al grabar la cabecera
                if not respuesta:
                    print('Error al grabar la cabecera...')
                    break
                else:
                    continue

            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # generamos el registro de vehiculos
            if registro[0:2] == 'C5' and registro[2:3] == 'C':

                # Tratamiento de la informacion del vehiculo automoviles
                totalC += 1
                respuesta = tipoRegistroC5(totalC)

                # verifica si hubo error al grabar la informacion vehiculos automoviles
                if not respuesta:
                    print('Error al grabar la informacion vehiculos automoviles...')
                    break
                else:
                    continue


            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # generamos el registro de titular
            if registro[0:2] == 'C5' and registro[2:3] == 'T':

                # Tratamiento de la informacion del vehiculo automoviles
                totalT += 1
                respuesta = tipoRegistroC5Titular(totalT)

                # verifica si hubo error al grabar la informacion vehiculos titular
                if not respuesta:
                    print('Error al grabar la informacion vehiculos titular...')
                    break
                else:
                    continue


            # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # generamos el registro de pie
            if registro[0:2] == 'P0':

                # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                # actualizo la relacion de de los titulares y los vehiculos
                if relacion['C'] != None and relacion['T'].__len__() != 0:
                    # actualizamos los titulares
                    actualizaTitular()

                # Tratamiento de la informacion del vehiculo automoviles
                respuesta = tipoRegistroP0()

                # verifica si hubo error al grabar la informacion vehiculos titular
                if not respuesta:
                    print('Error al grabar la informacion vehiculos titular...')
                    break
                else:
                    continue

        # proceso completado
        print(f'proceso completado....total C = {totalC}    total T = {totalT} total leidos {total}')


except Exception as e:
    print(f'total {total} - Error en el tronco del procedimiento {e}')


