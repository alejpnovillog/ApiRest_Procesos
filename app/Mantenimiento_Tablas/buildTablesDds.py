try:
    from app_Conexion_Iseries_JtOpen.pythonJTOpen import JT400Helper
    from app_Abstract.gestionRegistros import GestionRegistros
    import os
    from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# verificacion, creacion , limpieza de los registros de las tablas de la lista de tablas
def controlTablas(tablas, iprod):
    """
    Objetivo:  Es verificar si las DDS existe
               Es crear la tabla si las DDS existen
               Es limpiar la tabla si la tabla existe
    tablas = Es una lista de las tablas controlar
    iprod  = es el objeto de conexion a la iseries para ejecutar los comandos
    msg    = Es la respuesta de la ejecucion del comando donde
             msg[0] Los valores posibles es True o False
             msg[1] en adelante tenemos los mensajes que respondio el os400 ...
    return = msg
    """

    tablas = tablas

    # navegamos por el diccionario
    for elemento in tablas:

        lib = elemento["lib"]
        file = elemento["file"]
        src = elemento["src"]


        # verificamos si el fuente existe
        str = f'CHKOBJ OBJ({lib}/QDDSSRC) OBJTYPE(*FILE) MBR({file})'

        # ejecutamos el comando
        msg = iprod.GetCmdMsg(str)

        # verificamos si el fuente existe
        if not msg[0]:
            for error in msg:
                print(error)

        # si existe el fuente
        else:

            # verificamos si el objeto existe
            msg = iprod.CheckObjExists(lib, file, type="*FILE")

            # si no lo encuentra
            if not msg[0]:
                str = f'CRTPF FILE({elemento["lib"]}/{elemento["file"]}) SRCFILE({elemento["lib"]}/{elemento["src"]})'

                # creamos la tabla
                msg = iprod.GetCmdMsg(str)

                # si no hay error
                if msg[0]:
                    print(f'Tabla {file} creada...')
            else:
                str = f'CLRPFM FILE({elemento["lib"]}/{elemento["file"]})'

                # eliminamos registros de la tabla
                msg = iprod.GetCmdMsg(str)

                # si no hay error
                if msg[0]:
                    print(f'Tabla {file} eliminamos los registros...')
                else:
                    print(f'Tabla {file} ERROR...')
                    for error in msg:
                        print(error)
    return msg



data_Input_Dds = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_DDS)
con = data_Input_Dds.__getattribute__('instancia_Host_Input_Dict')
iprod = JT400Helper(con['ip'], con['usuario'], con['password'])

# cargamos la lista de las tablas a controlar
tablas = list()
tablas.append({'lib':'epagos', 'file':'INFOR00001', 'src':'QDDSSRC' })
tablas.append({'lib':'epagos', 'file':'INFOR00002', 'src':'QDDSSRC' })
print(controlTablas(tablas, iprod))
