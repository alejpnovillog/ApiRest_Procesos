from app_Abstract.gestionRegistros import GestionRegistros
from app_Config.config import ConfigurarAplicacion
import datetime


impr = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_GX)
fmt = '%Y-%m-%d-%H.%M.%S.%f'
"""


# tablaApiRegistros
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.apiRegistros_Dal)



campos = {
    'apiregistrosdescripcion': 'pedidoconexion'.upper(),
    'apiregistronumero': 1,
    'apiusercrt': 'gxusr'.upper(),
    'tokenusercrttimestamp': datetime.datetime.now().strftime(fmt),
}

respuesta = impr.add_Dal(objetoTabla_Dal, **campos)
print(respuesta)

"""
# tablaApiTokenUser
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.apiTokenUser_Dal)

campos = {
    'apiusernombre'         : 'prueba'.upper(),
    'apiuserpass'           : 'pepe1234',
    'apellidonombre'        : 'prueba nombre'.upper(),
    'apiuseremail'          : 'pruebahotmail.com',
    'apiuserwhatsapp'       : '1523325075',
    'tipodocumentoid'       : 1,
    'numerodocumento'       : 1523325075,
    'apiregistrosid'        : 2,
    'apiusercrt'            : 'gxusr'.upper(),
    'tokenusercrttimestamp' : datetime.datetime.now().strftime(fmt)
}

respuesta = impr.add_Dal(objetoTabla_Dal, **campos)
print(respuesta)
