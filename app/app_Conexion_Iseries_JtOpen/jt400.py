try:
    import jpype
    import os
    import platform
    from app_Config.config import ConfigurarAplicacion    
    from com_ibm_as400_accees.as400 import AS400
    from com_ibm_as400_accees.user import User
    from com_ibm_as400_accees.job import Job

except Exception as e:
    print(f'Falta algun modulo {e}')


class JT400(AS400, User, Job):

    """
    CALL  PGM(QCMD) para poder acceder sin restricciones de permisos
    """


    def __init__(self, server, username, pwd):

        """
        server    = Es la Ip del server
        username  = Es el usuario
        pwd       = Es la password  del usuario
        """

        self.registros = list()

        # asignamos los parametros recibidos
        self.server, self.username, self.pwd = server, username, pwd

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
        AS400.__init__(self, self.server, self.username, self.pwd)

        # asigno el constructor de User
        User.__init__(self, self.system, self.username)

        # asigno el constructor de Job
        Job.__init__(self, self.system)
