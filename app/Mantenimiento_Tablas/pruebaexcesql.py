try:
    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion
    import os
    import datetime

except Exception as e:
    print(f'Falta algun modulo {e}')

# definimos la conexion de datos ------------------
data_Input = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_GX)

sql = 'select max(infvehiculoid) from "INFORMACIONVEHICULO"'

valor = data_Input.run_comando(sql)

print(valor)
