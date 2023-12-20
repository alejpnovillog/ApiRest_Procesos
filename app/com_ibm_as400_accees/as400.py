
# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Definimos la clase para manejar la iseries
class AS400():

    AUTHENTICATION_SCHEME_GSS_TOKEN = 1
    AUTHENTICATION_SCHEME_IDENTITY_TOKEN = 3
    AUTHENTICATION_SCHEME_PASSWORD = 0
    AUTHENTICATION_SCHEME_PROFILE_TOKEN = 2
    CENTRAL = 6
    COMMAND = 2
    DATABASE = 4
    DATAQUEUE = 3
    FILE = 0
    GSS_OPTION_FALLBACK = 1
    GSS_OPTION_MANDATORY = 0
    GSS_OPTION_NONE = 2
    PRINT = 1
    RECORDACCESS = 5
    SIGNON = 7
    USE_PORT_MAPPER  = - 1


    def __init__( self, server, username, pwd):


        """
        server          - Es la direccion ip del servidor\n
        username        - Nombre del usuario\n
        pwd             - password\n

        documentacion
        https://www.ibm.com/docs/ja/i/7.2?topic=ssw_ibm_i_72/rzahh/javadoc/com/ibm/as400/access/package-summary.html\n

        """

        # asigno la clase Java
        self.iseries = jpype.JClass('com.ibm.as400.access.AS400')

        # La interfaz ConnectionListener proporciona una interfaz
        # de escucha para recibir eventos de conexión.
        self.eventListener = jpype.JClass('java.util.EventListener')

        # realiza la conexion con la clase Java
        self.system = self.iseries(server, username, pwd)


    # ***
    # Agrega un agente de escucha para recibir una notificación
    # cuando se produzca un evento de conexión.
    def addAs400ConnectionListener(self, eventListener):
        """
            Agrega un agente de escucha para recibir una notificación\n
            cuando se produzca un evento de conexión.\n

            parametro eventListener\n

            por error utilizar el objeto AS400SecurityException\n
        """

    # ***
    # Valida el ID de usuario y la contraseña y, si tiene éxito,
    def addAs400PasswordCacheEntry(self, system, usuario, password):
        """
            Valida el ID de usuario y la contraseña y, si tiene éxito,\n
            agrega la información a la caché de contraseñas.\n

            parametros\n
                string system\n
                string usuario\n
                string password\n

            por error utilizar el objeto AS400SecurityException\n

        """


    # Agrega un oyente para recibir una notificación cuando se cambia el valor de
    def addAs400VetoableChangeListener(self, eventListener):
        """
            Agrega un oyente para recibir una notificación cuando se cambia el valor de\n
            cualquier propiedad restringida. Se llamará al método vetoableChange.\n

            parametro eventListener\n

        """

    # ***
    # Indica si las propiedades están congeladas. Si esto es cierto, no se deben realizar
    def areAs400PropertiesFrozen(self)-> bool:


        """
            Indica si las propiedades están congeladas. Si esto es cierto, no se deben realizar\n
            cambios de propiedad. Las propiedades no son lo mismo que los atributos.\n
            Las propiedades son piezas básicas de información que se deben establecer para\n
            que el objeto se pueda utilizar, como el nombre del sistema,\n
            el ID de usuario u otras propiedades que identifican el recurso.\n

            return  boolean(True, False)\n
            True si las propiedades están congeladas,\n
            False en caso contrario.\n


        """
        return self.system.arePropertiesFrozen()


    # ***
    # Autentica el nombre del perfil de usuario y la contraseña del perfil de usuario.
    def authenticateAs400(self, usuario: str, password: str)-> bool:

        """
            Autentica el nombre del perfil de usuario y la contraseña del perfil de usuario.\n
            Este método es funcionalmente equivalente al método validateSignon() .\n
            No altera el perfil de usuario asignado a este objeto, no afecta el estado de las\n
            conexiones existentes ni afecta al usuario ni a las autoridades en las que se\n
            ejecuta la aplicación.\n

            El nombre del sistema debe establecerse antes de llamar a este método.\n

            Nota: Proporcionar una contraseña incorrecta aumenta el número de intentos\n
            fallidos de inicio de sesión para el perfil de usuario y puede provocar que el perfil se deshabilite.\n

            Nota: Esto devolverá verdadero si la información se valida con éxito.\n
            Una validación fallida hará que se lance una excepción, nunca se devuelve falso.\n

            parametros\n
                string usuario\n
                string password\n

            return  boolena(True, False)\n
            True si tiene éxito.\n
        """
        return self.system.authenticate(usuario, password)


    # ***
    # Indica si este objeto AS400 está habilitado para aprovechar las optimizaciones nativas de Toolbox.
    def canAs400UseNativeOptimizations(self)-> bool:
        """
            Indica si este objeto AS400 está habilitado para aprovechar las optimizaciones nativas de Toolbox.\n
            Esto requiere que las clases de optimización nativas estén disponibles en el classpath,\n
            y este objeto AS400 representa el sistema local y está configurado para permitir que se\n
            utilicen las optimizaciones nativas. Nota: si el esquema de autenticación es distinto de\n
            AUTHENTICATION_SCHEME_PASSWORD, no se utilizarán las optimizaciones nativas.\n

            return boolean(True, False)
            True if the native optimizations can be used;\n
            False otherwise.\n

        """
        return self.system.canUseNativeOptimizations()


    # ***
    # Cambia la contraseña del perfil de usuario. El nombre del sistema y el nombre
    def changeAs400Password(self, oldpassword: str, newpassword: str):

        """
            Cambia la contraseña del perfil de usuario. El nombre del sistema y el nombre\n
             del perfil de usuario deben configurarse antes de llamar a este método.\n

            parametro
                oldpassword- La contraseña del perfil de usuario anterior.\n
                newpassword- La contraseña del nuevo perfil de usuario.\n

            return boolean(True, False)

        """
        self.system.changePassword(oldpassword, newpassword)


    # ***
    # Se conecta a un servicio. Se valida la seguridad y se establece una conexión.
    def connectAs400Service(self, servicio: int):

        """
            Se conecta a un servicio. Se valida la seguridad y se establece una conexión.

            Los servicios normalmente se conectan implícitamente; por lo tanto, no es necesario llamar a este método para utilizar un servicio. Este método se puede utilizar para controlar cuándo se establece la conexión.

            Parámetros:  service- El nombre del servicio. Los servicios válidos son:
                    FILE- Clases de archivos IFS.
                    PRINT- clases de impresión.
                    COMMAND- Clases de llamadas a comandos y programas.
                    DATAQUEUE- clases de cola de datos.
                    DATABASE- Clases JDBC.
                    RECORDACCESS- Clases de acceso a nivel de registro.
                    CENTRAL- Clases de gestión de licencias.
                    SIGNON- Clases de inicio de sesión.

        """
        self.system.connectService(servicio)


    # ***
    # obtiene  el nombre de la base de datos en una conexion DDM
    def getAs400ddmrdb(self)-> str:
        """
        retorna un string con el nombre de la base de datos en una conexion DDM\n

        """
        return self.system.getDDMRDB()


    # ***
    # obtiene la Version el Release y la Modificacion del OS400
    def getAs400vrm(self)-> int:
        return self.system.getVRM()

    # ***
    # obtiene la autenticacion del schema
    def getAs400authenticationscheme(self)-> str:
        """
        returna un string con los siguientes valores\n
        0 = AUTHENTICATION_SCHEME_PASSWORD\n
        1 = 	AUTHENTICATION_SCHEME_GSS_TOKEN\n
        3 = AUTHENTICATION_SCHEME_IDENTITY_TOKEN\n
        2 = AUTHENTICATION_SCHEME_PROFILE_TOKEN\n

        """

        if self.system.getAuthenticationScheme() == 0: return 'AUTHENTICATION_SCHEME_PASSWORD'
        if self.system.getAuthenticationScheme() == 1: return 'AUTHENTICATION_SCHEME_GSS_TOKEN'
        if self.system.getAuthenticationScheme() == 3: return 'AUTHENTICATION_SCHEME_IDENTITY_TOKEN'
        if self.system.getAuthenticationScheme() == 2: return 'AUTHENTICATION_SCHEME_PROFILE_TOKEN'


    # ***
    # returnamos el codigo CCSID
    def getAs400ccsid(self)-> int:
        """
        retorna un integer con el codigo CCSID que esta asociado en el perfil del usuario
        """
        return self.system.getCcsid()

    # ***
    # retornamos el default time zone
    def getAs400defaulttimezone(self):
        return self.system.getDefaultTimeZone(self.system)

    # ***
    # retornamos el ID del user
    def getAs400userid(self)-> str:
        """
        retorna un string con el valor del userid
        """
        return self.system.getUserId()


    # ***
    # retornamos la Version del sistema operativo
    def getAs400version(self)-> int:
        """
        retorna un integer con el valor de la version del OS iseries
        """
        return self.system.getVersion()


    # ***
    # obtenemos el nombre del sistema
    def getAs400systemname(self)->  str:
        """
        retorna un string con el nombre del sistema
        """
        return self.system.getSystemName()


    #  ***
    # obtenemos el port del servicio de la Iseries
    def getAs400serviceport(self, service: int)-> int:
        """
        Codigos de los servicios
        0 = FILE
        1 = PRINT
        2 = COMMAND
        3 = DATAQUEUE
        4 = DATABASE
        5 = RECORDACCESS
        6 = CENTRAL
        7 = SIGNON
        """

        return self.system.getServicePort(service)


    # ***
    # obtenemos el release del iseries
    def getAs400release(self)-> int:

        """
        Retorna el Realease de Sistema OS 400
        """

        return self.system.getRelease()


    # ***
    # obtenemos el proxy server
    def getAs400proxyserver(self)-> str:

        """
        Retorna el Proxy Server
        """

        return self.system.getProxyServer()


    # ***
    # obtenemos cuando expira la password del perfil de usuario en dias
    def getAs400passwordexpirationwarningdays(self)-> int:

        """
        Retorna cuantos dias falta para que expire la password del usuario
        y empiece a advertir al usuario
        """
        return self.system.getPasswordExpirationWarningDays()


    # ***
    # obtenemos la cantidad de dias que faltan para caducar el perfil
    def getAs400passwordexpirationDate(self):
        """
        Retorna cuantos dias falta para que expire la password del usuario
        """
        return self.system.getPasswordExpirationDate()


    # ***
    # obtenemos el default user
    def getAs400defaultuser(self)-> str:
        """
        retorna un string
        Devuelve el ID de usuario predeterminado para este nombre de sistema.
        Este ID de usuario se usa para conectarse si no se usó un ID de usuario para construir el objeto.
        """

        return self.system.getDefaultUser(self.getsystemname())


    # ***
    # obtenemos el nombre GSS
    def getAs400gssname(self)-> str:
        """
        retorna un string
        """
        return self.system.getGSSName()


    # ***
    # obtenemos la opción de cómo se utilizará el marco JGSS.
    def getAs400gssoption(self)-> int:
        """
        retorna un integer
        """
        return self.system.getGSSOption()


    # ***
    # obtenemos una lista de los job asociados a un servicio
    def getAs400jobs(self, servicio: int)-> list:

        """
        retorna una lista con los job de un determinado servicio
        """

        #lista = list()

        #for elementoJob in self.system.getJobs(servicio):

            #job = Job(elementoJob)

            #print(job.getName())
            #pepe = job.getJobAccountingCode()
            #print(len(pepe))
            #print(f'Obtenemos el Job Accounting Code = {job.getJobAccountingCode()} ')
            #print(job.getAuxiliaryIORequests(job.AUXILIARY_IO_REQUESTS))
            #print(job.getJobActiveDate())


        return self.system.getJobs(servicio)


    # ***
    # Verificación si esta conectado cualquier o un servicio
    def isConnectedAs400(self, servicio: int = None)->  bool:
        """
            servicio (int, optional): _description_. Defaults to None.

        Returns:
            bool: _description_

        """

        if servicio != None:
            return self.system.isConnected(servicio)
        else:
            return self.system.isConnected()










