try:
    import jpype
    import os
    import platform
    from app_Config.config import ConfigurarAplicacion    
    from com_ibm_as400_accees.as400 import AS400
    from com_ibm_as400_accees.user import User
    from com_ibm_as400_accees.job import Job

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

# asignamos los parametros recibidos
server = 'PUB400.COM'
username = 'anovillo'
pwd = 'macs6259'    


# determinamos en que plataforma estamos ejeutando el script
if platform.system() == 'Linux':

    # definimos el path la java virtual machine
    jvmpath = ConfigurarAplicacion.JVMPATH_LINUX
    # definimos el path del jt400
    jpype.addClassPath(ConfigurarAplicacion.ADDCLASSPATH_LINUX)

else:

    # definimos el path la java virtual machine
    jvmpath = ConfigurarAplicacion.JVMPATH_WINDOWS
    # definimos el path del jt400
    jpype.addClassPath(ConfigurarAplicacion.ADDCLASSPATH_WINDOWS)


#jarpath = r'C:\Users\anovillo\Desktop\Software\JtOpen\lib\jt400.jar'
jarpath = jpype.getClassPath()

# definimos donde se encuentra jt400
jvmArg = f'-Djava.class.path={jarpath}'

# arracamos la virtual machine
jpype.startJVM(jvmpath, jvmArg)

# asignamos el constructor del AS400 usuario y password
system = AS400(server, username, pwd)

print(system.getAs400systemname())
print(system.getAs400jobs(4))
print(system.getAs400version())



# asigno el constructor de User
#sysUser = User(system, username)

# asigno el constructor de Job
#sysJob = Job(system)


