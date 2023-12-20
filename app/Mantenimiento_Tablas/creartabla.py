# Load las bibliotecas necesarias
try:

    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion
    
except Exception as e:
    print(f'Falta algun modulo {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Lista de tablas a crear
lista_tablas = [
    'TABLA_ESTADO',                             # False Tabla de referencia
    'TABLA_PROVINCIA',                          # False Tabla de referencia
    'TABLA_TIPO_CUERPO',                        # False Tabla de referencia
    'TABLA_TIPO_CUOTA',                         # False Tabla de referencia
    'TABLA_TIPO_DOCUMENTO',                     # False Tabla de referencia
    'TABLA_TIPO_MONEDA',                        # False Tabla de referencia
    'TABLA_TIPO_MOVIMIENTO',                    # False Tabla de referencia
    'TABLA_TIPO_ORIGEN',                        # False Tabla de referencia
    'TABLA_TIPO_PAGO',                          # False Tabla de referencia
    'TABLA_TIPO_REGISTRO',                      # False Tabla de referencia
    'TABLA_TIPO_SUB_REGISTRO',                  # False Tabla de referencia
    'TABLA_TIPO_TITULAR',                       # False Tabla de referencia
    'TABLA_API_ESTADOS',                        # False Tabla de referencia
    'TABLA_API_TAREAS',                         # False Tabla de referencia
    'TABLA_API_LOG',                            # False Tabla de referencia
    'TABLA_PROCESOIMPORTACIONEXPORTACION',      # False Tabla de referencia

    'TABLA_TIPO_VEHICULO',                      # False Tabla de referencia
    'TABLA_TIPO_TRAMITE',                       # False Tabla de referencia

    'TABLA_CATEGORIA',                          # True
    'TABLA_DETALLE_TIPO_TRAMITE',               # False
    'TABLA_API_ESTADOS_TAREAS',                 # False
    'TABLA_API_REGISTROS',                      # False
    'TABLA_API_TOKEN_USER',                     # False
    'TABLA_API_TOKEN',                          # False

    'TABLA_ALTAIMPOSITIVATITULAR',              # False
    'TABLA_ALTAIMPOSITIVA',                     # False
    'TABLA_API_AUMOSO',                         # False
    'TABLA_ANULACIONTRAMITESSELLOS',            # False ---
    'TABLA_ANULACIONTRAMITESSELLOSDETALLE',     # False
    'TABLA_BAJAIMPOSITIVATITULAR',              # False
    'TABLA_BAJAIMPOSITIVA',                     # False
    'TABLA_CAMBIOTITULARIDADTITULAR',           # False
    'TABLA_CAMBIOTITULARIDAD',                  # False
    'TABLA_ENCABEZADO',                         # False
    'TABLA_IMPUESTOAUTOMOTOR',                  # False
    'TABLA_IMPUESTOSELLOS',                     # False
    'TABLA_IMPUESTOSELLOSPARTES',               # False
    'TABLA_IMPUESTOSELLOSPARTESTIPOTRAMITE',    # False
    'TABLA_INFORMACIORADICACION',               # False
    'TABLA_INFORMACIONVEHICULO',                # False
    'TABLA_INFORMACIONVEHICULOTITULAR',         # False
    'TABLA_PIE',                                # False
    'TABLA_RELACION_ARBA_SUCERP_MARCA',         # False


]


# Obtengo el conector a la base de datos
data_Input = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_GX)

# inspeccionamos la lista

try:
        for elemento in lista_tablas:

            #data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS[elemento]['objeto'])
            valor  = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS[elemento]['objeto'])


            if ConfigurarAplicacion.ENV_GX in ConfigurarAplicacion.ENV_LABEL_ON:

                texto = ''

                # we iterate through the fields of the table record
                for x in range(0, len(valor._fields)):

                    # we build the text variable
                    texto += f'\"{valor._fields[x].lower()}\" text is \'{valor.__getattribute__(valor._fields[x]).comment}\''

                    if x != (len(valor._fields) - 1):
                        texto += ' ,'

                # we build the sentencia variable
                sentencia = f'LABEL ON COLUMN {valor._dalname} ({texto})'

                # execute the sql statement
                data_Input.db.executesql(sentencia)

                data_Input.db.commit()


            print(f'Nombre de la Tabla ({valor})')


except Exception as inst:
    print(inst)







