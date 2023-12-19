# -------Lista de lisbrerias y Modulos
try:

    # ---------------LIBRERIAS DE FECHA Y HORA
    import datetime
    import copy

    # Tipo de dato decimal
    import decimal
    from app_Abstract.atributosAbstract import AtributosSucerp, AtributosGx

    from app_Config.config import ConfigurarAplicacion
    import pyodbc
    from pydal.adapters.db2 import DB2Pyodbc


    # --------------LIBRERIA PYDAL
    # --- PARA LA DEFINICION DE TABLAS Y LOS CAMPOS DE ELLAS
    from pydal import DAL, Field
    from pydal.objects import Table

except Exception as e:
    print(f'Falta algun modulo {e}')

"""
Son los Tipos de datos  y referencias para capa abstracta

types = {
    'boolean': 'CHAR(1)',
    'string': 'VARCHAR(%(length)s)',
    'text': 'CLOB',
    'json': 'CLOB',
    'password': 'VARCHAR(%(length)s)',
    'blob': 'BLOB',
    'upload': 'VARCHAR(%(length)s)',
    'integer': 'INT',
    'bigint': 'BIGINT',
    'float': 'REAL',
    'double': 'DOUBLE',
    'decimal': 'NUMERIC(%(precision)s,%(scale)s)',
    'date': 'DATE',
    'time': 'TIME',
    'datetime': 'TIMESTAMP',
    'id': 'INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL',
    'reference': 'INT, FOREIGN KEY (%(field_name)s) REFERENCES %(foreign_key)s ON DELETE %(on_delete_action)s',
    'list:integer': 'CLOB',
    'list:string': 'CLOB',
    'list:reference': 'CLOB',
    'big-id': 'BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY NOT NULL',
    'big-reference': 
        'BIGINT, FOREIGN KEY (%(field_name)s) REFERENCES %(foreign_key)s ON DELETE %(on_delete_action)s',
    'reference FK': 
        ', CONSTRAINT FK_%(constraint_name)s 
            FOREIGN KEY (%(field_name)s) 
            REFERENCES %(foreign_key)s ON DELETE %(on_delete_action)s',
    'reference TFK': 
        ' CONSTRAINT FK_%(foreign_table)s_PK 
            FOREIGN KEY (%(field_name)s) 
            REFERENCES %(foreign_table)s (%(foreign_key)s) ON DELETE %(on_delete_action)s',
    }
"""


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# El objetivo de esta clase es poder obtener el diccionario de un Objeto Tabla
class ToolsAbatract():
    """
    El objetivo de esta clase es poder recuperar los elmentos para poder gestionar las bases de datos:\n
        La key  de una tabla\n
        El registro a actualizar\n
        Los campos de la estructura de la Tabla\n
        Almacenado en gestion_Tablas_dict\n
    """

    def __init__(self):

        # Tabla
        self.__tabla = None

        # Campos del Mensaje
        self.__key = dict()
        self.__registro = dict()
        self.__campos = dict()

        # Gestion de las Tablas
        self.__gestion_Tablas_dict = dict()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Encapsulacion de los atributos

    # ----------DETERMINA EL CAMPOS ID DE LA TABLA--------------------------------
    @property
    def tabla(self):
        return self.__tabla

    @tabla.setter
    def tabla(self, valor):
        self.__tabla = valor
        self.__id_Tabla = self.__tabla._id.longname
        self.__id_Tabla = self.__id_Tabla[(self.__id_Tabla.find('.') + 1):]

    # ----------CAMPOS DE LA TABLAS--------------------------------
    @property
    def campos(self):
        return self.__campos

    @campos.setter
    def campos(self, valor):
        campos = valor
        for c in campos:
            if c != self.__id_Tabla:
                self.__campos[c] = None

    # ----KEY DE LAS TABLAS------------------------
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, valor):
        self.__key = valor

    # ----REGISTRO DE LAS TABLAS------------------------
    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, valor):
        self.__registro = valor

    # ----MENSAJE INSERT------------------------
    @property
    def mensaje_insert(self):
        self.__mensaje_insert = {'datos': self.registro}
        return self.__mensaje_insert

    # ----GESTION TABLAS------------------------
    @property
    def gestion_Tablas_dict(self):
        return self.__gestion_Tablas_dict

    @gestion_Tablas_dict.setter
    def gestion_Tablas_dict(self, valor):
        self.__gestion_Tablas_dict = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Obtiene el diccionario de manejo de la tabla
    def getTableTools(self, tabla):

        if type(tabla) is Table:
            self.tabla = tabla
            self.campos = tabla.fields()
            self.key, self.registro = {self.__id_Tabla: None}, self.campos
            self.gestion_Tablas_dict[tabla._id.tablename] = dict()
            self.gestion_Tablas_dict[tabla._id.tablename]['table'] = tabla
            self.gestion_Tablas_dict[tabla._id.tablename]['campos'] = self.campos
            self.gestion_Tablas_dict[tabla._id.tablename]['insert'] = self.mensaje_insert
            self.gestion_Tablas_dict[tabla._id.tablename]['update'] = {'clave': self.key, 'registro': self.registro}
            self.gestion_Tablas_dict[tabla._id.tablename]['update'] = {'clave': self.key}
            return self.gestion_Tablas_dict


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# El objetivo de esta clase es poder describir los campos de cada tabla que estan en motor SQLITE
class SqliteAbstractDb():

    def __init__(self, db):

        # Conexion
        self.db = db

        # ------------------------------------------------------
        # Tablas del Validator
        self.__mensajesError = None
        self.__mensajesErrorMsgdDinamicos = None
        self.__msgNivelGravedad = None
        self.__userPathFile = None
        self.__usuario = None

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----USERPATHFILE
    #     FOR SYSTEM NAME USERP00001------------------------
    @property
    def sq_userPathFile_Dal(self):
        if self.__userPathFile is None:
            try:
                self.__userPathFile = self.db.define_table(
                    'USERPATHFILE',
                    Field('USERPATHFILEID', type='id', label='Id'),
                    Field('USERNAME', type='string', length=10, required=True, label='Nombre Usuario'),
                    Field('USERPATHFILEMODULO', type='string', length=50, required=True, label='Modulo del Usuario'),
                    Field('USERPATHFILEPATH', type='string', length=50, required=True, label='Path de Files'),
                    Field('USEROUTPUT', type='string', length=1, required=True, label='OutPut'),
                    Field('USERLINKPROD', type='string', length=512, required=True, label='User Link Prod'),
                    Field('USERLINKTEST', type='string', length=512, required=True, label='User Link Test'),
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__userPathFile

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.MSGNIVELGRAVEDAD
    #     FOR SYSTEM NAME MSGNI00001------------------------
    @property
    def sq_msgNivelGravedad_Dal(self):
        if self.__msgNivelGravedad is None:
            try:
                self.__msgNivelGravedad = self.db.define_table(
                    'MSGNIVELGRAVEDAD',
                    Field('NIVELGRAVEDADID', type='id', label='Id'),
                    Field('NIVELGRAVEDADDESCRIPCION', type='string', length=50, required=True, label='Descripcion'),
                    Field('MSGNIVELGRAVEDADALERTA', type='string', length=50, required=True, label='Ayuda Mensaje'),
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__msgNivelGravedad

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.MENSAJESERROR
    #     FOR SYSTEM NAME MENSA00001------------------------
    @property
    def sq_mensajeError_Dal(self):
        if self.__mensajesError is None:
            try:
                self.__mensajesError = self.db.define_table(
                    'MENSAJESERROR',
                    Field('MSGCODE', type='string', length=7, required=True, label='Mensaje Codigo'),
                    Field('MSGDESCRIPCION', type='string', length=150, required=True, label='Descripcion'),
                    Field('MSGHELP', type='string', length=1024, required=True, label='Ayuda Mensaje'),
                    Field('NIVELGRAVEDADID', 'reference MSGNIVELGRAVEDAD', label='Id', ondelete='CASCADE'),
                    primarykey=['MSGCODE'],
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__mensajesError

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.MENSAJESERRORMSGDINAMICOS
    #     FOR SYSTEM NAME MENSA00002------------------------
    @property
    def sq_mensajesErrorMsgdDinamicos_Dal(self):
        if self.__mensajesErrorMsgdDinamicos is None:
            try:
                self.__mensajesErrorMsgdDinamicos = self.db.define_table(
                    'MENSAJESERRORMSGDINAMICOS',
                    Field('MSGCODE', type='integer', required=True, label='Codigo del Mensaje'),
                    Field('MSGDINAMICOID', type='integer', required=True, label='Mensaje Dinamico Id'),
                    Field('MSGDINAMICOLEN', type='integer', required=True, label='Ayuda Mensaje'),
                    primarykey=['MSGCODE', 'MSGDINAMICOID'],
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__mensajesErrorMsgdDinamicos


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class GxAbstractDb():
    """
    EL OBJTIVO DE ESTA CLASE ES PODER DESCRIBIR LOS CAMPOS DE LAS TABLAS QUE ESTAN EN EL MOTOR ISERIES O MYSQL \n
    EN EL CASO DEL ISERIES LAS TABLAS ESTAN EN LA BIBLIOTECA GXPROD O GXTST DE ACUERDO A LA CONFIGURACION \n
    CUANDO TRABAJAMOS SIN CONEXION A LA ISERIES SE TRABAJA CON MYSQL \n

    """

    def __init__(self, db):

        # Conexion
        self.db = db

        # Formatos
        self.formatosSucerp = AtributosSucerp()
        #self.formatosGx = AtributosGx()

        # diccionario de objetos tablas
        self.__GxdictObjetosTablas = dict()


        # ------------------------------------------------------
        # Tablas de GxProd

        self.__tipoRegistro = None
        self.__tipoSubRegistro = None
        self.__tipoCuerpo = None
        self.__tipoTitular = None
        self.__tipoOrigen = None
        self.__tipoMovimiento = None
        self.__tipoCuota = None
        self.__tipoPago = None
        self.__tipoMoneda = None
        self.__tipoDocumento = None
        self.__provincias = None
        self.__estado = None
        self.__encabezado = None

        self.__registroEncabezado = None
        self.__altaImpositiva = None
        self.__altaImpositivaTitular = None
        self.__bajaImpositiva = None
        self.__bajaImpositivaTitular = None
        self.__impuestoSellos = None
        self.__impuestoSellosPartes = None
        self.__impuestoSellosPartesTipoTramite = None
        self.__impuestoAutomotor = None

        self.__informacionVehiculo = None
        self.__informacionVehiculoTitular = None
        self.__cambioTitularidad = None
        self.__cambioTitularidadTitular = None
        self.__informacionRadicacion = None
        self.__anulacionTramitesSellos = None
        self.__anulacionTramitesSellosDetalle = None
        self.__tramitesGenerales = None
        self.__tramitesGeneralesTitular = None
        self.__pie = None

        self.__apiAumoso = None
        self.__apiToken = None
        self.__apiTokenUser = None
        self.__apiTokenUserRef = list()
        self.__apiRegistros = None
        self.__apiEstados = None
        self.__apiTareas = None
        self.__apiEstadosTareas = None
        self.__relArbaSucerpMarca = None
        self.__procesoImportacionExportacion = None
        self.__apiLog = None


        self.__tmpInformacionVehiculo = None
        self.__tmpInformacionVehiculoTitular = None




    # ----Atributos------------------------
    #@property
    #def encabezado(self):
    #    return self.__encabezado

    #@encabezado.setter
    #def encabezado(self, valor):
    #    self.__encabezado = valor

    @property
    def tipoRegistro(self):
        return self.__tipoRegistro

    @tipoRegistro.setter
    def tipoRegistro(self, valor):
        self.__tipoRegistro = valor

    @property
    def tipoSubRegistro(self):
        return self.__tipoSubRegistro

    @tipoSubRegistro.setter
    def tipoSubRegistro(self, valor):
        self.__tipoSubRegistro = valor

    @property
    def tipoCuerpo(self):
        return self.__tipoCuerpo

    @tipoCuerpo.setter
    def tipoCuerpo(self, valor):
        self.__tipoCuerpo = valor

    @property
    def tipoTitular(self):
        return self.__tipoTitular

    @tipoTitular.setter
    def tipoTitular(self, valor):
        self.__tipoTitular = valor

    @property
    def tipoOrigen(self):
        return self.__tipoOrigen

    @tipoOrigen.setter
    def tipoOrigen(self, valor):
        self.__tipoOrigen = valor

    @property
    def tipoMovimiento(self):
        return self.__tipoMovimiento

    @tipoMovimiento.setter
    def tipoMovimiento(self, valor):
        self.__tipoMovimiento = valor

    @property
    def tipoCuota(self):
        return self.__tipoCuota

    @tipoCuota.setter
    def tipoCuota(self, valor):
        self.__tipoCuota = valor

    @property
    def tipoPago(self):
        return self.__tipoPago

    @tipoPago.setter
    def tipoPago(self, valor):
        self.__tipoPago = valor

    @property
    def tipoMoneda(self):
        return self.__tipoMoneda

    @tipoMoneda.setter
    def tipoMoneda(self, valor):
        self.__tipoMoneda = valor

    @property
    def tipoDocumento(self):
        return self.__tipoDocumento

    @tipoDocumento.setter
    def tipoDocumento(self, valor):
        self.__tipoDocumento = valor

    @property
    def provincias(self):
        return self.__provincias

    @provincias.setter
    def provincias(self, valor):
        self.__provincias = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    @property
    def registroEncabezado(self):
        return self.__registroEncabezado

    @registroEncabezado.setter
    def registroEncabezado(self, valor):
        self.__registroEncabezado = valor

    @property
    def altaImpositiva(self):
        return self.__altaImpositiva

    @altaImpositiva.setter
    def altaImpositiva(self, valor):
        self.__altaImpositiva = valor

    @property
    def altaImpositivaTitular(self):
        return self.__altaImpositivaTitular

    @altaImpositivaTitular.setter
    def altaImpositivaTitular(self, valor):
        self.__altaImpositivaTitular = valor

    @property
    def bajaImpositiva(self):
        return self.__bajaImpositiva

    @bajaImpositiva.setter
    def bajaImpositiva(self, valor):
        self.__bajaImpositiva = valor

    @property
    def bajaImpositivaTitular(self):
        return self.__bajaImpositivaTitular

    @bajaImpositivaTitular.setter
    def bajaImpositivaTitular(self, valor):
        self.__bajaImpositivaTitular = valor

    @property
    def impuestoSellos(self):
        return self.__impuestoSellos

    @impuestoSellos.setter
    def impuestoSellos(self, valor):
        self.__impuestoSellos = valor

    @property
    def impuestoSellosPartes(self):
        return self.__impuestoSellosPartes

    @impuestoSellosPartes.setter
    def impuestoSellosPartes(self, valor):
        self.__impuestoSellosPartes = valor

    @property
    def impuestoSellosPartesTipoTramite(self):
        return self.__impuestoSellosPartesTipoTramite

    @impuestoSellosPartesTipoTramite.setter
    def impuestoSellosPartesTipoTramite(self, valor):
        self.__impuestoSellosPartesTipoTramite = valor

    @property
    def impuestoAutomotor(self):
        return self.__impuestoAutomotor

    @impuestoAutomotor.setter
    def impuestoAutomotor(self, valor):
        self.__impuestoAutomotor = valor

    @property
    def informacionVehiculo(self):
        return self.__informacionVehiculo

    @informacionVehiculo.setter
    def informacionVehiculo(self, valor):
        self.__informacionVehiculo = valor

    @property
    def informacionVehiculoTitular(self):
        return self.__informacionVehiculoTitular

    @informacionVehiculoTitular.setter
    def informacionVehiculoTitular(self, valor):
        self.__informacionVehiculoTitular = valor


    @property
    def tmpInformacionVehiculo(self):
        return self.__tmpInformacionVehiculo

    @tmpInformacionVehiculo.setter
    def tmpInformacionVehiculo(self, valor):
        self.__tmpInformacionVehiculo = valor

    @property
    def tmpInformacionVehiculoTitular(self):
        return self.__tmpInformacionVehiculoTitular

    @tmpInformacionVehiculoTitular.setter
    def tmpInformacionVehiculoTitular(self, valor):
        self.__tmpInformacionVehiculoTitular = valor


    @property
    def cambioTitularidad(self):
        return self.__cambioTitularidad

    @cambioTitularidad.setter
    def cambioTitularidad(self, valor):
        self.__cambioTitularidad = valor

    @property
    def cambioTitularidadTitular(self):
        return self.__cambioTitularidadTitular

    @cambioTitularidadTitular.setter
    def cambioTitularidadTitular(self, valor):
        self.__cambioTitularidadTitular = valor

    @property
    def informacionRadicacion(self):
        return self.__informacionRadicacion

    @informacionRadicacion.setter
    def informacionRadicacion(self, valor):
        self.__informacionRadicacion = valor

    @property
    def anulacionTramitesSellos(self):
        return self.__anulacionTramitesSellos

    @anulacionTramitesSellos.setter
    def anulacionTramitesSellos(self, valor):
        self.__anulacionTramitesSellos = valor

    @property
    def anulacionTramitesSellosDetalle(self):
        return self.__anulacionTramitesSellosDetalle

    @anulacionTramitesSellosDetalle.setter
    def anulacionTramitesSellosDetalle(self, valor):
        self.__anulacionTramitesSellosDetalle = valor

    @property
    def tramitesGenerales(self):
        return self.__tramitesGenerales

    @tramitesGenerales.setter
    def tramitesGenerales(self, valor):
        self.__tramitesGenerales = valor

    @property
    def tramitesGeneralesTitular(self):
        return self.__tramitesGeneralesTitular

    @tramitesGeneralesTitular.setter
    def tramitesGeneralesTitular(self, valor):
        self.__tramitesGeneralesTitular = valor

    @property
    def pie(self):
        return self.__pie

    @pie.setter
    def pie(self, valor):
        self.__pie = valor

    @property
    def apiAumoso(self):
        return self.__apiAumoso

    @apiAumoso.setter
    def apiAumoso(self, valor):
        self.__apiAumoso = valor

    @property
    def apiToken(self):
        return self.__apiToken

    @apiToken.setter
    def apiToken(self, valor):
        self.__apiToken = valor

    @property
    def apiTokenUser(self):
        return self.__apiTokenUser

    @apiTokenUser.setter
    def apiTokenUser(self, valor):
        self.__apiTokenUser = valor

    @property
    def apiTokenUserRef(self):
        return self.__apiTokenUserRef

    @apiTokenUserRef.setter
    def apiTokenUserRef(self, valor):
        self.__apiTokenUserRef = valor

    @property
    def apiRegistros(self):
        return self.__apiRegistros

    @apiRegistros.setter
    def apiRegistros(self, valor):
        self.__apiRegistros = valor

    @property
    def apiEstados(self):
        return self.__apiEstados

    @apiEstados.setter
    def apiEstados(self, valor):
        self.__apiEstados = valor

    @property
    def apiTareas(self):
        return self.__apiTareas

    @apiTareas.setter
    def apiTareas(self, valor):
        self.__apiTareas = valor

    @property
    def apiEstadosTareas(self):
        return self.__apiEstadosTareas

    @apiEstadosTareas.setter
    def apiEstadosTareas(self, valor):
        self.__apiEstadosTareas = valor

    @property
    def relArbaSucerpMarca(self):
        return self.__relArbaSucerpMarca

    @relArbaSucerpMarca.setter
    def relArbaSucerpMarca(self, valor):
        self.__relArbaSucerpMarca = valor

    @property
    def procesoImportacionExportacion(self):
        return self.__procesoImportacionExportacion

    @procesoImportacionExportacion.setter
    def procesoImportacionExportacion(self, valor):
        self.__procesoImportacionExportacion = valor


    @property
    def apiLog(self):
        return self.__apiLog

    @apiLog.setter
    def apiLog(self, valor):
        self.__apiLog = valor




    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA PROCESOIMPORTACIONEXPORTACION
    #     FOR SYSTEM NAME ------------------------
    @property
    def procesoImportacionExportacion_Dal(self):
        if self.procesoImportacionExportacion is None:
            self.procesoImportacionExportacion = self.__buildTable(self.formatosSucerp.tablaProcesoImportacionExportacion())


        return self.procesoImportacionExportacion


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA TIPOMOVIMIENTO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoMovimiento_Dal(self):
        if self.tipoMovimiento is None:
            self.tipoMovimiento = self.__buildTable(self.formatosSucerp.tablaTipoMovimiento())


        return self.tipoMovimiento

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     TABLA ENCABEZADO
    #     FOR SYSTEM NAME ------------------------
    #@property
    #def encabezado_Dal(self):
    #    if self.encabezado is None:
    #        migrate = False
    #        #self.encabezado = self.__buildTable(self.formatosSucerp.tablaEncabezado(migrate=migrate))


    #    return self.encabezado



    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TIPOREGISTRO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoRegistro_Dal(self):
        if self.tipoRegistro is None:
            self.tipoRegistro = self.__buildTable(self.formatosSucerp.tablaTipoRegistro())

        return self.tipoRegistro

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TIPORSUBEGISTRO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoSubRegistro_Dal(self):

        if self.tipoSubRegistro is None:
            self.tipoSubRegistro = self.__buildTable(self.formatosSucerp.tablaTipoSubRegistro())

        return self.tipoSubRegistro

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TIPOCUERPO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoCuerpo_Dal(self):

        if self.tipoCuerpo is None:
            self.tipoCuerpo = self.__buildTable(self.formatosSucerp.tablaTipoCuerpo())

        return self.tipoCuerpo

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TIPOTITULAR
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoTitular_Dal(self):

        if self.tipoTitular is None:
            self.tipoTitular = self.__buildTable(self.formatosSucerp.tablaTipoTitular())

        return self.tipoTitular

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TIPOORIGEN
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoOrigen_Dal(self):

        if self.tipoOrigen is None:
            self.tipoOrigen = self.__buildTable(self.formatosSucerp.tablaTipoOrigen())

        return self.tipoOrigen

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TIPOCUOTA
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoCuota_Dal(self):

        if self.tipoCuota is None:
            self.tipoCuota = self.__buildTable(self.formatosSucerp.tablaTipoCuota())

        return self.tipoCuota

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TIPOPAGO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoPago_Dal(self):

        if self.tipoPago is None:
            self.tipoPago = self.__buildTable(self.formatosSucerp.tablaTipoPago())

        return self.tipoPago

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TIPOMONEDA
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoMoneda_Dal(self):

        if self.tipoMoneda is None:
            self.tipoMoneda = self.__buildTable(self.formatosSucerp.tablaTipoMoneda())

        return self.tipoMoneda

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TIPODOCUMENTO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tipoDocumento_Dal(self):

        if self.tipoDocumento is None:
            self.tipoDocumento = self.__buildTable(self.formatosSucerp.tablaTipoDocumento())

        return self.tipoDocumento

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----PROVINCIAS
    #     FOR SYSTEM NAME ------------------------
    @property
    def provincias_Dal(self):

        if self.provincias is None:
            self.provincias = self.__buildTable(self.formatosSucerp.tablaProvincias())

        return self.provincias

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----ESTADO
    #     FOR SYSTEM NAME ------------------------
    @property
    def estado_Dal(self):

        if self.estado is None:
            self.estado = self.__buildTable(self.formatosSucerp.tablaEstado())

        return self.estado

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----ENCABEZADO
    #     FOR SYSTEM NAME ------------------------
    @property
    def registroEncabezado_Dal(self):

        if self.registroEncabezado is None:

            # Referencias a tipos de registros
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            self.registroEncabezado = self.__buildTable(self.formatosSucerp.tablaEncabezado())

            # Tablas de referencias
            self.registroEncabezado._referenced_by_list = [self.tipoRegistro]

        return self.registroEncabezado


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----RELACIONARBASUCERPMARCA
    #     FOR SYSTEM NAME ------------------------
    @property
    def relArbaSucerpMarca_Dal(self):

        if self.relArbaSucepMarca is None:
            self.relArbaSucepMarca = self.__buildTable(self.formatosSucerp.tablaRelArbaSucerpMarca())


        return self.relArbaSucepMarca






    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----ALTAIMPOSITIVA
    #     FOR SYSTEM NAME ------------------------
    @property
    def altaImpositiva_Dal(self):

        try:

            if self.altaImpositiva is None:

                # Referencias a tipos de registros
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal


                # Referencias a tipos de sub registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal


                # Referencias a tipos de origen
                if self.tipoOrigen is None:
                    self.tipoOrigen = self.tipoOrigen_Dal


                # Referencias a tipos de documento
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                # Referencias a altasimpositivatitular
                if self.altaImpositivaTitular is None:
                    self.altaImpositivaTitular = self.altaImpositivaTitular_Dal


                self.altaImpositiva = self.__buildTable(self.formatosSucerp.tablaAltaImpositiva())

                # Tablas de referencias
                self.altaImpositiva._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro,
                    self.tipoOrigen, self.tipoDocumento, self.provincias,
                    self.altaImpositivaTitular
                ]

            return self.altaImpositiva

        except Exception as inst:
            print(f'Error - altaImpositiva_Dal {e}')
            return inst

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----ALTAIMPOSITIVATITULAR
    #     FOR SYSTEM NAME ------------------------
    @property
    def altaImpositivaTitular_Dal(self):

        try:

            if self.altaImpositivaTitular is None:

                # Referencias a tipos de cuerpo
                if self.tipoCuerpo is None:
                    self.tipoCuerpo = self.tipoCuerpo_Dal

                # Referencias a tipos de sub registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencias a tipos de documento
                if self.tipoDocumento is None:
                    self.tipoDocumento = self.tipoDocumento_Dal

                # Referencias a provincias
                if self.provincias is None:
                    self.provincias = self.provincias_Dal

                self.altaImpositivaTitular = self.__buildTable(self.formatosSucerp.tablaAltaImpositivaTitular())

                # Tablas de referencias
                self.altaImpositivaTitular._referenced_by_list = [
                    self.tipoCuerpo, self.tipoSubRegistro, self.tipoDocumento, self.provincias
                ]

            return self.altaImpositivaTitular

        except Exception as inst:
            print(f'Error - altaImpositivaTitular_Dal {e}')
            return inst


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----ANULACIONTRAMITESSELLOS
    #     FOR SYSTEM NAME ------------------------
    @property
    def anulacionTramitesSellos_Dal(self):
        if self.anulacionTramitesSellos is None:

            # Referencias a tipos de registros
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            # Referencias a tipos de sub registros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Referencias a tipos de origen
            if self.tipoOrigen is None:
                self.tipoOrigen = self.tipoOrigen_Dal

            # Referencia a tipos de Pago
            if self.tipoPago is None:
                self.tipoPago = self.tipoPago_Dal

            # Referencia a tipos de Moneda
            if self.tipoMoneda is None:
                self.tipoMoneda = self.tipoMoneda_Dal

            self.anulacionTramitesSellos = self.__buildTable(self.formatosSucerp.tablaAnulacionTramitesSellos())

            # Tablas de referencias
            self.anulacionTramitesSellos._referenced_by_list = [
                self.tipoRegistro, self.tipoSubRegistro, self.tipoOrigen, self.tipoPago, self.tipoMoneda
            ]

        return self.anulacionTramitesSellos

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----ANULACIONTRAMITESSELLOSDETALLE
    #     FOR SYSTEM NAME ------------------------
    @property
    def anulacionTramitesSellosDetalle_Dal(self):

        try:

            if self.anulacionTramitesSellosDetalle is None:

                # Referencias a tipos de registros
                if self.tipoRegistro is None:
                    self.tipoRegistro = self.tipoRegistro_Dal

                # Referencias a tipos de sub registros
                if self.tipoSubRegistro is None:
                    self.tipoSubRegistro = self.tipoSubRegistro_Dal

                # Referencia a tipos de Moneda
                if self.tipoCuota is None:
                    self.tipoCuota = self.tipoCuota_Dal

                # Referencia a anulaciontramitesellos
                if self.anulacionTramitesSellos is None:
                    self.anulacionTramitesSellos = self.anulacionTramitesSellos_Dal



                self.anulacionTramitesSellosDetalle = self.__buildTable(
                    self.formatosSucerp.tablaAnulacionTramitesSellosDetalle())

                # Tablas de referencias
                self.anulacionTramitesSellosDetalle._referenced_by_list = [
                    self.tipoRegistro, self.tipoSubRegistro, self.tipoCuota, self.anulacionTramitesSellos
                ]

            return self.anulacionTramitesSellosDetalle

        except Exception as inst:
            print(f'Error - anulacionTramitesSellosDetalle_Dal {e}')
            return inst


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----APIESTADOS
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiEstados_Dal(self):
        if self.apiEstados is None:
            self.apiEstados = self.__buildTable(self.formatosSucerp.tablaApiEstados())

        return self.apiEstados

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----APITAREAS
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiTareas_Dal(self):
        if self.apiTareas is None:
            self.apiTareas = self.__buildTable(self.formatosSucerp.tablaApiTareas())

        return self.apiTareas

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----APIESTADOSTAREAS
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiEstadosTareas_Dal(self):
        if self.apiEstadosTareas is None:

            # Referencia a api Estados
            if self.apiEstados is None:
                self.apiEstados = self.apiEstados_Dal

            # Referencia a api Tareas
            if self.apiTareas is None:
                self.apiTareas = self.apiTareas_Dal

            self.apiEstadosTareas = self.__buildTable(self.formatosSucerp.tablaApiEstadosTareas())

            # Tablas de referencias
            self.apiEstadosTareas._referenced_by_list = [
                self.apiEstados, self.apiTareas
            ]

        return self.apiEstadosTareas

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----APIREGISTROS
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiRegistros_Dal(self):
        if self.apiRegistros is None:

            # Referencia a api Estados Tareas
            if self.apiEstadosTareas is None:
                self.apiEstadosTareas = self.apiEstadosTareas_Dal

            self.apiRegistros = self.__buildTable(self.formatosSucerp.tablaApiRegistros())

            # Tablas de referencias
            self.apiRegistros._referenced_by_list = [self.apiEstadosTareas]

        return self.apiRegistros

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----APITOKENUSER
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiTokenUser_Dal(self):
        if self.apiTokenUser is None:

            # Tabla de Tipo de Documento
            if self.tipoDocumento is None:
                self.tipoDocumento = self.tipoDocumento_Dal

            # Tabla ref APIREGISTROS
            if self.apiRegistros is None:
                self.apiRegistros = self.apiRegistros_Dal

            self.apiTokenUser = self.__buildTable(self.formatosSucerp.tablaApiTokenUser())

            # Tablas de referencias
            self.apiTokenUser._referenced_by_list = [self.tipoDocumento, self.apiRegistros]

        return self.apiTokenUser


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----APILOG
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiLog_Dal(self):

        try:
            if self.apiLog is None:
                self.apiLog = self.__buildTable(self.formatosSucerp.tablaApiLog())

            return self.apiLog

        except Exception as e:
            print(e)


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----APITOKEN
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiToken_Dal(self):

        if self.apiToken is None:

            # Tabla ref api Token User
            if self.apiTokenUser is None:
                self.apiTokenUser = self.apiTokenUser_Dal

            # Tabla ref api Registros
            if self.__apiRegistros is None:
                self.__apiRegistros = self.apiRegistros_Dal

            # Referencia a api Estados Tareas
            if self.apiEstadosTareas is None:
                self.apiEstadosTareas = self.apiEstadosTareas_Dal

            if self.apiToken is None:
                self.apiToken = self.__buildTable(self.formatosSucerp.tablaApiToken())

            # Tablas de referencias
            self.apiToken._referenced_by_list = [
                self.apiTokenUser, self.apiRegistros, self.apiEstadosTareas
            ]

        return self.apiToken

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----BAJAIMPOSITIVA
    #     FOR SYSTEM NAME ------------------------
    @property
    def bajaImpositiva_Dal(self):

        if self.bajaImpositiva is None:

            # Tabla tipo de Registros
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            # Tabla tipo de Sub Registros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Tabla tipo de Origen
            if self.tipoOrigen is None:
                self.tipoOrigen = self.tipoOrigen_Dal

            # Tabla bajaimpositivatitular
            if self.bajaImpositivaTitular is None:
                self.bajaImpositivaTitular = self.bajaImpositivaTitular_Dal


            self.bajaImpositiva = self.__buildTable(self.formatosSucerp.tablaBajaImpositiva())

            # Tablas de referencias
            self.bajaImpositiva._referenced_by_list = [
                self.tipoRegistro, self.tipoSubRegistro, self.tipoOrigen, self.bajaImpositivaTitular
            ]

        return self.bajaImpositiva

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----BAJAIMPOSITIVATITULAR
    #     FOR SYSTEM NAME ------------------------
    @property
    def bajaImpositivaTitular_Dal(self):
        if self.bajaImpositivaTitular is None:

            # Tabla tipo de Cuerpo
            if self.tipoCuerpo is None:
                self.tipoCuerpo = self.tipoCuerpo_Dal

            # Tabla tipo de Sub Registros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Referencias a tipos de documento
            if self.tipoDocumento is None:
                self.tipoDocumento = self.tipoDocumento_Dal

            # Referencias a provincias
            if self.provincias is None:
                self.provincias = self.provincias_Dal

            self.bajaImpositivaTitular = self.__buildTable(self.formatosSucerp.tablaBajaImpositivaTitular())

            # Tablas de referencias
            self.bajaImpositivaTitular._referenced_by_list = [
                self.tipoCuerpo, self.tipoSubRegistro, self.tipoDocumento, self.provincias
            ]
        return self.bajaImpositivaTitular

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----CAMBIOTITULARIDAD
    #     FOR SYSTEM NAME ------------------------
    @property
    def cambioTitularidad_Dal(self):

        if self.cambioTitularidad is None:

            # Tabla tipo de Registros
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            # Tabla tipo de Sub Registros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Tabla tipo de Cuerpo
            if self.tipoCuerpo is None:
                self.tipoCuerpo = self.tipoCuerpo_Dal

            # Referencias a tipos de documento
            if self.tipoDocumento is None:
                self.tipoDocumento = self.tipoDocumento_Dal

            # Referencias a provincias
            if self.provincias is None:
                self.provincias = self.provincias_Dal

            # Referencias a cambiotitularidadtitular
            if self.cambioTitularidadTitular is None:
                self.cambioTitularidadTitular = self.cambioTitularidadTitular_Dal


            self.cambioTitularidad = self.__buildTable(self.formatosSucerp.tablaCambioTitularidad())

            # Tablas de referencias
            self.cambioTitularidad._referenced_by_list = [
                self.tipoRegistro, self.tipoCuerpo, self.tipoSubRegistro, self.tipoDocumento, self.provincias,
                self.cambioTitularidadTitular
            ]

        return self.cambioTitularidad

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----CAMBIOTITULARIDADTITULAR
    #     FOR SYSTEM NAME ------------------------
    @property
    def cambioTitularidadTitular_Dal(self):

        if self.cambioTitularidadTitular is None:

            # Tabla tipo de Cuerpo
            if self.tipoCuerpo is None:
                self.tipoCuerpo = self.tipoCuerpo_Dal

            # Tabla tipo de Sub Registros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Tabla tipo de Titular
            if self.tipoTitular is None:
                self.tipoTitular = self.tipoTitular_Dal

            # Referencias a tipos de documento
            if self.tipoDocumento is None:
                self.tipoDocumento = self.tipoDocumento_Dal

            # Referencias a provincias
            if self.provincias is None:
                self.provincias = self.provincias_Dal

            self.cambioTitularidadTitular = self.__buildTable(self.formatosSucerp.tablaCambioTitularidadTitular())

            # Tablas de referencias
            self.cambioTitularidadTitular._referenced_by_list = [
                self.tipoCuerpo, self.tipoSubRegistro, self.tipoTitular, self.tipoDocumento, self.provincias
            ]

        return self.cambioTitularidadTitular

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----IMPUESTOAUTOMOTOR
    #     FOR SYSTEM NAME ------------------------
    @property
    def impuestoAutomotor_Dal(self):

        if self.impuestoAutomotor is None:

            # Tabla tipo de Cuerpo
            if self.tipoCuerpo is None:
                self.tipoCuerpo = self.tipoCuerpo_Dal

            # Tabla tipo de Movimeinto
            if self.tipoMovimiento is None:
                self.tipoMovimiento = self.tipoMovimiento_Dal

            # Tabla tipo de Registro
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            # Referencias a tipos de Pago
            if self.tipoPago is None:
                self.tipoPago = self.tipoPago_Dal

            # Referencias a tipos de Monedas
            if self.tipoMoneda is None:
                self.tipoMoneda = self.tipoMoneda_Dal

            self.impuestoAutomotor = self.__buildTable(self.formatosSucerp.tablaImpuestoAutomotor())

            # Tablas de referencias
            self.impuestoAutomotor._referenced_by_list = [
                self.tipoCuerpo, self.tipoMovimiento, self.tipoRegistro, self.tipoPago, self.tipoMoneda
            ]

        return self.impuestoAutomotor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----IMPUESTOSELLOS
    #     FOR SYSTEM NAME ------------------------
    @property
    def impuestoSellos_Dal(self):

        if self.impuestoSellos is None:

            # Tabla tipo de Registro
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            # Tabla tipo de Sub Registros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Tabla tipo de Origen
            if self.tipoOrigen is None:
                self.tipoOrigen = self.tipoOrigen_Dal

            # Tabla tipo de Pago
            if self.tipoPago is None:
                self.tipoPago = self.tipoPago_Dal

            # Tabla tipo de Moneda
            if self.tipoMoneda is None:
                self.tipoMoneda = self.tipoMoneda_Dal

            self.impuestoSellos = self.__buildTable(self.formatosSucerp.tablaImpuestosSellos())

            # Tablas de referencias
            self.impuestoSellos._referenced_by_list = [
                self.tipoRegistro, self.tipoSubRegistro, self.tipoOrigen, self.tipoPago, self.tipoMoneda
            ]

        return self.impuestoSellos

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----IMPUESTOSELLOSPARTES
    #     FOR SYSTEM NAME ------------------------
    @property
    def impuestoSellosPartes_Dal(self):

        if self.impuestoSellosPartes is None:

            # Tabla tipo de Cuerpo
            if self.tipoCuerpo is None:
                self.tipoCuerpo = self.tipoCuerpo_Dal

            # Tabla tipo de Sub Registros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Tabla tipo de Documento
            if self.tipoDocumento is None:
                self.tipoDocumento = self.tipoDocumento_Dal

            # Tabla de Provincias
            if self.provincias is None:
                self.provincias = self.provincias_Dal

            self.impuestoSellosPartes = self.__buildTable(self.formatosSucerp.tablaImpuestosSellosPartes())

            # Tablas de referencias
            self.impuestoSellosPartes._referenced_by_list = [
                self.tipoCuerpo, self.tipoSubRegistro, self.tipoDocumento, self.provincias
            ]

        return self.impuestoSellosPartes

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----IMPUESTOSELLOSPARTESTIPOTRAMITE
    #     FOR SYSTEM NAME ------------------------
    @property
    def impuestoSellosPartesTipoTramite_Dal(self):

        if self.impuestoSellosPartesTipoTramite is None:

            # Tabla tipo de Cuerpo
            if self.tipoCuerpo is None:
                self.tipoCuerpo = self.tipoCuerpo_Dal

            # Tabla tipo de Sub Registros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            self.impuestoSellosPartesTipoTramite = \
                self.__buildTable(self.formatosSucerp.tablaImpuestosSellosPartesTipoTramite())

            # Tablas de referencias
            self.impuestoSellosPartesTipoTramite._referenced_by_list = [
                self.tipoCuerpo, self.tipoSubRegistro
            ]

        return self.impuestoSellosPartesTipoTramite

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----INFORMACIONVEHICULO
    #     FOR SYSTEM NAME ------------------------
    @property
    def informacionVehiculo_Dal(self):

        if self.informacionVehiculo is None:

            # Tabla tipo de Registro
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            # Tabla tipo de Sub Registros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Tabla tipo de Origen
            if self.tipoOrigen is None:
                self.tipoOrigen = self.tipoOrigen_Dal

            # Tabla provincias
            if self.provincias is None:
                self.provincias = self.provincias_Dal



            self.informacionVehiculo = self.__buildTable(self.formatosSucerp.tablaInformacionVehiculo())

            # Tablas de referencias
            self.informacionVehiculo._referenced_by_list = [
                self.tipoRegistro, self.tipoSubRegistro, self.tipoOrigen, self.provincias
            ]


        return self.informacionVehiculo

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TMPINFORMACIONVEHICULO
    #     FOR SYSTEM NAME ------------------------
    @property
    def tmpInformacionVehiculo_Dal(self):

        if self.tmpInformacionVehiculo is None:

            # Tabla tipo de Registro
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            # Tabla tipo de Sub Registros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Tabla tipo de Origen
            if self.tipoOrigen is None:
                self.tipoOrigen = self.tipoOrigen_Dal

            # Tabla provincias
            if self.provincias is None:
                self.provincias = self.provincias_Dal



            self.tmpInformacionVehiculo = self.__buildTable(self.formatosSucerp.tablaTmpInformacionVehiculo())



        return self.tmpInformacionVehiculo



    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----INFORMACIONVEHICULOTITULAR
    #     FOR SYSTEM NAME ------------------------
    @property
    def informacionVehiculoTitular_Dal(self):

        if self.informacionVehiculoTitular is None:

            # Tabla tipo de Cuerpo
            if self.tipoCuerpo is None:
                self.tipoCuerpo = self.tipoCuerpo_Dal

            # Tabla tipo de Sub Registros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Tabla tipo de Documento
            if self.tipoDocumento is None:
                self.tipoDocumento = self.tipoDocumento_Dal

            # Tabla de provincias
            if self.provincias is None:
                self.provincias = self.provincias_Dal

            # Tabla de informacion de Vehiculo
            if self.informacionVehiculo is None:
                self.informacionVehiculo = self.informacionVehiculo_Dal

            self.informacionVehiculoTitular = self.__buildTable(self.formatosSucerp.tablaInformacionVehiculoTitular())

            # Tablas de referencias
            self.informacionVehiculoTitular._referenced_by_list = [
                self.tipoCuerpo, self.tipoSubRegistro, self.tipoDocumento, self.provincias,
                self.informacionVehiculo
            ]

        return self.informacionVehiculoTitular


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TMPINFORMACIONVEHICULOTITULAR
    #     FOR SYSTEM NAME ------------------------
    @property
    def tmpInformacionVehiculoTitular_Dal(self):

        if self.tmpInformacionVehiculoTitular is None:

            # Tabla tipo de Cuerpo
            if self.tipoCuerpo is None:
                self.tipoCuerpo = self.tipoCuerpo_Dal

            # Tabla tipo de Sub Registros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Tabla tipo de Documento
            if self.tipoDocumento is None:
                self.tipoDocumento = self.tipoDocumento_Dal

            # Tabla de provincias
            if self.provincias is None:
                self.provincias = self.provincias_Dal

            # Tabla de informacion de Vehiculo
            if self.tmpInformacionVehiculo is None:
                self.tmpInformacionVehiculo = self.tmpInformacionVehiculo_Dal

            self.tmpInformacionVehiculoTitular = self.__buildTable(self.formatosSucerp.tablaTmpInformacionVehiculoTitular())


        return self.tmpInformacionVehiculoTitular



    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----INFORMACIORADICACION
    #     FOR SYSTEM NAME ------------------------
    @property
    def informacionRadicacion_Dal(self):

        if self.informacionRadicacion is None:

            # Tabla tipo de Registros
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            # Tabla tipo de Esatdos
            if self.estado is None:
                self.estado = self.estado_Dal

            self.informacionRadicacion = self.__buildTable(self.formatosSucerp.tablaInformacionRadicacion())

            # Tablas de referencias
            self.informacionRadicacion._referenced_by_list = [
                self.tipoRegistro, self.estado
            ]

        return self.informacionRadicacion

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----ANULACIONTRAMITESSELLOSDETALLE
    #     FOR SYSTEM NAME ------------------------
    @property
    def anulacionTramitesSellosDetalle_Dal(self):

        if self.anulacionTramitesSellosDetalle is None:

            # Tabla tipo de Registros
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            # Tabla tipo de SubRegistros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Tabla tipo de Cuota
            if self.tipoCuota is None:
                self.tipoCuota = self.tipoCuota_Dal

            self.anulacionTramitesSellosDetalle = self.__buildTable(
                self.formatosSucerp.tablaAnulacionTramitesSellosDetalle())

            # Tablas de referencias
            self.anulacionTramitesSellosDetalle._referenced_by_list = [
                self.tipoRegistro, self.tipoSubRegistro, self.tipoCuota
            ]

        return self.anulacionTramitesSellosDetalle

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TRAMITESGENERALES
    #     FOR SYSTEM NAME ------------------------
    @property
    def tramitesGenerales_Dal(self):

        if self.tramitesGenerales is None:

            # Tabla tipo de Registros
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            # Tabla tipo de SubRegistros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Tabla tipo de Origen
            if self.tipoOrigen is None:
                self.tipoOrigen = self.tipoOrigen_Dal

            # Tabla tipo de Documentos
            if self.tipoDocumento is None:
                self.tipoDocumento = self.tipoDocumento_Dal

            # Tabla tramitesgeneralestitular
            if self.tramitesGeneralesTitular is None:
                self.tramitesGeneralesTitular = self.tramitesGeneralesTitular_Dal



            self.tramitesGenerales = self.__buildTable(
                self.formatosSucerp.tablaTramitesGenerales())

            # Tablas de referencias
            self.tramitesGenerales._referenced_by_list = [
                self.tipoRegistro, self.tipoSubRegistro, self.tipoOrigen, self.tipoDocumento,
                self.tramitesGeneralesTitular
            ]

        return self.tramitesGenerales

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----TRAMITESGENERALESTITULARES
    #     FOR SYSTEM NAME ------------------------
    @property
    def tramitesGeneralesTitular_Dal(self):

        if self.tramitesGeneralesTitular is None:

            # Tabla tipo de Registros
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            # Tabla tipo de SubRegistros
            if self.tipoSubRegistro is None:
                self.tipoSubRegistro = self.tipoSubRegistro_Dal

            # Tabla tipo de Titular
            if self.tipoTitular is None:
                self.tipoTitular = self.tipoTitular_Dal

            # Tabla tipo de Documento
            if self.tipoDocumento is None:
                self.tipoDocumento = self.tipoDocumento_Dal

            # Tabla de provincias
            if self.provincias is None:
                self.provincias = self.provincias_Dal

            self.tramitesGeneralesTitular = self.__buildTable(
                self.formatosSucerp.tablaTramitesGeneralesTitulares())

            # Tablas de referencias
            self.tramitesGeneralesTitular._referenced_by_list = [
                self.tipoRegistro, self.tipoSubRegistro, self.tipoTitular, self.tipoDocumento,
                self.provincias
            ]

        return self.tramitesGeneralesTitular

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----PIE
    #     FOR SYSTEM NAME ------------------------
    @property
    def pie_Dal(self):

        if self.pie is None:

            # Tabla tipo de Registros
            if self.tipoRegistro is None:
                self.tipoRegistro = self.tipoRegistro_Dal

            self.pie = self.__buildTable(self.formatosSucerp.tablaPie())

            # Tablas de referencias
            self.pie._referenced_by_list = [
                self.tipoRegistro
            ]

        return self.pie

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----APIAUMOSO
    #     FOR SYSTEM NAME ------------------------
    @property
    def apiAumoso_Dal(self):

        if self.apiAumoso is None:

            # Tabla api Token
            if self.apiToken is None:
                self.apiToken = self.apiToken_Dal

            self.apiAumoso = self.__buildTable(self.formatosSucerp.tablaApiAumoso())

            # Tablas de referencias
            self.apiToken._referenced_by_list = [ self.apiToken ]


        return self.apiAumoso

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.MSGNIVELGRAVEDAD
    #     FOR SYSTEM NAME MSGNI00001------------------------
    @property
    def msgNivelGravedad_Dal(self):
        if self.__msgNivelGravedad is None:
            try:
                self.__msgNivelGravedad = self.db.define_table(
                    'MSGNIVELGRAVEDAD',
                    Field('NIVELGRAVEDADID', type='id', label='Id'),
                    Field('NIVELGRAVEDADDESCRIPCION', type='string', length=50, required=True, label='Descripcion'),
                    Field('MSGNIVELGRAVEDADALERTA', type='string', length=50, required=True, label='Ayuda Mensaje'),
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__msgNivelGravedad

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.MENSAJESERROR
    #     FOR SYSTEM NAME MENSA00001------------------------
    @property
    def mensajeError_Dal(self):
        if self.__mensajesError is None:
            try:
                self.__mensajesError = self.db.define_table(
                    'MENSAJESERROR',
                    Field('MSGCODE', type='string', length=7, required=True, label='Mensaje Codigo'),
                    Field('MSGDESCRIPCION', type='string', length=150, required=True, label='Descripcion'),
                    Field('MSGHELP', type='string', length=1024, required=True, label='Ayuda Mensaje'),
                    Field('NIVELGRAVEDADID', 'reference MSGNIVELGRAVEDAD', label='Id', ondelete='CASCADE'),
                    primarykey=['MSGCODE'],
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__mensajesError

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.MENSAJESERRORMSGDINAMICOS
    #     FOR SYSTEM NAME MENSA00002------------------------
    @property
    def mensajesErrorMsgdDinamicos_Dal(self):
        if self.__mensajesErrorMsgdDinamicos is None:
            try:
                self.__mensajesErrorMsgdDinamicos = self.db.define_table(
                    'MENSAJESERRORMSGDINAMICOS',
                    Field('MSGCODE', type='integer', required=True, label='Codigo del Mensaje'),
                    Field('MSGDINAMICOID', type='integer', required=True, label='Mensaje Dinamico Id'),
                    Field('MSGDINAMICOLEN', type='integer', required=True, label='Ayuda Mensaje'),
                    primarykey=['MSGCODE', 'MSGDINAMICOID'],
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__mensajesErrorMsgdDinamicos

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # ----GXPROD.IMPRESIONPDF
    #     FOR SYSTEM NAME IMPRE00001------------------------
    @property
    def impresionPdf_Dal(self):
        if self.__impresionPdf is None:
            try:
                self.__impresionPdf = self.db.define_table(
                    'IMPRESIONPDF',
                    Field('IMPRESIONID', type='id', label='Inmpresion Id'),
                    Field('IMPRESIONPRMUNO', type='string', length=512, required=True, label='Parametro Uno'),
                    Field('IMPRESIONPRMDOS', type='string', length=512, required=True, label='Parametro Dos'),
                    Field('IMPRESIONUSUARIO', type='string', length=10, required=True, label='Usuario'),
                    Field('IMPRESIONFECHA', type='datetime', required=True, label='Fecha'),
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__impresionPdf

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def __buildTable(self, parm):

        try:

            # create  table
            valor = self.db.define_table(parm['name'], *parm['fields'], **parm['arg'])



            # if the environment allows to generate LABEL ON
            if parm['arg']['migrate']:

                if ConfigurarAplicacion.ENV_GX in ConfigurarAplicacion.ENV_LABEL_ON:

                    texto = ''

                    # we iterate through the fields of the table record
                    for x in range(0, len(valor._fields)):

                        # we build the text variable
                        texto += f'\"{valor._fields[x].lower()}\" text is \'{valor.__getattribute__(valor._fields[x]).comment}\''

                        if x != (len(valor._fields) - 1):
                            texto += ' ,'

                    # we build the sentencia variable
                    sentencia = f'LABEL ON COLUMN {valor._dalname} ({texto})'

                    # execute the sql statement
                    self.db.executesql(sentencia)


        except Exception as inst:
            print(inst)
            return inst

        self.db.commit()
        return valor


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ----CLASE DE DEFINICION DE TABLAS DE LA BIBLIOTECA MATANZA
class MatanzaAbstractDb():
    """
     EL OBJETIVO DE ESTA CLASE ES PODER DESCRIBIR LOS CAMPOS DE CADA TABLA QUE ESTAMN EL MOTOR ISERIES O MYSQL \n
     CUANDO TRABAJAMOS SIN CONEXION A LAS TABLAS DE ISERIES SE TRABAJA CON MYSQL \n

    """

    # Constructor
    def __init__(self, db):

        # Conexion
        self.db = db

        # ------------------------------------------------------
        # Tablas de Matanza
        self.__tmAut = None

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #     ARCHIVO MATANZA.TMAUT
    #     FOR SYSTEM NAME TMAUT
    @property
    def tmAut_Dal(self):
        if self.__tmAut is None:
            try:
                self.__tmAut = self.db.define_table(
                    'TMAUT',
                    Field('DORIGI', type='string', length=8, required=True, label='Dominio Original'),
                    Field('DACTUA', type='string', length=6, required=True, label='Dominio Actual'),
                    Field('FUDDJJ', type='integer', required=True, label='Fech.Ultima DDJJ'),
                    Field('FALTA', type='integer', required=True, label='Fecha Alta'),
                    Field('FTRIBA', type='integer', required=True, label='Fecha Tributación'),
                    Field('MODELO', type='integer', required=True, label='Modelo Año'),
                    Field('TIPOVE', type='string', length=2, required=True, label='Tipo de Vehículo'),
                    Field('USOVEH', type='integer', required=True, label='Uso de Vehículo'),
                    Field('PESO', type='integer', required=True, label='Peso'),
                    Field('CARGA', type='integer', required=True, label='Carga'),
                    Field('CODMAR', type='string', length=7, required=True, label='Código de Marca'),
                    Field('DESFAB', type='string', length=30, required=True, label='Descrip.Fabrica'),
                    Field('DESMOD', type='string', length=60, required=True, label='Descrip.de Modelo'),
                    Field('CODALT', type='string', length=1, required=True, label='Cód.Tipo de Alta'),
                    Field('NACION', type='integer', required=True, label='Nacionalidad'),
                    Field('CATEGO', type='integer', required=True, label='Categoria'),
                    Field('INCISO', type='string', length=1, required=True, label='Inciso'),
                    Field('FEBAJA', type='integer', required=True, label='Fecha de Baja'),
                    Field('COBAJA', type='string', length=1, required=True, label='Código de Baja'),
                    Field('MARMOT', type='string', length=12, required=True, label='Marca de Motor'),
                    Field('SERMOT', type='string', length=12, required=True, label='Serie de Motor'),
                    Field('NORMOT', type='string', length=17, required=True, label='Nro. de Motor'),
                    Field('CHASIS', type='string', length=17, required=True, label='Chasis'),
                    Field('TCOMBU', type='string', length=1, required=True, label='Tipo Combustible'),
                    Field('TYDDOC', type='integer', required=True, label='Tipo de Document.'),
                    Field('NUMDOC', type='integer', required=True, label='Nro.de Documento.'),
                    Field('PROPIE', type='string', length=30, required=True, label='Propietario'),
                    Field('CPFISC', type='integer', required=True, label='Cód.Postal Fiscal'),
                    Field('LOCFIS', type='string', length=17, required=True, label='Localidad Fiscal'),
                    Field('CALFIS', type='string', length=30, required=True, label='Calle  Fiscal'),
                    Field('NROFIS', type='integer', required=True, label='Número Fiscal'),
                    Field('PISFIS', type='string', length=2, required=True, label='Fiscal'),
                    Field('DEPFIS', type='string', length=3, required=True, label='Depto  Fiscal'),
                    Field('TEINFI', type='integer', required=True, label='Tel.Internac.Fisc'),
                    Field('TEZOFI', type='integer', required=True, label='Tel.Zonal Fiscal'),
                    Field('TELFIS', type='string', length=12, required=True, label='Telefono Fiscal'),
                    Field('CUITFI', type='bigint', required=True, label='Cuit Fiscal'),
                    Field('CODPOS', type='integer', required=True, label='Código Postal'),
                    Field('LOCPOS', type='string', length=17, required=True, label='Localidad Postal'),
                    Field('CALPOS', type='string', length=30, required=True, label='Calle  Postal'),
                    Field('NROPOS', type='integer', required=True, label='Número Postal'),
                    Field('PISPOS', type='string', length=2, required=True, label='Piso   Postal'),
                    Field('DEPPOS', type='string', length=2, required=True, label='Depto  Postal'),
                    Field('DESTIN', type='string', length=30, required=True, label='Destinatario'),
                    Field('FCDOMI', type='integer', required=True, label='F.Cambio Dom.Post'),
                    Field('TEINPO', type='integer', required=True, label='Tel.Internac.Post'),
                    Field('TEZOPO', type='integer', required=True, label='Tel.Zonal Postal'),
                    Field('TELPOS', type='string', length=12, required=True, label='Telefono Postal'),
                    Field('CUITPO', type='bigint', required=True, label='Cuit Postal'),
                    Field('CODMUN', type='integer', required=True, label='Código Municipal'),
                    Field('IDENTF', type='string', length=15, required=True, label='Identificador'),
                    Field('IDMUNI', type='integer', required=True, label='Identif.Municipal'),
                    Field('VALUA', type='decimal(17, 2)', required=True, label='Valucion'),
                    Field('FALT', type='integer', required=True, label='Fecha   Alta.....'),
                    Field('HALT', type='integer', required=True, label='Hora    Alta.....'),
                    Field('UALT', type='string', length=10, required=True, label='Usuario Alta.....'),
                    Field('FBAJ', type='integer', required=True, label='Fecha   Baja.....'),
                    Field('HBAJ', type='integer', required=True, label='Hora    Baja.....'),
                    Field('UBAJ', type='string', length=10, required=True, label='Usuario Baja.....'),
                    Field('FMOD', type='integer', required=True, label='Fecha   Modif....'),
                    Field('HMOD', type='integer', required=True, label='Hora    Modif....'),
                    Field('UMOD', type='string', length=10, required=True, label='Usuario Modif....'),
                    Field('FBAJAF', type='integer', required=True, label='Fec. Baj. Fiscal'),
                    Field('FEREVA', type='integer', required=True, label='Fecha Revaluo'),
                    Field('MNECOD', type='integer', required=True, label='Código No Emitir.'),
                    Field('CALCOD', type='integer', required=True, label='Codigo de Calle'),
                    Field('CCLCZO', type='integer', required=True, label='Zona'),
                    Field('TIPDAT', type='string', length=2, required=True, label='AUTO/MOTO'),
                    Field('MCILIN', type='integer', required=True, label='Cilindrada'),
                    primarykey=['IDENTF'],
                    migrate=False
                )
            except Exception as inst:
                print(inst)

        return self.__tmAut
