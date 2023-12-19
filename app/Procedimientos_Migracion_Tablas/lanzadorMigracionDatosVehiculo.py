# We load the necessary libraries
try:
    from app_Migraciones.migracionDatosVehiculos import DatosVehiculos
    from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')


#archivo_texto = "2481cfcc14ab493c51b9a4d02567bac1FIJO.txt"
#archivo_texto = "2481cfcc14ab493c51b9a4d02567bac1PRUEBA.txt"

# We assign the parameters of the DataVehicle class
envdds = ConfigurarAplicacion.ENV_DDS
envsql = ConfigurarAplicacion.ENV_GX
archivotexto = "2481cfcc14ab493c51b9a4d02567bac1FIJO.txt"
encoding = 'latin-1'

# We generate an instance of the Vehicle Data class
datos = DatosVehiculos(envdds, envsql, archivotexto, encoding)

# we process the migration
datos.procesamiento()

