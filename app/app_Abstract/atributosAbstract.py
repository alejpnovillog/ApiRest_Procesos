# -------Lista de lisbrerias y Modulos
try:
    from pydal import  Field
    from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Atributos del Esquema Matanza
class AtributosMatanza():

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Constructor
    def __init__(self):
        pass

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tabla Maut
    def tablaMaut(self):
        """
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

        """

        try:

            lista, primary, parm = list(), list(), dict()

            # fields list
            lista = [
                Field('DORIGI', type='string', length=8, required=True, comment='Dominio Original'),
                Field('DACTUA', type='string', length=6, required=True, comment='Dominio Actual'),
                Field('FUDDJJ', type='integer', required=True, comment='Fecha Ult DDJJ'),
                Field('FALT',   type='integer', required=True, comment='Fecha Alta'),
                Field('FTRIBA', type='integer', required=True, comment='Fecha Tributacion'),
                Field('MODELO', type='integer', required=True, comment='Año Modelo'),
                Field('TIPOVE', type='string', length=2, required=True, comment='Tipo Vehiculo'),
                Field('USOVEH', type='integer', required=True, comment='Uso Vehiculo'),
                Field('PESO',   type='integer',  required=True, comment='Peso'),
                Field('CARGA',  type='integer', required=True, comment='Carga'),
                Field('CODMAR', type='string', length=7, required=True, comment='Codigo Marca'),
                Field('DESFAB', type='string', length=30, required=True, comment='Descr. Fabrica'),
                Field('DESMOD', type='string', length=60, required=True, comment='Descr. Modelo'),
                Field('CODALT', type='string', length=1, required=True, comment='Cod Tipo Alta'),
                Field('NACION', type='integer', required=True, comment='Nacionalidad'),
                Field('CATEGO', type='integer', required=True, comment='Categoria'),
                Field('INCISO', type='string', length=1, required=True, comment='Inicio'),
                Field('FBAJ',   type='integer', required=True, comment='Fecha Baja'),
                Field('COBAJA', type='string', length=1, required=True, comment='Cod Baja'),
                Field('MARMOT', type='string', length=12, required=True, comment='Marca Motor'),
                Field('SERMOT', type='string', length=12, required=True, comment='Serie Motor'),
                Field('NORMOT', type='string', length=17, required=True, comment='Numero Motor'),
                Field('CHASIS', type='string', length=17, required=True, comment='Nro Chasis'),
                Field('TCOMBU', type='string', length=1, required=True, comment='Tipo Combustible'),
                Field('TYDDOC', type='integer', required=True, comment='Tipo Documento'),
                Field('NUMDOC', type='integer', required=True, comment='Nro Documento'),
                Field('PROPIE', type='string', length=30, required=True, comment='Propietario'),
                Field('CPFISC', type='integer', required=True, comment='Cod Postal Fiscal'),
                Field('LOCFIS', type='string', length=17, required=True, comment='Localidad Fiscal'),
                Field('CALFIS', type='string', length=30, required=True, comment='Calle Fiscal'),
                Field('NROFIS', type='integer', required=True, comment='Nro Fiscal'),
                Field('PISFIS', type='string', length=2, required=True, comment='Piso Fiscal'),
                Field('DEPFIS', type='string', length=3, required=True, comment='Depto Fiscal'),
                Field('TEINFI', type='integer', required=True, comment='Tel Internacional Fiscal'),
                Field('TEZOFI', type='integer', required=True, comment='Tel Zona Fiscal'),
                Field('TELFIS', type='string', length=12,   required=True, comment='Telefono Fiscal'),
                Field('CUITFI', type='bigint', required=True, comment='Cuit Fiscal'),
                Field('CODPOS', type='integer', required=True, comment='Codigo Postal'),
                Field('LOCPOS', type='string', length=17, required=True, comment='Localidad Postal'),
                Field('CALPOS', type='string', length=30, required=True, comment='Calle Postal'),
                Field('NROPOS', type='integer', required=True, comment='Nro Postal'),
                Field('PISPOS', type='string', length=2, required=True, comment='Piso Postal'),
                Field('DEPPOS', type='string', length=2, required=True, comment='Depto Postal'),
                Field('DESTIN', type='string', length=30, required=True, comment='Destinatario'),
                Field('FCDOMI', type='integer', required=True, comment='Fecha Camb Domicilio Postal'),
                Field('TEINPO', type='integer', required=True, comment='Tel Internacional Postal'),
                Field('TEZOPO', type='integer', required=True, comment='Tel Zona Postal'),
                Field('TELPOS', type='string', length=12,   required=True, comment='Telefono Fostal'),
                Field('CUITPO', type='bigint', required=True, comment='Cuit Postal'),
                Field('CODMUN', type='integer', required=True, comment='Cod Municipal'),
                Field('IDENTF', type='string', length=15,   required=True, comment='Identificador'),
                Field('IDMUNI', type='integer', required=True, comment='Id Municipal'),
                Field('VALUA', type='decimal(17, 2)', required=True, comment='Valuacion'),
                Field('FALT',   type='integer', required=True, comment='Fecha Alta'),
                Field('HALT',   type='integer', required=True, comment='Hora Alta'),
                Field('UALT',   type='string', length=10,   required=True, comment='Usuario Alta'),
                Field('FBAJ',   type='integer', required=True, comment='Fecha Baja'),
                Field('HBAJ',   type='integer', required=True, comment='Hora Baja'),
                Field('UBAJ',   type='string', length=10,   required=True, comment='Usuario Baja'),
                Field('FMOD',   type='integer', required=True, comment='Fecha Modificacion'),
                Field('HMOD',   type='integer', required=True, comment='Hora Modificacion'),
                Field('UMOD',   type='string', length=10,   required=True, comment='Usuario Modificacion'),
                Field('FBAJAF', type='integer', required=True, comment='Fecha Baja Fiscal'),
                Field('FEREVA', type='integer', required=True, comment='Fecha Revaluo'),
                Field('MNECOD', type='integer', required=True, comment='Cod No Emitir'),
                Field('CALCOD', type='integer', required=True, comment='Cod Calle'),
                Field('CCLCZO', type='integer', required=True, comment='Zona'),
                Field('TIPDAT', type='string', length=2, required=True, comment='Auto Moto'),
                Field('MCILIN', type='integer', required=True, comment='Cilindrada')
                ]

            # Primary Key list
            primary = [
                'IDENTF'
            ]

            # table construction parameters
            parm = {
                'name': 'TMAUT',
                'fields': tuple(lista),
                'arg': {'primarykey': primary, 'migrate': False},
                'sqlfldtexto': True
            }

            return parm

        except Exception as e:
            print(f'Error - AtributosMatanza tablaMaut {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class AtributosGx():

    def __init__(self):
        pass


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tabla de Impresion Pdf
    def tablaImpresionPdf(self):
            """
            PDF PRINT TABLE DEFINITION \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n
            """
            try:

                # fields list
                lista = [
                    Field('IMPRESIONID', type='id', comment='Id'),
                    Field('IMPRESIONPRMUNO', type='string', length=512, required=True, comment='Param Impresion Uno'),
                    Field('IMPRESIONPRMDOS', type='string', length=512, required=True, comment='Param Impresion Dos'),
                    Field('IMPRESIONUSUARIO', type='string', length=10, required=True, comment='Impresion Usuarios'),
                    Field('IMPRESIONFECHA', type='datetime', required=True, comment='Fecha Impresion')
                    ]

                # table construction parameters
                parm = {
                     'name': 'IMPRESIONPDF',
                     'fields': tuple(lista),
                     'arg': {'migrate': False},
                     'sqlfldtexto': True
                 }

                return parm

            except Exception as e:
                print(f'Error - tablaImpresionPdf {e}')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tabla de Mensajes Error Msg Dinamicos
    def tablaMensajesErrorMsgDinamicos(self):
        """
        DYNAMIC ERROR MESSAGE TABLE DEFINITION \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n
        """
        try:

            # fields list
            lista = [
                Field('MSGCODE', type='string', length=7, required=True, comment='Cod Mensaje'),
                Field('MSGDINAMICOID', type='integer', required=True, comment='Id FK Msg Dinamico'),
                Field('MSGDINAMICOLEN', type='integer', required=True, comment='Long Msg Dinamico')
                ]

            # Primary Key list
            primary = [
                Field('MSGCODE', type='string', length=7, required=True, comment='Cod Mensaje'),
                Field('MSGDINAMICOID', type='integer', required=True, comment='Id FK Msg Dinamico')
            ]

            # table construction parameters
            parm = {
                 'name': 'MENSAJESERRORMSGDINAMICOS',
                 'fields': tuple(lista),
                 'arg': {'primarykey': primary, 'migrate': False},
                 'sqlfldtexto': True
             }

            return parm

        except Exception as e:
            print(f'Error - tablaMensajesErrorMsgDinamicos {e}')

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tabla de Mensajes Error
    def tablaMensajesError(self):
        """
        DEFINITION OF THE ERROR MESSAGE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n
        """
        try:

            # fields list
            lista = [
                Field('MSGCODE', type='string', length=7,    required=True, comment='Cod Mensaje'),
                Field('MSGDESCRIPCION', type='string', length=150,  required=True, comment='Descr Mensaje'),
                Field('MSGHELP', type='string', length=1024, required=True, comment='Mensaje Ayuda'),
                Field('NIVELGRAVEDADID', type='reference MSGNIVELGRAVEDAD', ondelete='CASCADE', comment='Id FK Nivel Gravedad')
                ]

            # Primary Key list
            primary = [
                Field('MSGCODE', type='string', length=7, required=True, comment='Cod Mensaje')
            ]

            # table construction parameters
            parm = {
                 'name': 'MENSAJESERROR',
                 'fields': tuple(lista),
                 'arg': {'primarykey': primary, 'migrate': False},
                 'sqlfldtexto': True
             }

            return parm

        except Exception as e:
            print(f'Error - tablaMensajesError {e}')


    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Tabla de Nivel de Gravedad
    def tablaNivelGravedad(self):

        try:

            # fields list
            lista = [
                Field('NIVELGRAVEDADID',  type='id', comment='Id'),
                Field('NIVELGRAVEDADDESCRIPCION', type='string', length=50,   required=True, comment='Descr Nivel Gravedad'),
                Field('MSGNIVELGRAVEDADALERTA',   type='string', length=50,   required=True, comment='Alerta Nivel Gravedad')
                ]

            # table construction parameters
            parm = {
                 'name': 'MSGNIVELGRAVEDAD',
                 'fields': tuple(lista),
                 'arg': {'migrate': False},
                 'sqlfldtexto': True
             }

            return parm

        except Exception as e:
            print(f'Error - tablaNivelGravedad {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class AtributosSucerp():

     def __init__(self):
         pass


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Registro para la ultima version de Recepcion de Datos
     def tablaTipoRegistro(self):

        """
             DEFINITION OF THE RECORD TYPE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n
        """
        try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('tiporegistroid', type='id', required=True, comment='Id'),
                 Field('tiporegistro', unique=True, type='string', length=2, required=True, comment='Tipo Registro'),
                 Field('desctiporegistro', unique=True, type='string', length=50, required=True, comment='Desc Tipo Registro')
            ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_REGISTRO']['migrate']

             # table construction parameters
             parm = {
                 'name' :  'TIPOREGISTRO',
                 'fields' :  tuple(lista),
                 'arg' :  {'migrate': migrate},
                 'sqlfldtexto' : True
            }

             return parm

        except Exception as e:
            print(f'Error - tablaTipoRegistro {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Sub Registro
     def tablaTipoSubRegistro(self):
         """
         DEFINITION OF THE SUBREGISTRY TYPE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('tiposubregistroid', type='id', required=True, comment='Id'),
                 Field('tiposubregistro', unique=True, type='string', length=1, required=True, comment='Tipo Sub Registro'),
                 Field('desctiposubregistro', unique=True, type='string', length=50, required=True, comment='Descr Tipo Sub Registro')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_SUB_REGISTRO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOSUBREGISTRO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoSubRegistro {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Cuerpo
     def tablaTipoCuerpo(self):
         """
         BODY TYPE TABLE DEFINITION\n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('tipocuerpoid', type='id', required=True, comment='Id'),
                 Field('tipocuerpo', unique=True,  type='string', length=2,    required=True, comment='Tipo Cuerpo'),
                 Field('desctipocuerpo', unique=True, type='string', length=50, required=True, comment='Desc Cuerpo')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_CUERPO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOCUERPO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoCuerpo {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Titular
     def tablaTipoTitular(self):
         """
         DEFINITION OF THE HOLDER TYPE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('tipotitularid', type='id', required=True, comment='Id'),
                 Field('tipotitular', unique=True, type='string', length=1,    required=True, comment='Tipo Tirular'),
                 Field('desctipotitular', unique=True, type='string', length=50, required=True, comment='Desc Tipo Titular')
                 ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_TITULAR']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOTITULAR',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoTitular {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Origen
     def tablaTipoOrigen(self):
         """
         DEFINITION OF THE TYPE OF ORIGIN TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('origenid', type='id', required=True, comment='Id'),
                 Field('tipoorigen', unique=True, type='string', length=1, required=True, comment='Origen'),
                 Field('descorigen', unique=True, type='string', length=50, required=True, comment='Desc Origen')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_ORIGEN']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOORIGEN',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoOrigen {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Movimiento
     def tablaTipoMovimiento(self):
         """
         DEFINITION OF THE MOVEMENT TYPE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('codigotipomovimientoid', type='id', required=True, comment='Id'),
                 Field('codigotipomovimiento', unique=True,  type='integer', required=True, comment='Codigo Tipo Movimiento'),
                 Field('desctipomovimiento', unique=True, type='string', length=50, required=True, comment='Desc Tipo Movimiento')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_MOVIMIENTO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOMOVIMIENTO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoMovimiento {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Forma de Pago
     def tablaTipoPago(self):
         """
         DEFINITION OF THE PAYMENT TYPE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('codigoformapagoid', type='id', required=True, comment='Id'),
                Field('codigoformapago', unique=True, type='integer', required=True, comment='Codigo Forma Pago'),
                Field('descrtipopago', unique=True, type='string', length=50, required=True, comment='Desc Tipo Pago')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_PAGO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOPAGO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm


         except Exception as e:
                print(f'Error - tablaTipoPago {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Moneda
     def tablaTipoMoneda(self):

         """
         DEFINITION OF THE CURRENCY TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('codigomonedaid', type='id', required=True, comment='Id'),
                Field('codigomoneda', unique=True, type='integer', required=True, comment='Codigo Moneda'),
                Field('desctipomoneda', unique=True, type='string', length=50, required=True, comment='Desc Tipo Moneda')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_MONEDA']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOMONEDA',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoMoneda {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla Tipo de Documento
     def tablaTipoDocumento(self):

         """
         DEFINITION OF THE DOCUMENT TYPE TABLE\n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # Lista de campos
             lista = [
                Field('tipodocumentoid', type='id', required=True, comment='Id'),
                Field('tipodocumento', unique=True, type='integer', required=True, comment='Tipo Documento'),
                Field('desctipodocumento', unique=True, type='string', length=50, required=True, comment='Desc Tipo Documento')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_DOCUMENTO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPODOCUMENTO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoDocumento {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Provincias
     def tablaProvincias(self):

         """
         DEFINITION OF THE TABLE OF PROVINCES \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('provinciaid', type='id', required=True, comment='Id'),
                Field('provincia', unique=True, type='integer', required=True, comment='Provincia'),
                Field('descprovincia', unique=True, type='string', length=50, required=True, comment='Desc Provincia')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_PROVINCIA']['migrate']

             # table construction parameters
             parm = {
                 'name': 'PROVINCIAS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaProvincias {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Estado
     def tablaEstado(self):

         """
         DEFINITION OF THE STATE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fileds list
             lista = [
                 Field('estadoid', type='id', required=True, comment='Id'),
                 Field('estado', unique=True,      type='string', length=1,    required=True, comment='Estado'),
                 Field('descestado', unique=True, type='string', length=50, required=True, comment='Desc Estado')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ESTADO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOESTADO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaEstado {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Tipo de Cuota
     def tablaTipoCuota(self):

         """
         DEFINITION OF THE FEE TYPE TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 Field('tipocuotaid', type='id', required=True, comment='Id'),
                 Field('tipocuota', unique=True, type='integer', required=True, comment='Tipo Cuota'),
                 Field('desctipocuota', unique=True,  type='string', length=50, required=True, comment='Desc Tipo Cuota')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_CUOTA']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TIPOCUOTA',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaTipoCuota {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Encabezado de la ultima version de la Recepción de Datos de Sucerp
     def tablaEncabezado(self):

         """
         DEFINITION OF THE HEADER TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                # 
                # Id de la tabla 
                Field('encabezadoid', type='id', required=True, comment='Id'),
                # 
                # Constante “E0”
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                # 
                # Es la versión del protocolo. Por Ejemplo 01.40
                Field('versionprotocolo', type='string', length=5,    required=True, comment='Version Protocolo'),
                # 
                # Es el número de revisión. Por Ejemplo v01.40 r01.00
                Field('revisionprotocolo', type='string', length=5,    required=True, comment='Revision Protocolo'),
                # 
                # Código del organismo Municipal o Provincial que realiza la transferencia
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                # 
                # Número de envío (correlativo)
                Field('numeroenvio', type='bigint', required=True, comment='Nro Envio'),
                # CAMPO OPCIONAL
                # Fecha y hora de la producción del archivo de interacción. Formato aaaa-mm-dd hh:mm:ss
                Field('fechahora', type='datetime', required=True, comment='Fecha Hora'),
                #
                # Fecha time stamp de incorporación del registro
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ENCABEZADO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'ENCABEZADO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
                print(f'Error - tablaEncabezado {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Alta Impositiva de la ultima  version de Recepción de Datos de Sucerp
     def tablaAltaImpositiva(self):

         """
         DEFINITION OF THE HIGH TAX TABLE \n
             WE RETURN: \n
                TABLE NAME \n
                STRUCTURE FIELDS \n
                CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                # 
                # Id de la tabla 
                Field('altataxid', type='id', required=True, comment='Id'),
                #
                # Id de la tabla TIPO_REGISTRO
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                #
                # Id de la tabla TIPO_SUBREGISTRO
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                #
                # Código del organismo Municipal o Provincial al cual corresponde la información
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                # CAMPO OPCIONAL
                # Número de trámite interno de la aplicación
                Field('numerotramite', type='bigint',  required=True, comment='Nro Tramite '),
                #
                # Código de tipo de trámite registral realizado
                Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite '),
                #
                # Descripción del tipo de trámite registral realizado
                Field('descrtipotramite', type='string', length=60, required=True, comment='Descr Tipo Tramite '),
                #
                # Código del tip    o de acción realizada por el contribuyente
                Field('codigotipoaccion', type='integer', required=True, comment='Codigo Tipo Accion'),
                #
                # Descripción del tipo de acción realizada por el contribuyente
                Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr Tipo Accion'),
                #
                # Identificador de tipo de formulario exigible para el trámite
                Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
                #
                # Número de formulario en el que se realizo el trámite
                Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
                #
                # Patente del Vehículo (Reempadronado)
                Field('dominionuevo', type='string', length=8, required=True, comment='Dominio Nuevo'),
                #
                # Patente del Vehículo (Dominio Anterior)
                Field('dominioviejo', type='string', length=8, required=True, comment='Dominio Viejo'),
                #
                # Código del vehículo según la DNRPA. MTM (Marca – Tipo – Modelo) y FMM (Fabrica – Marca – Modelo).
                Field('codigomtmfmm', type='string', length=8, required=True, comment='Codigo Sucerp'),
                #
                # Tipo de origen del vehículo (N – Nacional, I - Importado)
                Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Tipo Origen Vehiculo'),
                # CAMPO OPCIONAL
                # Categoría del vehículo
                Field('categoría', type='string', length=3, required=True, comment='Categoria'),
                #
                # Descripción de la marca del Vehículo
                Field('marca', type='string', length=60, required=True, comment='Marca'),
                #
                # Descripción del tipo de Vehículo
                Field('tipovehiculo', type='string', length=60, required=True, comment='Tipo Vehiculo'),
                #
                # Descripción del modelo del vehículo
                Field('modelo', type='string', length=100, required=True, comment='Modelo'),
                #
                # Año/Modelo del vehículo
                Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                # CAMPO OPCIONAL
                # Peso del vehículo
                Field('peso', type='integer', required=True, comment='Peso'),
                # CAMPO OPCIONAL
                # Carga del Vehículo
                Field('carga', type='integer', required=True, comment='Carga'),
                # CAMPO OPCIONAL
                # Cilindrada (sólo motovehículos)
                Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
                #
                # Valuación del vehículo
                Field('valuacion', type='integer', required=True, comment='Valuacion'),
                #
                # Código de tipo de uso del vehículo
                Field('codigotipouso', type='string', length=2, required=True, comment='Codigo Tipo Uso'),
                #
                # Descripción del tipo de uso del vehículo
                Field('descrtipouso', type='string', length=100, required=True, comment='Descr Tipo Uso'),
                #
                # Fecha de vigencia. Formato aaaa-mm-dd
                Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
                #
                # Tipo de documento del titular principal. Según tabla anexa V
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                #
                # Número de documento del titular principal
                Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                #
                # Número de CUIT o CUIL del titular principal
                Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                #
                # Nombre y Apellido o Razón Social del titular principal
                Field('apenomrazonsocial', type='string', length=150,  required=True, comment='ApeNom Razon Social'),
                #
                # Calle donde recibirá el impuesto
                Field('calle', type='string', length=40,   required=True, comment='Calle'),
                #
                # Número donde recibirá el impuesto
                Field('numero', type='string', length=10,   requiSred=True, comment='Nro Puerta'),
                # CAMPO OPCIONAL
                # Piso donde recibirá el impuesto
                Field('piso', type='string', length=10,   required=True, comment='Piso'),
                # CAMPO OPCIONAL
                # Departamento donde recibirá el impuesto
                Field('departamento', type='string', length=10,   required=True, comment='Depto'),
                # CAMPO OPCIONAL
                # Barrio donde recibirá el impuesto
                Field('barrio', type='string', length=40,   required=True, comment='Barrio'),
                #
                # Localidad donde recibirá el impuesto
                Field('localidad', type='string', length=40,   required=True, comment='Localidad'),
                #
                # Código Postal donde recibirá el impuesto
                Field('codigopostal', type='string', length=8,    required=True, comment='Codigo Postal'),
                #
                # Código de provincia donde recibirá el impuesto
                Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                #
                # Cantidad de titulares del vehículo
                Field('cantidadtitulares', type='integer', required=True, comment='Cantidad Titulares'),
                #
                # Código de Registro Seccional que realizó la transacción
                Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                #
                # Nombre del Registro Seccional
                Field('razonsocial',  type='string', length=40,   required=True, comment='Razon Social'),
                #
                # Código del Registro Seccional de origen del trámite (sólo disponible en cambios de radicación y recuperos)
                Field('registroseccionalorigen', type='integer', required=True, comment='Registro Seccion Origen'),
                # CAMPO OPCIONAL
                # Razón social del Registro Seccional origen del trámite (sólo disponible en cambios de radicación).
                Field('razonsocialregistroseccionalorigen', type='string', length=40, required=True, comment='Raz Soc Reg Seccional Origeb'),
                # CAMPO OPCIONAL
                # Razón social de la Municipalidad origen del trámite.
                Field('municipalidadorigen', type='string', length=150,  required=True, comment='Municipalidad Origen'),
                #
                # Fecha de la operación. Formato aaaa-mm-dd hh:ii:ss
                Field('fechaoperacion', type='datetime', required=True, comment='fecha Operacion'),
                # CAMPO OPCIONAL
                # Contiene los datos de cada parámetro adicional que el organismo requiera al realizar el trámite. 
                # Dispone de un máximo de 10 valores adicionales. Ver anexo V
                Field('parametrosadicionales',   type='string', length=650,  required=True, comment='Parm Adicionales'),
                # CAMPO OPCIONAL
                # Reservado para uso futuro
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                # CAMPO OPCIONAL
                # Observaciones
                Field('observaciones',  type='string', length=256,  required=True, comment='Observaciones'),
                #
                # Referencia a la Alta Impositiva Titular
                Field('altataxtitularid', type='reference ALTAIMPOSITIVATITULAR', ondelete='CASCADE', comment='Id FK Alta Impositiva Titular'),
                #
                # Fecha time stamp de incorporación del registro
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ALTAIMPOSITIVA']['migrate']

             # table construction parameters
             parm = {
                'name': 'ALTAIMPOSITIVA',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaAltaImpositiva {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Arba and Sucerp Brand Relationship Table
     def tablaRelArbaSucerpMarca(self):

         """
         DEFINITION OF THE ARBA SUCERP BRAND RELATIONSHIP TABLE\n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # field list
             lista = [
                 Field('relArbaSucerpid', type='id', required=True, comment='Id'),
                 Field('relArbaSucerpArba', type='string', length=10, required=True, comment='Arba'),
                 Field('relArbaSucerpMarca', type='string', length=60, required=True, comment='Marca'),
                 Field('relArbaSucerpModelo', type='string', length=60, required=True, comment='Modelo'),
                 Field('relArbaSucerpCodMtmFmm', type='string', length=8, required=True, comment='Sucerp'),
                 Field('relArbaSucerpInciso', type='string', length=4, required=True, comment='Inciso'),
                 Field('relArbaSucerpEstado', type='string', length=1, required=True, comment='1=Procesa, 0=A Confirmar'),
                 Field('relArbaSucerpOrigenDato', type='string', length=1, required=True, comment='Origen Dato'),
                 Field('relArbaSucerpMarcaMoto', type='string', length=60, required=True, comment='Marca Moto'),
                 Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_RELACION_ARBA_SUCERP_MARCA']['migrate']

             parm = {
                'name': 'RELACIONARBASUCERPMARCA',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }
             return parm

         except Exception as e:
             print(f'Error - tablaRelArbaSucerpMarca {e}')



     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Procesos de Importacion y Exportacion
     def tablaProcesoImportacionExportacion(self):

         """
         DEFINITION OF IMPORTEXPORT PROCESS TABLE\n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # field list
             lista = [
                 Field('procesoid', type='id', comment='Id'),
                 Field('procesocodigotabla', type='integer', required=True, comment='Proceso Codigo Tabla'),
                 Field('procesonombretabla', type='string', length=150, required=True, comment='Proceso Nombre Tabla'),
                 Field('procesotransferencia', type='string', length=1, required=True, comment='Transferencia (S, Nulo)'),
                 Field('procesofechatransferencia', type='datetime',  comment='Fecha Transferencia'),
                 Field('procesobasedatos', type='string', length=1, required=True, comment='Base Datos (S, Nulo)'),
                 Field('procesofechabasedatos', type='datetime',  comment='Fecha Base Datos'),
                 Field('procesoaccion', type='string', length=1, required=True, comment='Accion ( E, I, Nulo)'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_PROCESOIMPORTACIONEXPORTACION']['migrate']

             parm = {
                'name': 'PROCESOIMPORTACIONEXPORTACION',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }
             return parm

         except Exception as e:
             print(f'Error - tablaRelArbaSucerpMarca {e}')













     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Alta Impositiva Titular de la ultima version de la Recepción de Datos de Sucerp
     def tablaAltaImpositivaTitular(self):

         """
         DEFINITION OF THE HOLDER'S HIGH TAX TABLE \n
         WE RETURN:\n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 #
                 # Id de identificación del registro
                 Field('altataxtitularid', type='id', required=True, comment='Id'),
                 #
                 # Constante “C1 ”
                 Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id Fk Tipo Cuerpo'),
                 #
                 # Constante “T ”
                 Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id Fk Tipo Sub Registro'),
                 #
                 # Tipo de documento del titular. Según tabla anexa V
                 Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id Fk Tipo Documento'),
                 #
                 # Número de documento correspondiente al titular
                 Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                 #
                 # Número de CUIT / CUIL correspondiente al titular
                 Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                 #
                 # Nombre y Apellido o Razón Social del titular del vehículo
                 Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
                 #
                 # Porcentaje de posesión del vehiculo
                 Field('porcentajetitularidad', type='integer', required=True, comment='Porcentaje Titular'),
                 #
                 # Calle del domicilio del titular
                 Field('calle', type='string', length=40, required=True, comment='Calle'),
                 #
                 # Número de puerta del domicilio del titular
                 Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                 # CAMPO OPCIONAL
                 # Piso del departamento del domicilio del titular
                 Field('piso', type='string', length=10, required=True, comment='Piso'),
                 # CAMPO OPCIONAL
                 # Departamento del domicilio del titular
                 Field('departamento', type='string', length=10, required=True, comment='Depto'),
                 # CAMPO OPCIONAL
                 # Barrio del domicilio del titular
                 Field('barrio', type='string', length=40, required=True, comment='Barrio'),
                 #
                 # Localidad del domicilio del titular
                 Field('localidad', type='string', length=40, required=True, comment='Localidad'),
                 #
                 # Código Postal del titular
                 Field('codigopostal', type='string', length=8, required=True, comment='Cod Postal'),
                 #
                 # Provincia del Titular. Según tabla Anexo VI
                 Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id Fk Provincia'),
                 # CAMPO OPCIONAL
                 # Reservado para uso futuro
                 Field('reservado', type='string', length=256, required=True, comment='Reservado Sucerp'),
                 #
                 # Fecha de incorporación del registro
                 Field('ktimestamp', type='datetime', required=True, comment='Timestamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ALTAIMPOSITIVATITULAR']['migrate']

            # table construction parameters
             parm = {
                 'name': 'ALTAIMPOSITIVATITULAR',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaAltaImpositivaTitular {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Baja Impositiva de la ultima version de la Recepción de Datos de Sucerp
     def tablaBajaImpositiva(self):

         """
         DEFINITION OF THE TAX LOW TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

              # fields list
             lista = [
                 #
                 # Id identificador del registro
                 Field('bajataxid', type='id', required=True, comment='Id'),
                 #
                 # Constante “C2 ”
                 Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id Fk Tipo Registro'),
                 #
                 # Constante “C”
                 Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id Fk Tipo Sub Registro'),
                 #
                 # Código del organismo Municipal o Provincial al cual corresponde la información
                 Field('codigoorganismo', type='integer', required=True, comment='Cod Organismo'),
                 # CAMPO OPCIONAL
                 # Número de trámite interno de la aplicación
                 Field('numerotramite', type='bigint', required=True, comment='Nro Tramite'),
                 #
                 # Código de trámite registral realizado
                 Field('codigotipotramite', type='integer', required=True, comment='Cod Tipo Tramite'),
                 #
                 # Descripción del tipo de trámite registral realizado
                 Field('descrtipotramite', type='string', length=60, required=True, comment='Descripcion Tramite'),
                 #
                 # Código del tipo de acción realizada por el contribuyente
                 Field('codigotipoaccion', type='integer', required=True, comment='Cod Tipo Accion'),
                 #
                 # Descripción del tipo de acción realizada por el contribuyente
                 Field('descrtipoaccion', type='string', length=60, required=True, comment='Descripcion Tipo Accion'),
                 #
                 # Identificador de tipo de formulario exigible para el trámit
                 Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
                 #
                 # Número de formulario en el que se realizo el trámite
                 Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
                 #
                 # Patente del Vehículo (Reempadronado)
                 Field('dominionuevo', type='string', length=8, required=True, comment='Dominio Nuevo'),
                 #
                 # Patente del Vehículo (Dominio Anterior)
                 Field('dominioviejo', type='string', length=8, required=True, comment='Dominio Viejo'),
                 #
                 # Código del vehículo según la DNRPA. MTM (Marca – Tipo – Modelo) y FMM (Fabrica – Marca – Modelo).
                 Field('codigomtmfmm', type='string', length=8, required=True, comment='Codigo Sucerp'),
                 #
                 # Tipo de origen del vehículo (N – Nacional, I - Importado)
                 Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id Fk Tipo Origen'),
                 # CAMPO OPCIONAL
                 # Categoría del vehículo
                 Field('categoría', type='string', length=3, required=True, comment='Categoria'),
                 #
                 # Descripción de la marca del Vehículo
                 Field('marca', type='string', length=60, required=True, comment='Marca'),
                 #
                 # Descripción del tipo de Vehículo
                 Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
                 #
                 # Descripción del modelo del vehículo
                 Field('modelo',  type='string', length=100,  required=True, comment='Modelo'),
                 #
                 # Año/Modelo del Vehículo
                 Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                 # CAMPO OPCIONAL
                 # Peso del Vehículo
                 Field('peso', type='integer', required=True, comment='Peso Vehiculo'),
                 # CAMPO OPCIONAL
                 # Carga del Vehículo
                 Field('carga', type='integer', required=True, comment='Carga'),
                 # CAMPO OPCIONAL
                 # Cilindrada (sólo motovehículos)
                 Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
                 #
                 # Valuación del vehículo
                 Field('valuacion', type='integer', required=True, comment='Valuacion'),
                 #
                 # Código de tipo de uso del vehículo
                 Field('codigotipouso', type='string', length=2,    required=True, comment='Cod Tipo Uso'),
                 #
                 # Descripción del tipo de uso del vehículo
                 Field('descrtipouso', type='string', length=100,  required=True, comment='Descripcion Tipo Uso'),
                 #
                 # Fecha de vigencia. Formato aaaa-mm-dd.
                 Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
                 #
                 # Cantidad de titulares del vehículo
                 Field('cantidadtitulares', type='integer', required=True, comment='Cantidad Titulares'),
                 #
                 # Código de Registro Seccional
                 Field('codigoregistronacional', type='integer', required=True, comment='Codigo Registro  Nacional'),
                 #
                 # Nombre del registro Seccional
                 Field('razonsocial', type='string', length=40,   required=True, comment='Razon Social'),
                 # CAMPO OPCIONAL
                 # Código del Registro Seccional de destino del trámite
                 Field('registroseccionaldestino', type='integer', required=True, comment='Registro Seccional Destino'),
                 #
                 # Razón social del Registro Seccional destino del trámite (sólo disponible en cambios de radicación)
                 Field('razonsocialregistroseccionalorigen', type='string', length=40, required=True, comment='Raz. Soc. Reg. Seccional  Orig.'),
                 # CAMPO OPCIONAL
                 # Razón social de la Municipalidad destino del trámite.
                 Field('municipalidaddestino', type='string', length=150,  required=True, comment='Muni. Destino'),
                 #
                 # Fecha de la operación. Formato aaaa-mm-dd hh:mm:ss
                 Field('fechaoperacion', type='datetime', required=True, comment='Fecha Operacion'),
                 # CAMPO OPCIONAL
                 # Contiene los datos de cada parámetro adicional que el organismo requiera al realizar el trámite. 
                 # Dispone de un máximo de 10 valores adicionales. Ver anexo VII.
                 Field('parametrosadicionales',   type='string', length=650,  required=True, comment='Param. Adicionales'),
                 # CAMPO OPCIONAL
                 # Reservado para uso futuro
                 Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                 # CAMPO OPCIONAL
                 # Observaciones
                 Field('observaciones', type='string', length=256,  required=True, comment='Observaciones'),
                 #
                 # Referencia al titular de la baja impositiva
                 Field('bajataxtitularid', type='reference BAJAIMPOSITIVATITULAR', ondelete='CASCADE', comment='Id Fk Baja Impositiva Titular'),
                 #
                 # Fecha del ingreso del registro 
                 Field('ktimestamp', type='datetime', required=True, comment='Key TimeStamp'),
             ]


             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_BAJAIMPOSITIVA']['migrate']

             # table construction parameters
             parm = {
                 'name': 'BAJAIMPOSITIVA',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaBajaImpositiva {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Alta Impositiva Titular de la ultima version de la Recepción de Datos de Sucerp
     def tablaBajaImpositivaTitular(self):

         """
         DEFINITION OF THE HOLDER'S LOW TAX TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n
         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 #
                 # Id identificador del registro
                 Field('bajataxtitularid', type='id', required=True, comment='Id'),
                 #
                 # Constante “C2 ”
                 Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id Fk Tipo Cuerpo'),
                 #
                 # Constante “T ”
                 Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id Fk Tipo Sub Registro'),
                 #
                 # Tipo de documento del titular. Según tabla anexa V
                 Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id Fk Tipo Documento'),
                 #
                 # Número de documento correspondiente al titular
                 Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                 #
                 # Número de CUIT / CUIL correspondiente al titular
                 Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                 #
                 # Nombre y Apellido o Razón Social del titular del vehículo
                 Field('apellidonombre', type='string', length=150,  required=True, comment='Apellido y Nombre'),
                 #
                 # Porcentaje de posesión del vehiculo
                 Field('porcentajetitularidad', type='integer', required=True, comment='Procentaje Titular'),
                 #
                 # Calle del domicilio del titular
                 Field('calle', type='string', length=40, required=True, comment='Calle'),
                 #
                 # Número de puerta del domicilio del titular
                 Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                 #
                 # Piso del departamento del domicilio del titular
                 Field('piso', type='string', length=10, required=True, comment='Piso'),
                 #
                 # Departamento del domicilio del titular
                 Field('departamento', type='string', length=10, required=True, comment='Depto'),
                 # CAMPO OPCIONAL
                 # Barrio del domicilio del titular
                 Field('barrio', type='string', length=40, required=True, comment='Barrio'),
                 #
                 # Localidad del domicilio del titular
                 Field('localidad', type='string', length=40, required=True, comment='Localidad'),
                 #
                 # Código Postal del titular
                 Field('codigopostal', type='string', length=8,    required=True, comment='Cod Postal'),
                 #
                 # Provincia del Titular. Según tabla Anexo VI
                 Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id Fk Provincias'),
                 # CAMPO OPCIONAL
                 # Reservado para uso futuro
                 Field('reservado', type='string', length=256, required=True, comment='Reservado Sucerp'),
                 #
                 # Fecha del ingreso del registro 
                 Field('ktimestamp', type='datetime', required=True, comment='Timestamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_BAJAIMPOSITIVATITULAR']['migrate']

             # table construction parameters
             parm = {
                 'name': 'BAJAIMPOSITIVATITULAR',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaBajaImpositivaTitular {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Impuestos  de Sellos de la ultima version de la Recepción de Datos de Sucerp
     def tablaImpuestosSellos(self):

         """
         DEFINITION OF THE STAMP TAX TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 #
                 # Id identificador del registro
                 Field('taxsellosid', type='id', required=True, comment='Id'),
                 #
                 # Constante “C3 ”
                 Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                 #
                 # Constante “C”
                 Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                 #
                 # Código del organismo Municipal o Provincial al cual corresponde la información
                 Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                 #
                 # Número de trámite interno de la aplicación
                 Field('numerotramite', type='bigint', required=True, comment='Nro Tramite'),
                 #
                 # Código del tipo de acción realizada por el contribuyente
                 Field('codigotipoaccion', type='integer', required=True, comment='Cod Tipo Accion'),
                 #
                 # Descripción del tipo de acción realizada por el contribuyente
                 Field('descrtipoaccion', type='string', length=60, required=True, comment='Descr. Tipo Accion'),
                 #
                 # Identificador de tipo de formulario exigible para el trámite
                 Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
                 #
                 # Número de formulario en el que se realizo el trámite
                 Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
                 # CAMPO OPCIONAL
                 # Patente del Vehículo (Reempadronado), es opcional, 
                 # puede llegar o el dominio o el nº de recibo, nunca los dos a la vez
                 Field('dominionuevo', type='string', length=8, required=True, comment='Dominio Nuevo'),
                 # CAMPO OPCIONAL
                 # Patente del Vehículo (Dominio Anterior)
                 Field('dominioviejo', type='string', length=8, required=True, comment='Dominio Viejo' ),
                 # CAMPO OPCIONAL
                 # Nº de recibo que otorga el registro seccional, es opcional, 
                 # puede llegar o el dominio o el nº de recibo, nunca los dos a la vez
                 Field('recibo', type='string', length=15, required=True, comment='Recibo'),
                 # CAMPO OPCIONAL
                 # Código del vehículo según la DNRPA. MTM (Marca – Tipo – Modelo) 
                 # y FMM (Fabrica – Marca – Modelo).
                 Field('codigomtmfmm', type='string', length=8, required=True, comment='Codigo Sucerp'),
                 # CAMPO OPCIONAL
                 # Tipo de origen del vehículo (N – Nacional, I - Importado)
                 Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
                 # CAMPO OPCIONAL
                 # Categoría del vehículo
                 Field('categoría', type='string', length=3, required=True, comment='Categoria'),
                 # CAMPO OPCIONAL
                 # Descripción de la marca del Vehículo
                 Field('marca', type='string', length=60, required=True, comment='Marca'),
                 # CAMPO OPCIONAL
                 # Descripción del tipo de Vehículo
                 Field('tipovehiculo', type='string', length=60, required=True, comment='Tipo Vehiculo'),
                 # CAMPO OPCIONAL
                 # Descripción del modelo del vehículo 
                 Field('modelo', type='string', length=100, required=True, comment='Modelo'),
                 # CAMPO OPCIONAL
                 # Año/Modelo del Vehículo
                 Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                 # CAMPO OPCIONAL
                 # Código de tipo de uso del vehículo
                 Field('codigotipouso', type='string', length=2, required=True, comment='Codigo Tipo Uso'),
                 # CAMPO OPCIONAL
                 # Descripción del tipo de uso del vehículo
                 Field('descrtipouso', type='string', length=100, required=True, comment='Descr Tipo Uso'),
                 # CAMPO OPCIONAL
                 # Valuación del Vehículo
                 Field('valuacion', type='integer', required=True, comment='Valuacion'),
                 #
                 # Cantidad de partes
                 Field('cantidadpartes', type='integer', required=True, comment='Cantidad Partes'),
                 #
                 # Total de los montos de impuesto adicionales al contrato
                 Field('montoimpuestoadicional', type='decimal(12, 2)', required=True, comment='Monto Impuesto Adicional'),
                 #
                 # Total de los montos de punitorios cobrados
                 Field('montopunitorios', type='decimal(12, 2)', required=True, comment='Monto Punitorios'),
                 #
                 # Total de los montos percibido
                 Field('montototalcobrado', type='decimal(12, 2)', required=True, comment='Monto Total Cobrado'),
                 #
                 # Total del monto abonado fuera del RRSS, exhibido ante la presentación de un comprobante. 
                 # Puede ser el importe parcial o total del sello
                 Field('montoabonado', type='decimal(12, 2)', required=True, comment='Monto Abonado'),
                 # CAMPO OPCIONAL
                 # Según tabla Anexo III
                 Field('codigoformapagoid', type='reference TIPOPAGO', ondelete='CASCADE', comment='Id FK Cod Forma Pago'),
                 # CAMPO OPCIONAL
                 # Según tabla Anexo IV
                 Field('codigomonedaid', type='reference TIPOMONEDA', ondelete='CASCADE', comment='Id FK Cod Moneda'),
                 # CAMPO OPCIONAL
                 # Código de entidad bancaria
                 Field('codigoentidadbancaria', type='integer', required=True, comment='Codigo Entidad Bancaria'),
                 # CAMPO OPCIONAL
                 # Razón Social de la entidad bancaria
                 Field('descrentidadbancaria', type='string', length=60, required=True, comment='Descr Entidad Bancaria'),
                 # CAMPO OPCIONAL
                 # Número de cheque
                 Field('numerocheque', type='string', length=20, required=True, comment='Nro Cheque'),
                 # 
                 # S: Esta exento, N: no esta exento
                 Field('exencion', type='string', length=1, required=True, comment='Execcion'),
                 # CAMPO OPCIONAL
                 # Código de la exención
                 Field('codigoexencion', type='string', length=10, required=True, comment='Codigo Execcion'),
                 # CAMPO OPCIONAL
                 # Descripción de la exención
                 Field('descripcionexencion', type='string', length=100, required=True, comment='Descr Execcion'),
                 # CAMPO OPCIONAL
                 # Fecha de depósito. Formato aaaa-mm-dd hh:mm:ss
                 Field('fechadeposito', type='datetime', required=True, comment='fecha Deposito'),
                 #
                 #  Código de Registro Seccional
                 Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                 #
                 # Número de CUIT del encargado del Registro Seccional
                 Field('cuitregistroseccional', type='bigint', required=True, comment='Cuit Registro Seccional'),
                 #
                 # Nombre del Registro Seccional
                 Field('razonsocial', type='string', length=40, required=True, comment='Razon Social'),
                 #
                 # Fecha de la operación. Formato aaaa-mm-dd hh:mm:ss
                 Field('fechaoperacion', type='datetime', required=True, comment='fecha Operacion'),
                 # CAMPO OPCIONAL
                 # Contiene los datos de cada parámetro adicional que el organismo requiera al realizar el trámite. 
                 # Dispone de un máximo de 10 valores adicionales. Ver anexo VII.
                 Field('parametrosadicionales', type='string', length=650, required=True, comment='Parm Adicionales'),
                 # CAMPO OPCIONAL
                 # Reservado para uso futuro
                 Field('reservado', type='string', length=256, required=True, comment='Reservado'),
                 # CAMPO OPCIONAL
                 # Observaciones
                 Field('observaciones', type='string', length=256, required=True, comment='Observaciones'),
                 # CAMPO OPCIONAL
                 # Observaciones anulación
                 Field('observacionesanulacion', type='string', length=256, required=True, comment='Observaciones Anulacion'),
                 #
                 # Fecha del ingreso del registro 
                 Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp'),
             ]


             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_IMPUESTOSELLOS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'IMPUESTOSELLOS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaImpuestosSellos {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Impuestos  de Sellos Partes de la ultima version de la Recepción de Datos de Sucerp
     def tablaImpuestosSellosPartes(self):

         """
         PART STAMP TAX TABLE DEFINITION \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """

         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 #
                 # Id identificador del registro
                 Field('taxsellospartesid', type='id', required=True, comment='Id'),
                 #
                 # Constante “C3 ”
                 Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
                 #
                 # Constante “P ” 
                 Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                 #
                 # Tipo de interviniente en la operación.
                 Field('tipointerviniente', type='integer', required=True, comment='Tipo Interviniente'),
                 #
                 # Descripción del tipo de parte del impuesto
                 Field('descrtipointerviniente', type='string', length=60,   required=True, comment='Descr Tipo Interviniente'),
                 # CAMPO OPCIONAL
                 # Tipo de documento del titular. Según tabla anexa V
                 Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                 # CAMPO OPCIONAL
                 # Número de documento correspondiente al titular
                 Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                 #
                 # Número de CUIT / CUIL correspondiente al titular
                 Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                 # CAMPO OPCIONAL
                 # Nombre y Apellido o Razón Social del titular del vehículo
                 Field('apellidonombre', type='string', length=150,  required=True, comment='Apellido y Nombre'),
                 #
                 # Porcentaje de posesión del vehiculo
                 Field('porcentajetitularidad', type='integer', required=True, comment='Porcentaje Titular'),
                 # CAMPO OPCIONAL
                 # Calle del domicilio del titular
                 Field('calle', type='string', length=40,   required=True, comment='Calle'),
                 # CAMPO OPCIONAL
                 # Número de puerta del domicilio del titular
                 Field('numero', type='string', length=10,   required=True, comment='Nro Puerta'),
                 # CAMPO OPCIONAL
                 # Piso del departamento del domicilio del titular
                 Field('piso', type='string', length=10,   required=True, comment='Piso'),
                 # CAMPO OPCIONAL
                 # Departamento del domicilio del titular
                 Field('departamento', type='string', length=10, required=True, comment='Depto'),
                 # CAMPO OPCIONAL
                 # Barrio del domicilio del titular
                 Field('barrio', type='string', length=40,   required=True, comment='Barrio'),
                 # CAMPO OPCIONAL
                 # Localidad del domicilio del titular
                 Field('localidad', type='string', length=40,   required=True, comment='Localidad'),
                 # CAMPO OPCIONAL
                 # Código Postal del titular
                 Field('codigopostal', type='string', length=8,    required=True, comment='Codigo Postal'),
                 # CAMPO OPCIONAL
                 # Provincia del Titular. Según tabla Anexo VI
                 Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                 #
                 # S: Esta exento, N: no esta exento
                 Field('exencion', type='string', length=1,    required=True, comment='Execcion'),
                 # CAMPO OPCIONAL
                 # Código de la exención
                 Field('codigoexencion', type='string', length=10,   required=True, comment='Codigo Execcion'),
                 # CAMPO OPCIONAL
                 # Descripción de la exención
                 Field('descripcionexencion', type='string', length=100,  required=True, comment='Descr Execcion'),
                 # CAMPO OPCIONAL
                 # Código de trámite registral realizado
                 Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                 # CAMPO OPCIONAL
                 # Descripción del tipo de trámite registral realizado
                 Field('descrtipotramite', type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
                 # CAMPO OPCIONAL
                 # Reservado
                 Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                 #
                 # Fecha del ingreso del registro 
                 Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_IMPUESTOSELLOSPARTES']['migrate']

             # table construction parameters
             parm = {
                 'name': 'IMPUESTOSELLOSPARTES',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaImpuestosSellosPartes {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Impuestos  de Sellos Partes Tipo Tramite de la ultima version de la Recepción de Datos de Sucerp
     def tablaImpuestosSellosPartesTipoTramite(self):

         """
         DEFINITION OF THE TAX TABLE OF PARTS STAMPS BY TYPE OF PROCESS\n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n
            
            DETALLE DE SUBCAMPOS DEL CAMPO RESERVADO
            
            1-2     Exención objetiva           Char 1          Determina si tiene exención objetiva (S o N)
            3-18    Código de exención          Char 15         Código de exención
            19-20   Celebración instrumento     Char 1          Determina el lugar de celebración del instrumento (D  Dentro de la provincia, F  Fuera de la provincia).
            20-21   Dispone de factura          Char 1          Establece si dispone de factura o no (S o N).
            22-23   Inscripto en IIBB           Char 1          Establece si el vendedor se encuentra inscripto en Ingresos Brutos de la jurisdicción (S o N).
            24-36   Importe de multa            Float 12,2      Determina que monto del punitorio es la multa por el pago fuera del vencimiento.
            
            

         """

         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                #
                # Id identificador del registro
                Field('taxsellospartestipotramiteid', type='id', required=True, comment='Id'),
                #
                # Constante “C3 ”
                Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
                #
                # Constante “T ”
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                #
                # Código de trámite registral realizado
                Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                #
                # Descripción del tipo de trámite registral realizado
                Field('descrtipotramite', type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
                #
                # Monto declarado del contrato para el instrumento
                Field('montocontrato', type='decimal(12, 2)', required=True, comment='Monto Contrato'),
                #
                # Base imponible del cálculo del impuesto
                Field('baseimponible', type='decimal(12, 2)', required=True, comment='Base Imponible'),
                #
                # Monto cobrado del impuesto
                Field('montoimpuesto', type='decimal(12, 2)', required=True, comment='Monto Impuesto'),
                #
                # Importe de punitorios cobrados del impuesto
                Field('montopunitorio', type='decimal(12, 2)', required=True, comment='monto Punitorio'),
                #
                # Importe abonado fuera del RRSS para el tipo de instrumentación
                Field('montofueraregistro', type='decimal(12, 2)', required=True, comment='Monto Abonado Fuera Registro'),
                #
                # Importe adicional del trámite
                Field('montoadicional', type='decimal(12, 2)', required=True, comment='Monto Adicional'),
                #
                # Alícuota aplicada al momento del cálculo del sello para este tipo de trámite
                Field('alicuota', type='decimal(5, 2)', required=True, comment='Alicuota'),
                #
                # Porcentaje del contrato del instrumento
                Field('porcentajecontrato', type='decimal(5, 2)', required=True, comment='Porcentaje Contrato'),
                #
                # Porcentaje del impuesto, será menor a 100 en caso de existir exenciones.
                Field('porcentajeimpuesto', type='decimal(5, 2)', required=True, comment='Porcentaje Impuesto'),
                #
                # Fecha de la instrumentación contrato sobre el cual se cobra el impuesto. Formato aaaa-mmdd hh:mm:ss
                Field('fechacontrato', type='datetime', required=True, comment='Fecha Contrato'),
                # CAMPO OPCIONAL
                # Reservado (**)
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                #
                # Fecha del ingreso del registro 
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]


             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_IMPUESTOSELLOSPARTESTIPOTRAMITE']['migrate']

             # table construction parameters
             parm = {
                 'name': 'IMPUESTOSELLOSPARTESTIPOTRAMITE',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaImpuestosSellosPartesTipoTramite {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Impuesto  Automotor de la ultima version de la Recepción de Datos de Sucerp
     def tablaImpuestoAutomotor(self):

         """
         DEFINITION OF THE AUTOMOTIVE TAX TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                #
                # Id identificador del registro
                Field('taxautomotorid', type='id', required=True, comment='Id'),
                #
                # Constante “C4 ”
                Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
                #
                # Código del organismo Municipal o Provincial al cual corresponde la información
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                # CAMPO OPCIONAL
                # Número de trámite interno de la aplicación
                Field('numerotramite', type='bigint', required=True, comment='Nro Tramite'),
                #
                # Según tabla Anexo I
                Field('codigotipomovimientoid', type='reference TIPOMOVIMIENTO', ondelete='CASCADE', comment='Id FK Cod Tipo Movimiento'),
                #
                # Según tabla Anexo II o los tipos que se convengan al momento de salir operativos.
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                #
                # Patente del Vehículo
                Field('dominionuevo', type='string', length=8, required=True, comment='Dominio Nuevo'),
                #
                # Patente del Vehículo
                Field('dominioviejo', type='string', length=8, required=True, comment='Dominio Viejo'),
                #
                # Año Fiscal               
                Field('yyyy', type='integer', required=True, comment='Año'),
                #
                # Número de Cuota
                Field('numerocuota', type='integer', required=True, comment='Nro Cuota'),
                #
                # Fecha hasta la cual es válido el importe bonificado
                Field('fechabonificacion', type='date', required=True, comment='Fecha Bonificacion'),
                #
                # Fecha a partir de la cual se comienza a realizar el cálculo de punitorios
                Field('fechavencimiento', type='date', required=True, comment='Fecha Vencimiento'),
                #
                # Determina si la deuda vence o no se tiene en cuenta la fecha de vencimiento (S=Vence  N=No vence)
                Field('flagvencimiento', type='string', length=1, required=True, comment='Flag Vencimiento'),
                #
                # Importe bonificado               
                Field('importebonificado', type='decimal(10, 2)', required=True, comment='Importe Bonificado'),
                #
                # Importe de la deuda
                Field('importecomun', type='decimal(10, 2)', required=True, comment='Importe Comun'),
                #
                # Fecha de proceso de la deuda en el Municipio y/o Provincia. Formato aaaa-mm-dd hh:mm:ss               
                Field('fechaproceso', type='datetime', required=True, comment='Fecha Proceso'),
                # CAMPO OPCIONAL
                # Importe total percibido               
                Field('importetotal', type='decimal(10, 2)',      required=True, comment='Importe Total'),
                # CAMPO OPCIONAL
                # Importe percibido en concepto de impuesto               
                Field('importeimpuesto', type='decimal(10, 2)', required=True, comment='Importe Impuesto'),
                # CAMPO OPCIONAL
                # Importe percibido de punitorios               
                Field('importepunitorio', type='decimal(10, 2)', required=True, comment='Importe Punitorio'),
                # CAMPO OPCIONAL
                # Según tabla Anexo III               
                Field('codigoformapagoid', type='reference TIPOPAGO', ondelete='CASCADE', comment='Id FK Cod Forma Pago'),
                # CAMPO OPCIONAL
                # Según tabla Anexo IV               
                Field('codigomonedaid', type='reference TIPOMONEDA', ondelete='CASCADE', comment='Id FK Cod Moneda'),
                # CAMPO OPCIONAL
                # Código de entidad bancaria               
                Field('codigoentidadbancaria', type='integer', required=True, comment='Codigo Entidad Bancaria'),
                # CAMPO OPCIONAL
                # Razón Social de la entidad bancaria
                Field('descrentidadbancaria',     type='string', length=60,   required=True, comment='Descr Entidad Bancaria'),
                # CAMPO OPCIONAL
                # Número de cheque
                Field('numerocheque',             type='string', length=20,   required=True, comment='Nro Cheque'),
                # CAMPO OPCIONAL
                # Fecha de cobro. Formato aaaa-mm-dd hh:mm:ss
                Field('fechacobro', type='datetime', required=True, comment='Fecha Cobro'),
                # CAMPO OPCIONAL
                # Fecha de transferencia estimada. Formato aaaamm-dd hh:mm:s
                Field('fechatransferencia', type='datetime', required=True, comment='Fecha Transferencia'),
                # CAMPO OPCIONAL
                # Código del Registro Seccional
                Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                # CAMPO OPCIONAL
                # Nombre del Registro Seccional
                Field('descrregistroseccional', type='string', length=40,   required=True, comment='Descr Registro Seccional'),
                # CAMPO OPCIONAL
                # Reservado para uso del organismo. Recuerde que no podrá contener ni caracteres pipe “|” ni el separador que utilice para el protocolo.
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                # CAMPO OPCIONAL
                # Observaciones
                Field('observaciones',  type='string', length=256,  required=True, comment='Observaciones'),
                #
                # Fecha del ingreso del registro 
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_IMPUESTOAUTOMOTOR']['migrate']

             # table construction parameters
             parm = {
                 'name': 'IMPUESTOAUTOMOTOR',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm
         except Exception as e:
             print(f'Error - tablaImpuestoAutomotor {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Informacion de Vehiculo de la ultima version de la Recepción de Datos de Sucerp
     def tablaInformacionVehiculo(self):

         """
          DEFINITION OF THE VEHICLE INFORMATION TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

          """

         try:
             lista, primary, parm = list(), list(), dict()


             # fields list
             lista = [
                #
                # Id identificador del registro
                Field('infvehiculoid', type='id', required=True, comment='Id'),
                #
                # Constante “C5 ”
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                #
                # Constante “C”
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                #
                # Código del organismo Municipal o Provincial al cual corresponde la información
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                #
                # Patente del Vehículo (Reempadronado)
                Field('dominionuevo', type='string', length=8,    required=True, comment='Dominio Nuevo'),
                #
                # Patente del Vehículo (Dominio Anterior)
                Field('dominioviejo', type='string', length=8,    required=True, comment='Dominio Viejo'),
                #
                # Código del vehículo según la DNRPA. MTM (Marca – Tipo – Modelo) y FMM (Fabrica – Marca – Modelo).
                Field('codigomtmfmm', type='string', length=8, required=True, comment='Codigo Sucerp'),
                #
                # Tipo de origen del vehículo (N – Nacional, I – Importado).
                Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
                # CAMPO OPCIONAL
                # Categoría del vehículo
                Field('categoría', type='string', length=3,    required=True, comment='Categoria'),
                #
                # Descripción de la marca del Vehículo
                Field('marca', type='string', length=60,   required=True, comment='Marca'),
                #
                # Descripción del tipo de Vehículo
                Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
                #
                # Descripción del modelo del vehículo
                Field('modelo', type='string', length=100,  required=True, comment='Modelo'),
                #
                # Año/Modelo del Vehículo
                Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                # CAMPO OPCIONAL
                # Peso del Vehículo
                Field('peso', type='integer', required=True, comment='Peso'),
                # CAMPO OPCIONAL
                # Carga del Vehículo
                Field('carga', type='integer', required=True, comment='Carga'),
                # CAMPO OPCIONAL
                # Cilindrada (sólo motovehículos)
                Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
                #
                # Valuación del Vehículo
                Field('valuacion', type='integer', required=True, comment='Valuacion'),
                #
                # Código de tipo de uso del vehículo
                Field('codigotipouso', type='string', length=2,    required=True, comment='Codigo Tipo Uso'),
                #
                # Descripción del tipo de uso del vehículo
                Field('descrtipouso', type='string', length=100,  required=True, comment='Descr Tipo Uso'),
                #
                # Fecha de la inscripción inicial del vehículo
                Field('fechainscripcioninicial', type='date', required=True, comment='Fecha Inscripcion Inicial'),
                # CAMPO OPCIONAL
                # Fecha de la última transferencia del vehículo
                Field('fechaultimatransferencia', type='date', required=True, comment='Fecha Ult Transferencia'),
                # CAMPO OPCIONAL
                # Fecha del último movimiento en SU jurisdicción
                Field('fechaultimomovimiento', type='date', required=True, comment='Fecha Ult Movimiento'),
                #
                # Estado dominial. Según tabla anexa VIII
                Field('estadodominial', type='string', length=1,    required=True, comment='Estado Dominial'),
                # CAMPO OPCIONAL
                # Fecha en que se produjo el último cambio dominial
                Field('fechacambioestadodominal', type='date', required=True, comment='Fecha Camb Estado Dominial'),
                #
                # Determina si dispone de una guarda habitual
                Field('guardahabitual', type='string', length=1,    required=True, comment='Guarda Habitual'),
                # CAMPO OPCIONAL
                # Calle del domicilio de guarda
                Field('calle', type='string', length=40, required=True, comment='Calle'),
                # CAMPO OPCIONAL
                # Número de puerta del domicilio de guarda
                Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                # CAMPO OPCIONAL
                # Piso del departamento del domicilio de guarda
                Field('piso', type='string', length=10, required=True, comment='Piso'),
                # CAMPO OPCIONAL
                # Departamento del domicilio de guarda
                Field('departamento', type='string', length=10, required=True, comment='Depto'),
                # CAMPO OPCIONAL - EN LA DESCRIPCION ACTUAL EL CAMPO NO EXISTE 
                # Localidad del domicilio de guarda 
                Field('barrio', type='string', length=40, required=True, comment='Barrio'),
                # CAMPO OPCIONAL
                # Localidad del domicilio de guarda
                Field('localidad', type='string', length=40, required=True, comment='Localidad'),
                # CAMPO OPCIONAL
                # Código Postal de guarda
                Field('codigopostal', type='string', length=8, required=True, comment='Codigo Postal'),
                # CAMPO OPCIONAL
                # Provincia de guarda. Según tabla Anexo VI
                Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                #
                # Cantidad de titulares del vehículo
                Field('cantidadtitulares', type='integer', required=True, comment='Cantidad Titulares'),
                #
                # Código de Registro Seccional
                Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                #
                # Nombre del Registro Seccional
                Field('razonsocial',  type='string', length=40,   required=True, comment='Razon Social'),
                #
                # Fecha de la operación. Formato aaaa-mm-dd hh:mm:ss
                Field('fechaoperacion', type='datetime', required=True, comment='fecha Operacion'),
                # CAMPO OPCIONAL
                # Reservado para uso futuro
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                # EN LA DESCRIPCION ACTUAL EL CAMPO NO EXISTE 
                # 
                Field('controlsucerp', type='string', length=3,    required=True, comment='Control Sucerp'),
                #
                # Fecha del ingreso del registro 
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_INFORMACIONVEHICULO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'INFORMACIONVEHICULO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaInformacionVehiculo {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Informacion de Vehiculo del Titular de la ultima version de la Recepción de Datos de Sucerp
     def tablaInformacionVehiculoTitular(self):

         """
          DEFINITION OF THE HOLDER'S VEHICLE INFORMATION TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                #
                # Id identificador del registro
                Field('infvehiculotitularid', type='id', required=True, comment='Id'),
                #
                # Constante “C5 ” 
                Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
                #
                # Constante “T ”
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                #
                # Tipo de documento del titular. Según tabla anexa V
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                #
                # Número de documento correspondiente al titular
                Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                #
                # Número de CUIT / CUIL correspondiente al titular
                Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                #
                # Nombre y Apellido o Razón Social del titular del vehículo
                Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
                #
                # Porcentaje de posesión del vehiculo
                Field('porcentajetitularidad', type='integer', required=True, comment='Porcentaje Titular'),
                #
                # Calle del domicilio del titular
                Field('calle', type='string', length=40, required=True, comment='Calle'),
                #
                # Número de puerta del domicilio del titular
                Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                #
                # Piso del departamento del domicilio del titular
                Field('piso', type='string', length=10, required=True, comment='Piso'),
                #
                # Departamento del domicilio del titular
                Field('departamento', type='string', length=10, required=True, comment='Depto'),
                # CAMPO OPCIONAL
                # Barrio del domicilio del titular
                Field('barrio', type='string', length=40, required=True, comment='Barrio'),
                #
                # Localidad del domicilio del titular
                Field('localidad', type='string', length=40, required=True, comment='Localidad'),
                #
                # Código Postal del titular
                Field('codigopostal', type='string', length=8, required=True, comment='Codigo Postal'),
                #
                # Provincia del Titular. Según tabla Anexo VI
                Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                # CAMPO OPCIONAL
                # Reservado para uso futuro
                Field('reservado', type='string', length=256, required=True, comment='Reservado'),
                #
                # 
                Field('infvehiculoid', type='reference INFORMACIONVEHICULO', ondelete='CASCADE', notnull=False, comment='Id FK Inf Vehiculo'),
                #
                # Fecha del ingreso del registro 
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_INFORMACIONVEHICULOTITULAR']['migrate']

             # table construction parameters
             parm = {
                 'name': 'INFORMACIONVEHICULOTITULAR',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaInformacionVehiculoTitular {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Temporal Informacion de Vehiculo No tiene Id porque no va ser una tabla definida con DDS
     def tablaTmpInformacionVehiculo(self):

         """
          TEMPORARY VEHICLE INFORMATION TABLE DEFINITION \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

          """

         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                #
                # Id identificador del registro
                Field('INFVE00001', type='integer', comment='Id'),
                #
                # Constante “C5 ”
                Field('TIPOR00001', type='integer', comment='Id FK Tipo Cuerpo'),
                #
                # Constante “C”
                Field('TIPOS00001', type='integer', comment='Id FK Tipo Documento'),
                #
                # Código del organismo Municipal o Provincial al cual corresponde la información
                Field('CODIG0ORGA', type='integer', comment='Codigo Organismo'),
                #
                # Patente del Vehículo (Reempadronado)
                Field('DOMIN00001', type='string', length=8, comment='Dominio Nuevo'),
                #
                # Patente del Vehículo (Dominio Anterior)
                Field('DOMIN00002', type='string', length=8, comment='Dominio Viejo'),
                #
                # Código del vehículo según la DNRPA. 
                # MTM (Marca – Tipo – Modelo) y FMM (Fabrica – Marca – Modelo).
                Field('CODMTMFNM1', type='string', length=8, comment='Codigo Sucerp'),
                #
                # Tipo de origen del vehículo (N – Nacional, I – Importado).
                Field('ORIGENID01', type='integer', comment='Id FK Origen'),
                # CAMPO OPCIONAL
                # Categoría del vehículo
                Field('CATEG00001', type='string', length=3, comment='Categoria'),
                #
                # Descripción de la marca del Vehículo
                Field('MARCA00001', type='string', length=60, comment='Marca'),
                #
                # Descripción del tipo de Vehículo
                Field('TIPOV00001', type='string', length=60, comment='Tipo Vehiculo'),
                #
                # Descripción del modelo del vehículo
                Field('MODEL00001', type='string', length=100, comment='Modelo'),
                #
                # Año/Modelo del Vehículo
                Field('YYYYM00001', type='integer', comment='Año Modelo'),
                # CAMPO OPCIONAL
                # Peso del Vehículo
                Field('PESO_00001', type='integer', comment='Peso'),
                # CAMPO OPCIONAL
                # Carga del Vehículo
                Field('CARGA00001', type='integer', comment='Carga'),
                # CAMPO OPCIONAL
                # Cilindrada (sólo motovehículos)
                Field('CILIN00001', type='integer', comment='Cilindrada'),
                #
                # Valuación del Vehículo
                Field('VALUA00001', type='integer', comment='Valuacion'),
                #
                # Código de tipo de uso del vehículo
                Field('CODIG00003', type='string', length=2, comment='Codigo Tipo Uso'),
                #
                # Descripción del tipo de uso del vehículo
                Field('DESCR00001', type='string', length=100, comment='Descr Tipo Uso'),
                #
                # Fecha de la inscripción inicial del vehículo
                Field('FECHA00001', type='date', comment='Fecha Inscripcion Inicial'),
                # CAMPO OPCIONAL
                # Fecha de la última transferencia del vehículo
                Field('FECHA00002', type='date', comment='Fecha Ult Transferencia'),
                # CAMPO OPCIONAL
                # Fecha del último movimiento en SU jurisdicción
                Field('FECHA00003', type='date', comment='Fecha Ult Movimiento'),
                #
                # Estado dominial. Según tabla anexa VIII
                Field('ESTAD00001', type='string', length=1, comment='Estado Dominial'),
                # CAMPO OPCIONAL
                # Fecha en que se produjo el último cambio dominial
                Field('FECHA00004', type='date', comment='Fecha Camb Estado Dominial'),
                #
                # Determina si dispone de una guarda habitual
                Field('GUARD00001', type='string', length=1, comment='Guarda Habitual'),
                # CAMPO OPCIONAL
                # Calle del domicilio de guarda
                Field('CALLE00001', type='string', length=40, comment='Calle'),
                # CAMPO OPCIONAL
                # Número de puerta del domicilio de guarda
                Field('NUMER00002', type='string', length=10, comment='Nro Puerta'),
                # CAMPO OPCIONAL
                # Piso del departamento del domicilio de guarda
                Field('PISO_00001', type='string', length=10, comment='Piso'),
                # CAMPO OPCIONAL
                # Departamento del domicilio de guarda
                Field('DEPAR00001', typr='string', length=10, comment='Depto'),
                # CAMPO OPCIONAL - EN LA DESCRIPCION ACTUAL EL CAMPO NO EXISTE 
                # Localidad del domicilio de guarda 
                Field('BARRI00001', type='string', length=40, comment='Barrio'),
                # CAMPO OPCIONAL
                # Localidad del domicilio de guarda
                Field('LOCAL00001', type='string', length=40, comment='Localidad'),
                # CAMPO OPCIONAL
                # Código Postal de guarda
                Field('CODIG00004', type='string', length=8, comment='Codigo Postal'),
                # CAMPO OPCIONAL
                # Provincia de guarda. Según tabla Anexo VI
                Field('PROVI00001', type='integer', comment='Id FK Provincia'),
                #
                # Cantidad de titulares del vehículo
                Field('CANTI00001', type='integer', comment='Cantidad Titulares'),
                #
                # Código de Registro Seccional
                Field('CODIG00005', type='integer', comment='Codigo Registro Seccional'),
                #
                # Nombre del Registro Seccional
                Field('RAZON00001', type='string', length=40, comment='Razon Social'),
                #
                # Fecha de la operación. Formato aaaa-mm-dd hh:mm:ss
                Field('FECHA00005', type='datetime', comment='fecha Operacion'),
                # CAMPO OPCIONAL
                # Reservado para uso futuro
                Field('RESER00001', type='string', length=256, comment='Reservado'),
                # EN LA DESCRIPCION ACTUAL EL CAMPO NO EXISTE 
                # 
                Field('CONTR00001', type='string', length=3, comment='Control Sucerp'),
                #
                # Fecha del ingreso del registro 
                Field('KTIME00001', type='datetime', comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TMPINFORMACIONVEHICULO']['migrate']

             # Primary Key List
             primary = ['INFVE00001']

             # table construction parameters
             parm = {
                 'name': 'INFOR00001',
                 'fields': tuple(lista),
                 'arg': {'primarykey': primary, 'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaTmpInformacionVehiculo {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Temporal Informacion de Vehiculo Titular No tiene Id porque no va ser una tabla definida con DDS
     def tablaTmpInformacionVehiculoTitular(self):

         """
          DEFINITION OF THE INFORMATION TABLE OF THE TEMPORARY OWNER VEHICLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

          """

         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                 
                #
                # Id identificador del registro
                Field('INFVE00003', type='integer', comment='Id'),
                #
                # Constante “C5 ” 
                Field('TIPOC00001', type='integer', comment='Id FK Tipo Cuerpo'),
                #
                # Constante “T ”
                Field('TIPOS00001', type='integer', comment='Id FK Tipo Sub Registro'),
                #
                # Tipo de documento del titular. Según tabla anexa V
                Field('TIPOD00001', type='integer', comment='Id FK Tipo Documento'),
                 
                #
                # Número de documento correspondiente al titular
                Field('NUMER00001', type='integer', comment='Nro Documento'),
                 
                #
                # Número de CUIT / CUIL correspondiente al titular
                Field('CUITC00001', type='integer', comment='Cuit/Cuil'),
                 
                #
                # Nombre y Apellido o Razón Social del titular del vehículo
                Field('APELL00001', type='string', length=150, comment='Apellido y Nombre'),
                 
                #
                # Porcentaje de posesión del vehiculo
                Field('PORCE00001', type='integer', comment='Porcentaje Titular'),
                 
                #
                # Calle del domicilio del titular
                Field('CALLE00001', type='string', length=40, comment='Calle'),
                 
                #
                # Número de puerta del domicilio del titular
                Field('NUMER00002', type='string', length=10, comment='Nro Puerta'),
                 
                #
                # Piso del departamento del domicilio del titular
                Field('PISO_00001', type='string', length=10, comment='Piso'),
                 
                #
                # Departamento del domicilio del titular
                Field('DEPAR00001', type='string', length=10, comment='Depto'),
                 
                # CAMPO OPCIONAL
                # Barrio del domicilio del titular
                Field('BARRI00001', type='string', length=40, comment='Barrio'),
                 
                #
                # Localidad del domicilio del titular
                Field('LOCAL00001', type='string', length=40, comment='Localidad'),
                 
                #
                # Código Postal del titular
                Field('CODIG00001', type='string', length=8, comment='Codigo Postal'),
                 
                #
                # Provincia del Titular. Según tabla Anexo VI
                Field('PROVI00001', type='integer', comment='Id FK Provincia'),
                 
                # CAMPO OPCIONAL
                # Reservado para uso futuro
                Field('RESER00001', type='string', length=256, comment='Reservado'),
                 
                #
                # 
                Field('INFVE00002', type='integer', comment='Id FK Inf Vehiculo'),
                 
                #
                # Fecha del ingreso del registro 
                Field('KTIME00001', type='detetime', comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TMPINFORMACIONVEHICULOTITULAR']['migrate']

             # Lista de Primary Key
             primary = ['INFVE00003']

             # table construction parameters
             parm = {
                 'name': 'INFOR00002',
                 'fields': tuple(lista),
                 'arg': {'primarykey': primary, 'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm
         except Exception as e:
             print(f'Error - tablaTmpInformacionVehiculoTitular {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Cambio de Titularidad de la ultima version de la Recepción de Datos de Sucerp
     def tablaCambioTitularidad(self):
         """
          DEFINITION OF THE CHANGE OF OWNERSHIP TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:
             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                #
                # Id identificador del registro
                Field('cambiotitularidadid', type='id', required=True, comment='Id'),
                #
                # Constante “C6 ”
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                #
                # Constante “C”
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                #
                # Código del organismo Municipal o Provincial al cual corresponde la información
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                # CAMPO OPCIONAL
                # Número de trámite interno de la aplicación
                Field('numerotramite', type='bigint', required=True, comment='Nro Tramite'),
                #
                # Código de trámite registral realizado
                Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                #
                # Descripción del tipo de trámite registral realizado
                Field('descrtipotramite', type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
                #
                # Código del tipo de acción realizada por el contribuyente
                Field('codigotipoaccion', type='integer', required=True, comment='Codigo Tipo Accion'),
                #
                # Descripción del tipo de acción realizada por el contribuyente
                Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr Tipo Accion'),
                #
                # Identificador de tipo de formulario exigible para el trámite
                Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
                #
                # Número de formulario en el que se realizo el trámite
                Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
                #
                # Patente del Vehículo (Reempadronado)
                Field('dominionuevo', type='string', length=8,    required=True, comment='Dominio Nuevo'),
                #
                # Patente del Vehículo (Dominio Anterior)
                Field('dominioviejo', type='string', length=8,    required=True, comment='Dominio Viejo'),
                #
                # Código del vehículo según la DNRPA. MTM (Marca – Tipo – Modelo) y FMM (Fabrica – Marca – Modelo).
                Field('codigomtmfmm', type='string', length=8,    required=True, comment='Codigo Sucerp'),
                #
                # Tipo de origen del vehículo (N – Nacional, I – Importado).
                Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
                # CAMPO OPCIONAL
                # Categoría del vehículo
                Field('categoría', type='string', length=3, required=True, comment='Categoria'),
                #
                # Descripción de la marca del Vehículo
                Field('marca', type='string', length=60, required=True, comment='Marca'),
                #
                # Descripción del tipo de Vehículo
                Field('tipovehiculo', type='string', length=60, required=True, comment='Tipo Vehiculo'),
                #
                # Descripción del modelo del vehículo
                Field('modelo', type='string', length=100, required=True, comment='Modelo'),
                #
                # Año/Modelo del Vehículo
                Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                # CAMPO OPCIONAL
                # Peso del Vehículo
                Field('peso', type='integer', required=True, comment='Peso'),
                # CAMPO OPCIONAL
                # Carga del Vehículo
                Field('carga', type='integer', required=True, comment='Carga'),
                #
                # Cilindrada (sólo motovehículos)
                Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
                #
                # Valuación del Vehículo
                Field('valuacion', type='integer', required=True, comment='Valuacion'),
                #
                # Código de tipo de uso del vehículo
                Field('codigotipouso', type='string', length=2, required=True, comment='Codigo Tipo Uso'),
                #
                # Descripción del tipo de uso del vehículo
                Field('descrtipouso', type='string', length=100, required=True, comment='Descr Tipo Uso'),
                #
                # Fecha de Transferencia. Formato aaaa-mm-dd
                Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
                #
                # Tipo de documento del titular principal. Según tabla anexa V
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                #
                # Número de documento correspondiente al titular principal
                Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                #
                # Número de CUIT o CUIL del titular principal
                Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                #
                # Nombre y Apellido o Razón Social del titular principal
                Field('apenomrazonsocial', type='string', length=150, required=True, comment='ApeNom Razon Social'),
                #
                # Calle donde recibirá el impuesto
                Field('calle', type='string', length=40, required=True, comment='Calle'),
                #
                # Número donde recibirá el impuesto
                Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                # CAMPO OPCIONAL
                # Piso donde recibirá el impuesto
                Field('piso', type='string', length=10, required=True, comment='Piso'),
                # CAMPO OPCIONAL  
                # Departamento donde recibirá el impuesto
                Field('departamento', type='string', length=10, required=True, comment='Depto'),
                # CAMPO OPCIONAL
                # Barrio donde recibirá el impuesto
                Field('barrio', type='string', length=40, required=True, comment='Barrio'),
                #
                # Localidad donde recibirá el impuesto
                Field('localidad', type='string', length=40, required=True, comment='Localidad'),
                #
                # Código Postal donde recibirá el impuesto
                Field('codigopostal', type='string', length=8, required=True, comment='Codigo Postal'),
                #
                # Provincia donde recibirá el impuesto
                Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                #
                # Cantidad de titulares del vehículo
                Field('cantidadtitulares', type='integer', required=True, comment='Cantidad Titulares'),
                #
                # Código de registro seccional que realizó la transacción
                Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                #
                # Nombre del Registro Seccional
                Field('razonsocial', type='string', length=40, required=True, comment='Razon Social'),
                #
                # Fecha de la operación. Formato aaaa-mm-dd hh:mm:ss
                Field('fechaoperacion', type='datetime', required=True, comment='fecha Operacion'),
                # CAMPO OPCIONAL
                # Contiene los datos de cada parámetro adicional que el organismo requiera al realizar el trámite. 
                # Dispone de un máximo de 10 valores adicionales. Ver anexo VII.
                Field('parametrosadicionales', type='string', length=650, required=True, comment='Parm Adicionales'),
                # CAMPO OPCIONAL
                # Reservado para uso futuro
                Field('reservado', type='string', length=256, required=True, comment='Reservado'),
                # CAMPO OPCIONAL
                # Observaciones
                Field('observaciones', type='string', length=256, required=True, comment='Observaciones'),
                #
                #
                Field('cambiotitularidadtitid', type='reference CAMBIOTITULARIDADTITULAR', ondelete='CASCADE', comment='Id FK Camb Titularidad Titu'),
                #
                # Fecha del ingreso del registro 
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_CAMBIOTITULARIDAD']['migrate']

             # table construction parameters
             parm = {
                 'name': 'CAMBIOTITULARIDAD',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaCambioTitularidad {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Cambio de Titularidad Titular de la ultima version de la Recepción de Datos de Sucerp
     def tablaCambioTitularidadTitular(self):

         """
          DEFINITION OF THE TABLE OF CHANGE OF OWNERSHIP OF THE HOLDER \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                #
                # Id identificador del registro
                Field('cambiotitularidadtitid', type='id', required=True, comment='Id'),
                #
                # Constante “C6 ”
                Field('tipocuerpoid', type='reference TIPOCUERPO', ondelete='CASCADE', comment='Id FK Tipo Cuerpo'),
                #
                # Constante “T ”
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                #
                # Determina el tipo de titular transferido. (N=Titular Nuevo – A=Titular Anterior)
                Field('tipotitularid', type='reference TIPOTITULAR', ondelete='CASCADE', comment='Id FK Tipo Titular'),
                #
                # Tipo de documento del titular. Según tabla anexa V
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                #
                # Número de documento correspondiente al titular
                Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                #
                # Número de CUIT / CUIL correspondiente al titularId identificador del registro
                Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                #
                # Nombre y Apellido o Razón Social del titular del vehículo
                Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
                #
                # Porcentaje de posesión del vehiculo
                Field('porcentajetitularidad', type='integer', required=True, comment='Porcentaje Titular'),
                #
                # Calle del domicilio del titular
                Field('calle', type='string', length=40, required=True, comment='Calle'),
                #
                # Número de puerta del domicilio del titular
                Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                # CAMPO OPCIONAL
                # Piso del departamento del domicilio del titular
                Field('piso', type='string', length=10, required=True, comment='Piso'),
                # CAMPO OPCIONAL
                # Departamento del domicilio del titular
                Field('departamento', type='string', length=10, required=True, comment='Depto'),
                # CAMPO OPCIONAL
                # Barrio del domicilio del titular
                Field('barrio', type='string', length=40, required=True, comment='Barrio'),
                #
                # Localidad del domicilio del titular
                Field('localidad', type='string', length=40, required=True, comment='Localidad'),
                #
                # Código Postal del titular
                Field('codigopostal', type='string', length=8, required=True, comment='Codigo Postal'),
                #
                # Provincia del Titular. Según tabla Anexo VI
                Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                # CAMPO OPCIONAL
                # Reservado para uso futuro
                Field('reservado', type='string', length=256, required=True, comment='Reservado'),
                #
                # Fecha del ingreso del registro 
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_CAMBIOTITULARIDADTITULAR']['migrate']

             # table construction parameters
             parm = {
                 'name': 'CAMBIOTITULARIDADTITULAR',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaCambioTitularidadTitular {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Informacion de Radicacion de la ultima version de la Recepción de Datos de Sucerp
     def tablaInformacionRadicacion(self):

         """
          DEFINITION OF THE FILING INFORMATION TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                #
                # Id identificador del registro
                Field('infradicacionid', type='id', required=True, comment='Id'),
                #
                # Constante “C7 ”
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                #
                # Código del organismo Municipal o Provincial al cual corresponde la información
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                #
                # Patente del Vehículo
                Field('dominio', type='string', length=8,    required=True, comment='Dominio'),
                #
                # Estado de la radicación del vehículo (A – Activa, B – Baja, C - Cancelada).
                Field('estadoid', type='reference TIPOESTADO',  ondelete='CASCADE', comment='Id FK Estado'),
                #
                # Tipo de la radicación (D – Definitiva, P – Pendiente, T – Temporal).
                Field('tiporadicacion', type='string', length=1,    required=True, comment='Tipo Radicacion'),
                #
                # Fecha de alta en la jurisdicción. Formato aaaamm-dd
                Field('fechaalta', type='date', required=True, comment='Fecha Alta'),
                #
                # Fecha de baja en la jurisdicción. Formato aaaamm-d
                Field('fechabajaradicacion', type='date', required=True, comment='Fecha Baja Radicacion'),
                #
                # Determina de donde proviene la información 
                # del estado de la radicación (M – Municipalidad, R – Registro Seccional).
                Field('origeninformacion', type='string', length=1,    required=True, comment='Origen Informacion'),
                #
                # Código del Registro Seccional donde se originó la modificación de la radicación.
                Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                #
                # Razón Social del Registro Seccional donde se originó la modificación de la radicación.
                Field('razonsocialregistro', type='string', length=100,  required=True, comment='Razon Social Registro'),
                # CAMPO OPCIONAL
                # Reservado para uso futuro
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                #
                # Observaciones ingresadas al momento 
                # de la modificación de la radiación por parte de un Registro Seccional
                Field('observaciones', type='string', length=256,  required=True, comment='Observaciones'),
                #
                # Fecha del ingreso del registro 
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_INFORMACIORADICACION']['migrate']

             # table construction parameters
             parm = {
                 'name': 'INFORMACIORADICACION',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaInformacionRadicacion {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Anulacion de Tramites de Sellos de la ultima version de la Recepción de Datos de Sucerp
     def tablaAnulacionTramitesSellos(self):

         """
          DEFINITION OF THE TABLE FOR CANCELLATION OF STAMP PROCEDURES \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """

         try:

             lista, primary, parm = list(), list(), dict()


             # fields list
             lista = [
                #
                # Id identificador del registro
                Field('anultramitesellosid', type='id', required=True, comment='Id'),
                #
                # Constante “C8 ”
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                #
                # Constante “C”
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                #
                # Código del organismo Municipal o Provincial al cual corresponde la información
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                #
                # Determina el tipo de anulación, puede ser un trámite de patentes “P” o de sellos “S”
                Field('tipoanulacion',            type='string', length=1,    required=True, comment='Tipo Anulacion'),
                #
                # Número de trámite interno de la aplicación (sello o patente)
                Field('numerotramite', type='bigint',              required=True, comment='Nro Tramite'),
                #
                # Código de trámite registral realizado
                Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                #
                # Descripción del tipo de trámite registral realizado
                Field('descrtipotramite',         type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
                #
                # Código del tipo de acción realizada por el contribuyente
                Field('codigotipoaccion', type='integer', required=True, comment='Codigo Tipo Accion'),
                #
                # Descripción del tipo de acción realizada por el contribuyente
                Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr Tipo Accion'),
                #
                # Identificador del tipo de formulario exigible para el trámite
                Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
                #
                # Número de formulario en el que se realizó el trámite
                Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
                # CAMPO OPCIONAL
                # Patente del Vehículo (Reempadronado)
                Field('dominionuevo', type='string', length=8,    required=True, comment='Dominio Nuevo'),
                # CAMPO OPCIONAL
                # Patente del Vehículo (Dominio Anterior)
                Field('dominioviejo', type='string', length=8,    required=True, comment='Dominio Viejo'),
                # CAMPO OPCIONAL
                # Número del comprobante entregado por el Registro Seccional
                Field('numerorecibo',             type='string', length=15,   required=True, comment='Nro Recibo'),
                #
                # Código del vehículo según la DNRPA. MTM (Marca – Tipo – Modelo) y FMM (Fábrica – Marca – Modelo)
                Field('codigomtmfmm', type='string', length=8,    required=True, comment='Codigo Sucerp'),
                #
                # Tipo de origen del vehículo (N – Nacional, I – Importado)
                Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
                #
                # Categoría del vehículo
                Field('categoría', type='string', length=3,    required=True, comment='Categoria'),
                #
                # Descripción de la marca del Vehículo
                Field('marca', type='string', length=60,   required=True, comment='Marca'),
                #
                # Descripción del tipo de Vehículo
                Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
                #
                # Descripción del modelo del vehículo
                Field('modelo', type='string', length=100,  required=True, comment='Modelo'),
                #
                # Año/Modelo del Vehículo
                Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                #
                # Formato de la fecha de contrato/vigencia aaaamm-dd.
                Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
                #
                # Importe total percibido
                Field('montototal',               type='decimal(12, 2)',      required=True, comment='Monto Total'),
                #
                # Importe total del impuesto
                Field('montoimpuesto', type='decimal(12, 2)', required=True, comment='Monto Impuesto'),
                #
                # Importe percibido por punitorios
                Field('montopunitorio', type='decimal(12, 2)', required=True, comment='monto Punitorio'),
                #
                # Importe adicional
                Field('montoadicional', type='decimal(12, 2)', required=True, comment='Monto Adicional'),
                #
                # Según tabla Anexo III
                Field('codigoformapagoid', type='reference TIPOPAGO', ondelete='CASCADE', comment='Id FK Cod Forma Pago'),
                #
                # Según tabla Anexo IV
                Field('codigomonedaid', type='reference TIPOMONEDA', ondelete='CASCADE', comment='Id FK Cod Moneda'),
                #
                # Código de entidad bancaria
                Field('codigoentidadbancaria', type='integer', required=True, comment='Codigo Entidad Bancaria'),
                #
                # Razón Social de la entidad bancaria
                Field('descrentidadbancaria',     type='string', length=60,   required=True, comment='Descr Entidad Bancaria'),
                #
                # Número de cheque
                Field('numerocheque',             type='string', length=20,   required=True, comment='Nro Cheque'),
                #
                # Formato de la fecha de emisión del trámite aaaa - mm - dd hh:mm:ss
                Field('fechatramite', type='datetime', required=True, comment='Fecha Tramite'),
                # CAMPO OPCIONAL
                # Formato de la fecha de cobro aaaa-mm- dd hh:mm:ss
                Field('fechacobro', type='datetime', required=True, comment='Fecha Cobro'),
                # CAMPO OPCIONAL
                # Formato de la fecha de depósito aaaa-mm- dd hh:mm:ss.
                Field('fechadeposito', type='datetime', required=True, comment='fecha Deposito'),
                #
                # Formato de la fecha de anulación del trámite aaaa-mm- dd hh:mm:ss
                Field('fechabaja', type='date', required=True, comment='Fecha Baja'),
                #
                # Cantidad de registros de detalles de la anulación
                Field('cantidaddetalle', type='integer', required=True, comment='Cantidad Detalle'),
                #
                # Código del Registro Seccional
                Field('codigoregistroseccional', type='integer', required=True, comment='Codigo Registro Seccional'),
                #
                # Nombre del Registro Seccional
                Field('descrregistroseccional', type='string', length=40,   required=True, comment='Descr Registro Seccional'),
                # CAMPO OPCIONAL
                # Reservado para el uso del organismo. 
                # Recuerde que no podrá contener ni caracteres pipe “|” 
                # ni el separador que utilice para el protocolo
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                # CAMPO OPCIONAL
                # Observaciones
                Field('observaciones',            type='string', length=256,  required=True, comment='Observaciones'),
                #
                # Fecha del ingreso del registro 
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]


             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ANULACIONTRAMITESSELLOS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'ANULACIONTRAMITESSELLOS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaAnulacionTramitesSellos {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Anulacion de Tramites de Sellos Detalle de la ultima version de la Recepción de Datos de Sucerp
     def tablaAnulacionTramitesSellosDetalle(self):

         """
          DETAILED DEFINITION OF THE TABLE FOR CANCELLATION OF STAMP PROCEDURES \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                #
                # Id identificador del registro
                Field('anultramitesellosdetid', type='id', required=True, comment='Id'),
                #
                # Constante “C8 ”
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                #
                # Constante “D”
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                #
                # Año Fiscal
                Field('yyyy', type='integer', required=True, comment='Año'),
                #
                # Número de Cuota
                Field('numerocuota', type='integer', required=True, comment='Nro Cuota'),
                #
                # Según tabla Anexo II o los tipos que se convengan al momento de salir operativos
                Field('tipocuotaid', type='reference TIPOCUOTA', ondelete='CASCADE', comment='Id FK Tipo Cuota'),
                #
                # Importe total percibido
                Field('importetotal', type='decimal(10, 2)',      required=True, comment='Importe Total'),
                #
                # Importe total del impuesto
                Field('importeimpuesto', type='decimal(10, 2)', required=True, comment='Importe Impuesto'),
                #
                # Importe percibido por punitorios
                Field('importepunitorio', type='decimal(10, 2)', required=True, comment='Importe Punitorio'),
                #
                # Importe adicional
                Field('importeadicional',         type='decimal(10, 2)',      required=True, comment='Importe Adicional'),
                # CAMPO OPCIONAL
                # Reservado para el uso del organismo. 
                # Recuerde que no podrá contener ni caracteres pipe “|” 
                # ni el separador que utilice para el protocolo
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                # CAMPO OPCIONAL
                # Observaciones
                Field('observaciones',            type='string', length=256,  required=True, comment='Observaciones'),
                #
                # Relación de ANULACIONTRAMITESSELLOS
                Field('anultramitesellosid', type='reference ANULACIONTRAMITESSELLOS', ondelete='CASCADE', comment='Id FK Anulacion Tramites Sellos'),
                #
                # Fecha del ingreso del registro 
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_ANULACIONTRAMITESSELLOSDETALLE']['migrate']

             # table construction parameters
             parm = {
                 'name': 'ANULACIONTRAMITESSELLOSDETALLE',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaAnulacionTramitesSellosDetalle {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Tramites Generales de la ultima version de la Recepción de Datos de Sucerp
     def tablaTramitesGenerales(self):

         """
          DEFINITION OF THE TABLE OF GENERAL PROCEDURES \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields  list
             lista = [
                #
                # Id identificador del registro
                Field('tramitesgeneralesid', type='id', required=True, comment='Id'),
                #
                # Constante “C9 ”
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                #
                # Constante “C”
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                #
                # Código del organismo Municipal o Provincial al cual corresponde la información
                Field('codigoorganismo', type='integer', required=True, comment='Codigo Organismo'),
                #
                # Número de trámite interno de la aplicación
                Field('numerotramite', type='bigint',              required=True, comment='Nro Tramite'),
                #
                # Código de trámite registral realizado
                Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                #
                # Descripción del tipo de trámite registral realizado
                Field('descrtipotramite',         type='string', length=60,   required=True, comment='Descr Tipo Tramite'),
                #
                # Código del tipo de acción realizada por el contribuyente
                Field('codigotipoaccion', type='integer', required=True, comment='Codigo Tipo Accion'),
                #
                # Descripción del tipo de acción realizada por el contribuyente
                Field('descrtipoaccion', type='string', length=60,   required=True, comment='Descr Tipo Accion'),
                #
                # Identificador de tipo de formulario exigible para el trámite
                Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
                #
                # Número de formulario en el que se realizó el trámite
                Field('numeroformulario', type='integer', required=True, comment='Nro Formulario'),
                #
                # Patente del Vehículo (Reempadronado)
                Field('dominionuevo', type='string', length=8,    required=True, comment='Dominio Nuevo'),
                #
                # Patente del Vehículo (Dominio Anterior)
                Field('dominioviejo', type='string', length=8,    required=True, comment='Dominio Viejo'),
                #
                # Código del vehículo según la DNRPA. 
                # MTM (Marca – Tipo – Modelo) y FMM (Fabrica – Marca – Modelo).
                Field('codigomtmfmm', type='string', length=8,    required=True, comment='Codigo Sucerp'),
                #
                # Tipo de origen del vehículo (N – Nacional, I – Importado).
                Field('origenid', type='reference TIPOORIGEN', ondelete='CASCADE', comment='Id FK Origen'),
                # CAMPO OPCIONAL
                # Categoría del vehículo
                Field('categoría', type='string', length=3,    required=True, comment='Categoria'),
                #
                # Descripción de la marca del Vehículo
                Field('marca', type='string', length=60,   required=True, comment='Marca'),
                #
                # Descripción del tipo de Vehículo
                Field('tipovehiculo', type='string', length=60,   required=True, comment='Tipo Vehiculo'),
                #
                # Descripción del modelo del vehículo
                Field('modelo', type='string', length=100,  required=True, comment='Modelo'),
                #
                # Año/Modelo del Vehículo
                Field('yyyymodelo', type='integer', required=True, comment='Año Modelo'),
                # CAMPO OPCIONAL
                # Peso del Vehículo
                Field('peso', type='integer', required=True, comment='Peso'),
                # CAMPO OPCIONAL
                # Carga del Vehículo
                Field('carga', type='integer', required=True, comment='Carga'),
                # CAMPO OPCIONAL
                # Cilindrada (sólo motovehículos)
                Field('cilindrada', type='integer', required=True, comment='Cilindrada'),
                #
                # Valuación del Vehículo
                Field('valuacion', type='integer', required=True, comment='Valuacion'),
                #
                # Código de tipo de uso del vehículo
                Field('codigotipouso', type='string', length=2,    required=True, comment='Codigo Tipo Uso'),
                #
                # Descripción del tipo de uso del vehículo
                Field('descrtipouso', type='string', length=100,  required=True, comment='Descr Tipo Uso'),
                #
                # Fecha de Transferencia. Formato aaaa-mm-dd
                Field('fechavigencia', type='date', required=True, comment='Fecha Vigencia'),
                #
                # Tipo de documento del titular principal. Según tabla anexa V
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                #
                # Número de documento correspondiente al titular principal
                Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                #
                # Número de CUIT o CUIL del titular principal
                Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                #
                # Nombre y Apellido o Razón Social del titular principal
                Field('apenomrazonsocial', type='string', length=150,  required=True, comment='ApeNom Razon Social'),
                #
                # Calle donde recibirá el impuesto
                Field('calle', type='string', length=40,   required=True, comment='Calle'),
                #
                # Número donde recibirá el impuesto
                Field('numero', type='string', length=10, required=True, comment='Nro Puerta'),
                # CAMPO OPCIONAL
                # Piso donde recibirá el impuesto
                Field('piso', type='string', length=10,   required=True, comment='Piso'),
                # CAMPO OPCIONAL
                # Departamento donde recibirá el impuesto
                Field('departamento', type='string', length=10,   required=True, comment='Depto'),
                # CAMPO OPCIONAL
                # Barrio donde recibirá el impuesto
                Field('barrio', type='string', length=40,   required=True, comment='Barrio'),
                #
                # Relación de TRAMITESGENERALESTITULARES
                Field('tramitesgeneralestitid', type='reference TRAMITESGENERALESTITULARES', ondelete='CASCADE', comment='Id FK Tramite Grales Tramites'),
                #
                # Fecha del ingreso del registro 
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TRAMITESGENERALES']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TRAMITESGENERALES',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaTramitesGenerales {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Tramites Generales Titulares de la ultima version de la Recepción de Datos de Sucerp
     def tablaTramitesGeneralesTitulares(self):

         """
          DEFINITION OF THE TABLE OF GENERAL PROCEDURES FOR HOLDERS \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                #
                # Id identificador del registro
                Field('tramitesgeneralestitid', type='id', required=True, comment='Id'),
                #
                # Constante “C9 ”
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                #
                # Constante “T ”
                Field('tiposubregistroid', type='reference TIPOSUBREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Sub Registro'),
                #
                # Determina el tipo de titular transferido. (N=Titular Nuevo – A=Titular Anterior)
                Field('tipotitularid', type='reference TIPOTITULAR', ondelete='CASCADE', comment='Id FK Tipo Titular'),
                #
                # Tipo de documento del titular. Según tabla anexa V
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                #
                # Número de documento correspondiente al titular
                Field('numerodocumento', type='bigint', required=True, comment='Nro Documento'),
                #
                # Número de CUIT / CUIL correspondiente al titular
                Field('cuitcuil', type='bigint', required=True, comment='Cuit/Cuil'),
                #
                # Nombre y Apellido o Razón Social del titular del vehículo
                Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
                #
                # Porcentaje de posesión del vehiculo
                Field('porcentajetitularidad', type='integer', required=True, comment='Procentaje Titular'),
                #
                # Calle del domicilio del titular
                Field('calle', type='string', length=40,   required=True, comment='Calle'),
                #
                # Número de puerta del domicilio del titular
                Field('numero', type='string', length=10,   required=True, comment='Nro Puerta'),
                # CAMPO OPCIONAL
                # Piso del departamento del domicilio del titular
                Field('piso', type='string', length=10,   required=True, comment='Piso'),
                # CAMPO OPCIONAL
                # Departamento del domicilio del titular
                Field('departamento', type='string', length=10,   required=True, comment='Depto'),
                # CAMPO OPCIONAL
                # Barrio del domicilio del titular
                Field('barrio', type='string', length=40,   required=True, comment='Barrio'),
                #
                # Localidad del domicilio del titular
                Field('localidad', type='string', length=40,   required=True, comment='Localidad'),
                #
                # Código Postal del titular
                Field('codigopostal', type='string', length=8,    required=True, comment='Codigo Postal'),
                #
                # Provincia del Titular. Según tabla Anexo VI
                Field('provinciaid', type='reference PROVINCIAS', ondelete='CASCADE', comment='Id FK Provincia'),
                # CAMPO OPCIONAL
                # Reservado para uso futuro
                Field('reservado', type='string', length=256,  required=True, comment='Reservado'),
                #
                # Fecha del ingreso del registro 
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_TRAMITESGENERALESTITULARES']['migrate']

             # table construction parameters
             parm = {
                 'name': 'TRAMITESGENERALESTITULARES',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaTramitesGeneralesTitulares {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Pie de la ultima version de la Recepción de Datos de Sucerp
     def tablaPie(self):

         """
          DEFINITION OF THE FOOT BOARD \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()


             # fields list
             lista = [
                #
                # Id identificador del registro
                Field('pieid', type='id', required=True, comment='Id'),
                #
                # Constante “P0 ”
                Field("tiporegistroid", type='reference TIPOREGISTRO', ondelete='CASCADE', comment='Id FK Tipo Registro'),
                #
                # Cantidad de cuerpos enviados
                Field('cantidadregistros', type='integer', required=True, comment='Cantidad Regsitros'),
                #
                # Hash de verificación de redundancia cíclica, 
                # la misma se calcula utilizando el algoritmo MD5 
                # sobre el contenido del archivo sin incluir el 
                # encabezado ni pie del mismo.
                Field('checksum',                 type='string', length=32,   required=True, comment='Check Sum'),
                #
                # Fecha del ingreso del registro 
                Field('ktimestamp', type='datetime', required=True, comment='Key Time Stamp')
                ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_PIE']['migrate']

             # table construction parameters
             parm = {
                 'name': 'PIE',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaPie {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla para Responder al Api
     def tablaApiAumoso(self):

         """
          DEFINITION OF THE AUMOSO TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()


             # fields list
             lista = [
                Field('aumosoid', type='id', required=True, comment='Id'),
                Field('idpakey', type='bigint', required=True, comment='IdPakey'),
                Field('samnrodoc', type='bigint', required=True, comment='Sam Nro Documento'),
                Field('samcuit', type='bigint', required=True, comment='Sam Cuit'),
                Field('samareages', type='bigint', required=True, comment='Sam Area Gestion'),
                Field('samdareages', type='string', length=100,  required=True, comment='Sam Descr Area Gestion'),
                Field('idcontrib', type='string', length=15,   required=True, comment='Id FK Contrib'),
                Field('samcontmu', type='bigint', required=True, comment='Sam Cont Mu'),
                Field('samaaocuo', type='integer', required=True, comment='Sam Año Cuota'),
                Field('samcuota', type='string', length=2,    required=True, comment='Sam Cuota'),
                Field('samtasa', type='integer', required=True, comment='Sam Tasa'),
                Field('samdtasa', type='string', length=100,  required=True, comment='Desc Sam Tasa'),
                Field('samconvenio', type='integer', required=True, comment='Sam Convenio'),
                Field('samimporte', type='decimal(15, 2)',      required=True, comment='Sam Importe'),
                Field('samfecvto', type='date', required=True, comment='Sam Fecha Vencimiento'),
                Field('samintpuni', type='decimal(15, 2)', required=True, comment='Sam Intereses Punitorios'),
                Field('samintresa', type='decimal(15, 2)', required=True, comment='Sam Intresa'),
                Field('samrecargo', type='decimal(15, 2)', required=True, comment='Sam Recargo'),
                Field('samfeccal', type='date', required=True, comment='Sam Fecha Calculo'),
                Field('samimpboni', type='decimal(15, 2)', required=True, comment='Sam Importe Bonificado'),
                Field('samfevtbon', type='date', required=True, comment='Sam Fecha Venc Bonificacion'),
                Field('samcodbarr', type='string', length=50, required=True, comment='Sam Cod Barra'),
                Field('tokenapiid', type='reference APITOKEN', ondelete='CASCADE', comment='Id FK Token Api'),
                Field('cuotacancelada',  type='string', length=1,    required=True, default='N', comment='Cuota Cancelada'),
                Field('codigotipotramite', type='integer', required=True, comment='Codigo Tipo Tramite'),
                Field('tipoformulario', type='integer', required=True, comment='Tipo Formulario'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_AUMOSO']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APIAUMOSO',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiAumoso {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Estados para Responder al Api
     def tablaApiEstados(self):

         """
          API STATE TABLE DEFINITION \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

          """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('apiestadosid', type='id', required=True, comment='Id'),
                Field('apiestadodescripcion', unique=True, type='string', length=100, required=True, comment='Descr Token Api Estado'),
                Field('apiusercrt',               type='string', length=10,   required=True, comment='Token Api User Create'),
                Field('tokenusercrttimestamp', type='datetime', required=True, comment='Token Api User Crt Time Stamp'),
                Field('apiuserdlt',               type='string', length=10,   required=True, comment='Token Api User Delete'),
                Field('tokenuserdlttimestamp', type='datetime', required=True, comment='Token Api User Dlt Time Stamp'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_ESTADOS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APIESTADOS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiEstados {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Log de Errores del Apí
     def tablaApiLog(self):

         """
          API LOG TABLE DEFINITION \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

          """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('apilogid', type='id',  comment='Id'),
                Field('apilogerror', type='string', length=15360, required=True, comment='Json del Error'),
                Field('apilogtimestamp', type='datetime', required=True, comment='Error Log Time Stamp'),
                Field('apilogidcontrib', type='string', length=15, required=True, comment='Id Contribuyente Aumoso'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_LOG']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APILOG',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiLog {e}')


     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Archivos Recibidos de Sucerp
     def tablaRecepcionArchivos(self):

         """
          DEFINITION OF THE FILE RECEPTION TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

          """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('archivorecibidoid', type='id', required=True, comment='Id'),
                Field('archivonombre', unique=True, type='string', length=256, required=True, comment='Nombre Archivo'),
                Field('archivousercrt',   type='string', length=10,  required=True, comment='Archivo User Create'),
                Field('archivoprocesado', type='datetime', required=True, comment='Archivo Procesado'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_RECEPCIONARCHIVOS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'RECEPCIONARCHIVOS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiEstados {e}')



     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Tareas para Responder al Api
     def tablaApiTareas(self):

         """
          TASK API TABLE DEFINITION \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('apitareasid', type='id', required=True, comment='Id'),
                Field('apitareasdescripcion', unique=True, type='string', length=100, required=True, comment='Descr Token Api Tareas'),
                Field('apiusercrt',               type='string', length=10,   required=True, comment='Token Api User Create'),
                Field('tokenusercrttimestamp', type='datetime', required=True, comment='Token Api User Crt Time Stamp'),
                Field('apiuserdlt',               type='string', length=10,   required=True, comment='Token Api User Delete'),
                Field('tokenuserdlttimestamp', type='datetime', required=True, comment='Token Api User Dlt Time Stamp'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_TAREAS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APITAREAS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiTareas {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Estados Tareas para Responder al Api
     def tablaApiEstadosTareas(self):

         """
          DEFINITION OF THE API TABLE STATES TASKS \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('apiestadotareasid', type='id', required=True, comment='Id'),
                Field('apiestadosid', type='reference APIESTADOS', ondelete='CASCADE', comment='Id FK Token Api Estado'),
                Field('apitareasid', type='reference APITAREAS', ondelete='CASCADE', comment='Id FK Token Api Tareas'),
                Field('apiestadosnewid', type='reference APIESTADOS', ondelete='CASCADE', comment='Id FK Token Estado New'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_ESTADOS_TAREAS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APIESTADOSTAREAS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiEstadosTareas {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Token Registros para Responder al Api
     def tablaApiRegistros(self):

         """
          API TABLE DEFINITION REGISTERS \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()


             # fields list
             lista = [
                Field('apiregistrosid', type='id', required=True, comment='Id'),
                Field('apiregistrosdescripcion', unique=True, type='string', length=100, required=True, comment='Descr Token Api Registros'),
                Field('apiregistrosnumero', unique=True, type='integer', required=True, comment='Token Api Registros Nro'),
                Field('apiestadotareasid', type='reference APIESTADOSTAREAS', ondelete='CASCADE', comment='Id FK Token Api Estado Tareas'),
                Field('apiusercrt',               type='string', length=10,   required=True, comment='Token Api User Create'),
                Field('tokenusercrttimestamp', type='datetime', required=True, comment='Token Api User Crt Time Stamp'),
                Field('apiuserdlt',               type='string', length=10,   required=True, comment='Token Api User Delete'),
                Field('tokenuserdlttimestamp', type='datetime', required=True, comment='Token Api User Dlt Time Stamp'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_REGISTROS']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APIREGISTROS',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm
         except Exception as e:
             print(f'Error - tablaApiRegistros {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Token Usuario para Responder al Api
     def tablaApiTokenUser(self):

         """
          DEFINITION OF THE USERS API TOKEN TABLE \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()


             # fields list
             lista = [
                Field('apiuserid', type='id', comment='Id'),
                Field('apiusernombre', unique=True, type='string', length=10, required=True, comment='Token Api User Nombre'),
                Field('apiuserpass', type='password', length=10, required=True, comment='Token Api User Pass'),
                Field('apellidonombre', type='string', length=150, required=True, comment='Apellido y Nombre'),
                Field('apiuseremail', unique=True, type='string', length=256, required=True, comment='Token Api User Email'),
                Field('apiuserwhatsapp', unique=True, type='string', length=20, required=True, default='', comment='Token Api User Whatsapp'),
                Field('tipodocumentoid', type='reference TIPODOCUMENTO', ondelete='CASCADE', comment='Id FK Tipo Documento'),
                Field('numerodocumento', type='bigint',  comment='Nro Documento'),
                Field('apiregistrosid', type='reference APIREGISTROS', ondelete='CASCADE', comment='Id FK Token Api Registros'),
                Field('apiestadotareasid', type='reference APIESTADOSTAREAS', ondelete='CASCADE', comment='Id FK Token Api Estado Tareas'),
                Field('apiusercrt', type='string', length=10,   required=True, comment='Token Api User Create'),
                Field('tokenusercrttimestamp', type='datetime', comment='Token Api User Crt Time Stamp'),
                Field('apiuserdlt', type='string', length=10,   comment='Token Api User Delete'),
                Field('tokenuserdlttimestamp', type='datetime',  comment='Token Api User Dlt Time Stamp'),

             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_TOKEN_USER']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APITOKENUSER',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm
         except Exception as e:
             print(f'Error - tablaApiTokenUser {e}')

     # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     # Tabla de Control de Token para Responder al Api
     def tablaApiToken(self):

         """
          API TOKEN TABLE DEFINITION \n
         WE RETURN: \n
            TABLE NAME \n
            STRUCTURE FIELDS \n
            CONSTRUCTION ARGUMENTS \n

         """
         try:

             lista, primary, parm = list(), list(), dict()

             # fields list
             lista = [
                Field('tokenapiid', type='id',  comment='Id'),
                Field('tokenvalor', unique=True,  type='string', length=512,  required=True, comment='Token Valor'),
                Field('apiuserid', type='reference APITOKENUSER', ondelete='CASCADE', comment='Id FK Token Api User'),
                Field('tokentimestamp', type='datetime', required=True, comment='Token Time Stamp'),
                Field('apiregistrosid', type='reference APIREGISTROS', ondelete='CASCADE', comment='Id FK Token Api Registros'),
                Field('apiestadotareasid', type='reference APIESTADOSTAREAS', ondelete='CASCADE', comment='Id FK Token Api Estado Tareas'),
                Field('tokenconectar', type='boolean', required=True, default='0', comment='Token Conectar'),
                Field('tokeniniciotransaccion', type='boolean', required=True, default='0', comment='Token Inicio Transaccion'),
                Field('tokenfintransaccion', type='boolean', required=True, default='0', comment='Token Fin Transaccion'),
             ]

             # We get the migrate parameter
             migrate = ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_TOKEN']['migrate']

             # table construction parameters
             parm = {
                 'name': 'APITOKEN',
                 'fields': tuple(lista),
                 'arg': {'migrate': migrate},
                 'sqlfldtexto': True
             }

             return parm

         except Exception as e:
             print(f'Error - tablaApiToken {e}')
