# Load las bibliotecas necesarias
try:
    import datetime
    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Lista de tablas a crear
lista_tablas = [
     'TABLA_ESTADO',
     'TABLA_PROVINCIA',
     'TABLA_TIPO_CUERPO',
     'TABLA_TIPO_CUOTA',
     'TABLA_TIPO_DOCUMENTO',
     'TABLA_TIPO_MONEDA',
     'TABLA_TIPO_MOVIMIENTO',
     'TABLA_TIPO_ORIGEN',
     'TABLA_TIPO_PAGO',
     'TABLA_TIPO_REGISTRO',
     'TABLA_TIPO_SUB_REGISTRO',
     'TABLA_TIPO_TITULAR',
     'TABLA_API_TOKEN_USER',
     'TABLA_API_ESTADOS',
     'TABLA_API_TAREAS',
     'TABLA_API_ESTADOS_TAREAS',
     'TABLA_API_TOKEN',
     'TABLA_API_AUMOSO',
     'TABLA_API_REGISTROS',
     'TABLA_ALTAIMPOSITIVA',
     'TABLA_ALTAIMPOSITIVATITULAR',
     'TABLA_ANULACIONTRAMITESSELLOS',
     'TABLA_ANULACIONTRAMITESSELLOSDETALLE',
     'TABLA_BAJAIMPOSITIVA',
     'TABLA_BAJAIMPOSITIVATITULAR',
     'TABLA_CAMBIOTITULARIDAD',
     'TABLA_CAMBIOTITULARIDADTITULAR',
     'TABLA_ENCABEZADO',
     'TABLA_IMPUESTOAUTOMOTOR',
     'TABLA_IMPUESTOSELLOS',
     'TABLA_IMPUESTOSELLOSPARTES',
     'TABLA_IMPUESTOSELLOSPARTESTIPOTRAMITE',
     'TABLA_INFORMACIONVEHICULO',
     'TABLA_INFORMACIONVEHICULOTITULAR',
     'TABLA_INFORMACIORADICACION',
     'TABLA_PIE',
     'TABLA_RELACION_ARBA_SUCERP_MARCA',
     'TABLA_PROCESOIMPORTACIONEXPORTACION'
]

# Obtengo el conector a la base de datos
data_Input = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_GX)

# inspeccionamos la lista

try:

    proceso = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS['TABLA_PROCESOIMPORTACIONEXPORTACION']['objeto'])
    objeto_Dal, campos_prc, insert, update, delete = data_Input.get_Struct_Tabla(proceso)

    for elemento in lista_tablas:


        valor = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS[elemento]['objeto'])
        tabla = ConfigurarAplicacion.LISTA_TABLAS[elemento]['numero']

        if proceso != valor:

            #campos = insert['datos']
            #campos['procesoid'] = ''
            campos = {
                #'procesoid': 1,
                'procesocodigotabla' : tabla,
                'procesonombretabla': valor._dalname,
                'procesotransferencia': None,
                #'procesofechatransferencia': None,
                'procesobasedatos': None,
                #'procesofechabasedatos': None,
                'procesoaccion': None
            }

            data_Input.add_Dal(proceso, **campos)

            print(f'Nombre de la Tabla ({valor})')


except Exception as inst:
    print(inst)
