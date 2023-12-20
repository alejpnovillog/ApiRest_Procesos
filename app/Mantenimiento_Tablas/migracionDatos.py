try:
    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion
    from app_Request import classRequestMigracionSource, classRequestMigracionTarget

except Exception as e:
    print(f'Falta algun modulo {e}')

# definimos el gestor de tablas del ambiente source
data_Input = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_SOURCE)

# definimos el gestor de tablas del ambiente destino
data_Output = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_TARGET)

# definimos un lista de las tablas a migrar
lista_migrar = [
    #ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_REGISTROS']
    #ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_TAREAS'],
    #ConfigurarAplicacion.LISTA_TABLAS['TABLA_TIPO_DOCUMENTO'],
    #ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_TOKEN_USER'],
    #ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_TOKEN'],
    ConfigurarAplicacion.LISTA_TABLAS['TABLA_API_AUMOSO']

    ]

# Recupera todos los registros
# id del registro de la tabla
id = 0

# el id de un qry especifico
qry = 0

# recorremos la lista de tablas a migrar
for elemento_migrar in lista_migrar:

    # obtengo el numero de la tabla
    idTabla = elemento_migrar['numero']

    # obtengo el objeto tabla
    objetotabla = data_Output.__getattribute__(elemento_migrar['objeto'])

    # Recuperamos los registros del ambiente source
    data_list, errores = classRequestMigracionSource.requestWrk(id, qry, idTabla)


    # Recupereamos estructuras de la Tabla
    objetoTabla_Dal, campos, insert, update, delete = data_Output.get_Struct_Tabla(objetotabla)


    # Recorremos la lista de los registros obtenidos de la tabla origen
    for elemento in data_list:

        # Recorremos el diccionario
        for k, valor in elemento.items():

            # Completamos el diccionario insert
            if k in insert['datos']:
                insert['datos'][k] = elemento[k]

        # Generamos el registro en la tabla target
        errores = classRequestMigracionTarget.requestAdd(idTabla, **insert['datos'])


print('llegue')
