# Load las bibliotecas necesarias
try:
    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion
    import os
    import datetime

except Exception as e:
    print(f'Falta algun modulo {e}')


# definimos la conexion de datos ------------------
data_Input = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_SOURCE)

# obtenemos el idTabla  y el objeto_dal de TABLA_ENCABEZADO -------------------
objetoEncabezado = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_ENCABEZADO']['objeto'])

tabla = data_Input.tipoDocumento_Dal



maximo = data_Input.db().select(tabla.tipodocumentoid.max())
print(maximo.response[0][0])
# contar = data_Input.db(tabla.desctipodocumento).count()


#print(maximo, contar)
