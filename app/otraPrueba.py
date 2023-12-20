try:

    from pydal.objects import Table

    # Clase de configuracion
    from app_Config.config import ConfigurarAplicacion

    # Gestion Registros
    from app_Abstract.gestionRegistros import GestionRegistros


except Exception as e:
    print(f'Falta algun modulo {e}')



# ------------------- recuperamos el ambiente ------------------------------------------------------------------
api = ConfigurarAplicacion()
db = GestionRegistros(ambiente=api.ENV_GX)
print('llego')
