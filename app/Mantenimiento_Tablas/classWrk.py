from app_Config import constantes
from app_Abstract.gestionRegistros import GestionRegistros

#from abmProvincias import AbmProvincias
from abmTipoDocumento import AbmTipoDocumento
from abmTipoMoneda import AbmTipoMoneda
from abmTipoPago import AbmTipoPago
from abmTipoCuota import AbmTipoCuota
from abmTipoMovimiento import AbmTipoMovimiento
from abmTipoCuerpo import AbmTipoCuerpo
from abmTipoOrigen import AbmTipoOrigen
#from abmEstado import AbmEstado
from abmTipoRegistro import AbmTipoRegistro
from abmTipoSubRegistro import AbmTipoSubRegistro
from abmTipoTitular import AbmTipoTitular
from abmTokenRegistros import AbmTokenRegistros
from abmTokenUser import AbmTokenUser
from app_Abstract.classAbm import AbmTablas

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkEstado(AbmTablas):

    """
    LA CLASE TRABAJA CON LA TABLA ESTADO\n
    Las posibilidades de la clase es poder realizar las siguientes tareas\n

    Insert un nuevo registro con el metodo insertRecord\n
    Update un registro con el metodo updateRecord\n

    Obtener una consulta exacta de un registro con el metodo getRecord
    Obtener una consulta de varios registros con el metodo getRecordWhere\n

    Tiene los siguientes atributos\n

    campos : es un dict con los campos que componen el registro de la tabla\n
    insert : es un dict con los campos a insertar en la tabla\n
    update : es un dict con la clave de acceso a la tabla y los campos a actualizar\n
    delete : es un dict con la clave de acceso a la tabla para eliminar el registro\n

    """

    def __init__(self):

        # se obtiene el ambiente en donde reside la tabla
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)

        # se obtiene los atributos de la tabla de estado
        self.__objeto_Dal, self.__campos, self.__insert, self.__update, self.__delete = \
            self.__ges.get_Struct_Tabla(self.__ges.estado_Dal)

        argumentos = {
            'ges'           : self.__ges,
            'objeto_dal'    : self.__objeto_Dal,
            'campos'        : self.__campos,
            'insert'        : self.__insert,
            'update'        : self.__update,
            'delete'        : self.__delete
        }

        # se inicializa el constructor de la clase heredara
        AbmTablas.__init__(self, **argumentos)


    """
    @property
    def campos(self):
        return self.__campos

    @property
    def insert(self):
        return self.__insert

    @property
    def update(self):
        return self.__update

    @property
    def delete(self):
        return self.__delete

    """




#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkProvincia(AbmTablas):

    def __init__(self):

        #self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)

        argumentos = {
            'ges'           : constantes.ENV_GX,
            'objeto_dal'    : self.__ges.provincias_Dal,
        }


        # se inicializa el constructor de la clase heredara
        AbmTablas.__init__(self, **argumentos)







#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkTipoCuerpo(AbmTipoCuerpo):

    def __init__(self, **consulta):
        self.__consulta = consulta
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)
        AbmTipoCuerpo.__init__(self,  ambiente=self.__ges, **self.__consulta)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkTipoCuota(AbmTipoCuota):

    def __init__(self, **consulta):
        self.__consulta = consulta
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)
        AbmTipoCuota.__init__(self,  ambiente=self.__ges, **self.__consulta)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkTipoPago(AbmTipoPago):

    def __init__(self, **consulta):
        self.__consulta = consulta
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)
        AbmTipoPago.__init__(self,  ambiente=self.__ges, **self.__consulta)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkTipoDocumento(AbmTipoDocumento):


    def __init__(self, **consulta):
        self.__consulta = consulta
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)
        AbmTipoDocumento.__init__(self,  ambiente=self.__ges, **self.__consulta)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkTipoMoneda(AbmTipoMoneda):

    def __init__(self, **consulta):
        self.__consulta = consulta
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)
        AbmTipoMoneda.__init__(self,  ambiente=self.__ges, **self.__consulta)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkTipoMovimiento(AbmTipoMovimiento):

    def __init__(self, **consulta):
        self.__consulta = consulta
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)
        AbmTipoMovimiento.__init__(self,  ambiente=self.__ges, **self.__consulta)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkTipoOrigen(AbmTipoOrigen):

    def __init__(self, **consulta):
        self.__consulta = consulta
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)
        AbmTipoOrigen.__init__(self,  ambiente=self.__ges, **self.__consulta)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkTipoRegistro(AbmTipoRegistro):

    def __init__(self, **consulta):
        self.__consulta = consulta
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)
        AbmTipoRegistro.__init__(self,  ambiente=self.__ges, **self.__consulta)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkTipoSubRegistro(AbmTipoSubRegistro):

    def __init__(self, **consulta):
        self.__consulta = consulta
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)
        AbmTipoSubRegistro.__init__(self,  ambiente=self.__ges, **self.__consulta)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkTipoTitular(AbmTipoTitular):

    def __init__(self, **consulta):
        self.__consulta = consulta
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)
        AbmTipoTitular.__init__(self,  ambiente=self.__ges, **self.__consulta)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkTokenRegistros(AbmTokenRegistros):

    def __init__(self, **consulta):
        self.__consulta = consulta
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)
        AbmTokenRegistros.__init__(self,  ambiente=self.__ges, **self.__consulta)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
class WrkTokenUser(AbmTokenUser):

    def __init__(self, **consulta):
        self.__consulta = consulta
        self.__ges      = GestionRegistros(ambiente=constantes.ENV_GX)
        AbmTokenUser.__init__(self,  ambiente=self.__ges, **self.__consulta)
