from app_Config import constantes
import datetime

from app_Abstract.gestionRegistros import GestionRegistros




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class BajaFiscalAutomotor():

    def __init__(self, impresionId = None, usuarioId = None):

        # Parametros
        self.__impresionId = impresionId
        self.__usuarioId   = usuarioId

        # Datos de Informacion
        self.__datosUsuariosDict = None
        self.__datosImpresionDict = None
        self.__datosAutomotorDict = None
        self.__datosFormulario = None

        # Respuesta de Error
        self.__respuesta = None

        # Id de TMAUT
        self.__id_Tmaut = None
        self.__motivo   = None


        # Objetos Conectores a DB
        self.__seg  = GestionRegistros(ambiente=constantes.VALIDATOR)
        self.__impr = GestionRegistros(ambiente=constantes.ENV_GX)
        self.__auto = GestionRegistros(ambiente=constantes.ENV_MATANZA)


        # Tratamiento de los Datos
        self.__tratamientoDatos()



    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Encapsulacion de los atributos

    #-------- impresionId --------------------------------------------
    @property
    def impresionId(self):
        return self.__impresionId

    @impresionId.setter
    def impresionId(self, valor):
        self.__impresionId = valor


    #---------usuarioId -------------------------------------------
    @property
    def usuarioId(self):
        return self.__usuarioId

    @usuarioId.setter
    def usuarioId(self, valor):
        self.__usuarioId = valor


    #---------respuesta -------------------------------------------
    @property
    def respuesta(self):
        return self.__respuesta

    @respuesta.setter
    def respuesta(self, valor):
        self.__respuesta = valor


    #---------datosFormulario -------------------------------------------
    @property
    def datosFormulario(self):
        return self.__datosFormulario

    @datosFormulario.setter
    def datosFormulario(self, valor):
        self.__datosFormulario = valor


    #---------datosUsuario -------------------------------------------
    @property
    def datosUsuariosDict(self):
        return self.__datosUsuariosDict

    @datosUsuariosDict.setter
    def datosUsuariosDict(self, valor):
        self.__datosUsuariosDict = valor


    # --------datosImpresionDict --------------------------------------------
    @property
    def datosImpresionDict(self):
        return self.__datosImpresionDict

    @datosImpresionDict.setter
    def datosImpresionDict(self, valor):
        self.__datosImpresionDict = valor


    # --------datosAutomotorDict --------------------------------------------
    @property
    def datosAutomotorDict(self):
        return self.__datosAutomotorDict

    @datosAutomotorDict.setter
    def datosAutomotorDict(self, valor):
        self.__datosAutomotorDict = valor


    #---------id_Tmaut -------------------------------------------
    @property
    def id_Tmaut(self):
        return self.__id_Tmaut

    @id_Tmaut.setter
    def id_Tmaut(self, valor):
        self.__id_Tmaut = valor

    #---------motivo -------------------------------------------
    @property
    def motivo(self):
        return self.__motivo

    @motivo.setter
    def motivo(self, valor):
        self.__motivo = valor



    # --------seg --------------------------------------------
    @property
    def seg(self):
        return self.__seg


    # --------impr --------------------------------------------
    @property
    def impr(self):
        return self.__impr


    # --------auto --------------------------------------------
    @property
    def auto(self):
        return self.__auto


    #***********************************************************************************************
    # Carga los Datos del Formulario
    def __loadDatosFormulario(self):

        self.ahora = datetime.datetime.now()
        self.pie = f"La Matanza, {self.ahora.strftime('%d/%m/%Y')} para constatar la veracidad de este documento enviar email a "
        self.pie += "descentralizada.automotor@lamatanza.gov.ar"
        self.fechaBaja = str(self.datosAutomotorDict['FEBAJA'])
        y = self.fechaBaja[0:4]
        m = self.fechaBaja[4:6]
        d = self.fechaBaja[6:]
        self.linea01 = f'Se deja constancia que con fecha, {d}/{m}/{y} se detecto la baja registral correspondiente al'
        self.linea02 = f'al dominio de referencia, habiendo abonado en esta Municipalidad hasta la fecha {d}/{m}/{y} '
        self.linea03 = 'se extiende la presente con el objeto de regularizar la situacion fiscal ante quie corresponda'
        calle   = self.datosAutomotorDict['CALFIS']
        nroCall = str(self.datosAutomotorDict['NROFIS'])
        piso    = str(self.datosAutomotorDict['PISFIS'])
        depto   = str(self.datosAutomotorDict['DEPFIS'])
        self.domicilio = str(f'{calle} {nroCall} {piso} {depto}')

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Estructura de Datos para la Pagina
        self.datosFormulario = {
            # Motivo de la Baja
            "motivo": self.motivo.strip(),

            # Dominio Original
            "dominioAnterior": self.datosAutomotorDict['DORIGI'],

            # Dominio Actual
            "dominioActual": self.datosAutomotorDict['DACTUA'],

            # Vehiculo Marca
            "vehiculomarca": self.datosAutomotorDict['DESMOD'],

            # Modelo Año
            "modeloaño": self.datosAutomotorDict['MODELO'],

            # Motor
            "motor": self.datosAutomotorDict['MARMOT'],

            # Motor Numero
            "numeromotor": self.datosAutomotorDict['NORMOT'],

            # Titular
            "titular": self.datosAutomotorDict['PROPIE'],

            # Domicilio
            "domicilio": self.domicilio,

            # Localidad
            "localidad": self.datosAutomotorDict['LOCFIS'],

            # Codigo Postal
            "codigopostal": self.datosAutomotorDict['CPFISC'],

            # Linea uno del detalle
            "linea01" : self.linea01,

            # Linea dos del detalle
            "linea02": self.linea02,

            # Linea tres del detalle
            "linea03": self.linea03,

            # Linea al Pie de Pagina
            "lineapie": self.pie

        }
        return self.datosFormulario, self.respuesta





    #***********************************************************************************************
    # Verifica si el Usuario existe
    def __verificaUsuario(self):

        # Obtengo los elementos para gestionar la Tabla de Automotores
        objetoSeg_Dal, campos, insert, update, delete = self.seg.get_Struct_Tabla(self.seg.sq_userPathFile_Dal)

        # Realizo la consulta al object_Dal y obtengo los registros en un diccionario
        self.datosUsuariosDict, self.respuesta = self.seg.get_Rows(objetoSeg_Dal, self.usuarioId)

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # Retorna el error al verificar el usuario
        if self.respuesta['error'] != None:

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # Arma el json del Error
            datos_api = {
                'error': respuesta['error'],
                'usuario': [self.usuarioId]
            }

            # Retorna informacion al cliente
            self.respuesta = datos_api

        else:

            # Recuperamos solo el diccionario del registro
            for l in self.datosUsuariosDict:
                for k, v in l.items():
                    self.datosUsuariosDict = v



    #***********************************************************************************************
    # Obtengo los Datos de Impresion
    def __obtengoDatosImpresion(self):

        # Obtengo los elementos para gestionar la tabla de Impresiones
        objetoImpr_Dal, campos, insert, update, delete = self.impr.get_Struct_Tabla(self.impr.impresionPdf_Dal)

        # Realizo la consulta al objeto_Dal y obtendo los registros de un diccionario
        self.datosImpresionDict, self.respuesta = self.impr.get_Rows(objetoImpr_Dal, self.impresionId)


        # Retorna el error del acceso a las Impresiones
        if self.respuesta['error'] != None:
            # Arma el json del Error
            datos_api = {
                'error': respuesta['error'],
                'identificador': [self.impresionId]
            }

            # Retorna informacion al cliente
            self.respuesta = datos_api

        else:

            # Recuperamos solo el diccionario del registro
            for l in self.datosImpresionDict:
                for k, v in l.items():
                    registro = v

            # obtengo el campo IMPRESIOPRMUNO  de la tabla IMPRESIONPDF
            impresionPrmUno = registro['IMPRESIONPRMUNO']

            self.id_Tmaut =   impresionPrmUno[50:65]
            self.motivo   =   impresionPrmUno[65:97]


    #***********************************************************************************************
    # Obtengo los Datos del Automotor
    def __obtengoDatosAutomotor(self):

        # Obtengo los elementos para gestionar la tabla de Impresiones
        objetoAuto_Dal, campos, insert, update, delete = self.auto.get_Struct_Tabla(self.auto.tmAut_Dal)

        # Realizo la consulta al objeto_Dal y obtendo los registros de un diccionario
        key = self.id_Tmaut
        self.datosAutomotorDict, self.respuesta = self.auto.get_Rows(objetoAuto_Dal, key)


        # Retorna el error del acceso a los datos del automotor
        if self.respuesta['error'] != None:

            # Arma el json del Error
            datos_api = {
                'error': respuesta['error'],
                'identificador': [self.id_Tmaut]
            }

            self.respuesta = datos_api

        else:

            # Recuperamos solo el diccionario del registro
            for  l in self.datosAutomotorDict:
                for k, v in l.items():
                    self.datosAutomotorDict = v


    #***********************************************************************************************
    # Funcion de Tratamiento de datos
    def __tratamientoDatos(self):

        # Realiza la verificacion del usuario
        self.__verificaUsuario()
        if self.respuesta['error'] !=  None:
            self.respuesta = {'respuesta': self.respuesta, 'datos': None}

        # Recuperamos los datos de la Impresion
        self.__obtengoDatosImpresion()
        if self.respuesta['error'] !=  None:
            self.respuesta = {'respuesta': self.respuesta, 'datos': None}

        # Recuperamos los datos del Automotor
        self.__obtengoDatosAutomotor()
        if self.respuesta['error'] !=  None:
            self.respuesta = {'respuesta': self.respuesta, 'datos': None}

        # Recuperamos los datos para el formulario
        self.__loadDatosFormulario()
        if self.respuesta['error'] !=  None:
            self.respuesta = {'respuesta': self.respuesta, 'datos': None}
        else:
            self.respuesta = {'respuesta': self.respuesta, 'datos':  self.datosFormulario}




