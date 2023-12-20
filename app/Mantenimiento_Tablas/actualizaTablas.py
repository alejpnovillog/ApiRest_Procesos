# Clase de configuracion
from app_Config.config import ConfigurarAplicacion

# Gestion Registros
from app_Abstract.gestionRegistros import GestionRegistros



from app_Token.function_jwt import write_token, validate_token



#db = GestionRegistros(ambiente=api.ENV_GX)

# cargamos los campos del registros de la tabla log
campos_log = {
    "apilogerror": "holaMundo",
    "apilogtimestamp": "123456789",
    "apilogidcontrib": 1
}

print(campos_log)
tk = write_token(**campos_log)
print(tk)

new = str(tk, 'utf-8')

rtn, error = validate_token(token=new, output=False)
print(rtn, error)

# garbamos APILOG


#retorno = db.add_Dal(db.__getattribute__(api.LISTA_TABLAS['TABLA_API_LOG']['objeto']), **campos_log)
