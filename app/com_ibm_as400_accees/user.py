# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        from com_ibm_as400_accees.directoryentry import DirectoryEntry

except Exception as e:
    print(f'Falta algun modulo {e}')



class User(DirectoryEntry):
    # Atributos
    NONE  =  "*NONE"
    SPECIAL_AUTHORITY_ALL_OBJECT = "*ALLOBJ"
    SPECIAL_AUTHORITY_AUDIT = "*AUDIT"
    SPECIAL_AUTHORITY_IO_SYSTEM_CONFIGURATION  = "*IOSYSCFG"
    SPECIAL_AUTHORITY_JOB_CONTROL = "*JOBCTL"
    SPECIAL_AUTHORITY_SAVE_SYSTEM = "*SAVSYS"
    SPECIAL_AUTHORITY_SECURITY_ADMINISTRATOR  = "*SECADM"
    SPECIAL_AUTHORITY_SERVICE = "*SERVICE"
    SPECIAL_AUTHORITY_SPOOL_CONTROL = "*SPLCTL"

    # Constructor
    def __init__(self, system, user):

        """
        Hereda :
            DirectoryEntry

        Metodos:

            addPropertyChangeListener(PropertyChangeListener listener)
                Agrega un PropertyChangeListener.

            addVetoableChangeListener(VetoableChangeListener listener)
                Agrega un VetoableChangeListener.


            DirectoryEntry = getDirectoryEntry()
                Recupera la entrada del directorio de distribución del sistema
                para el perfil de usuario, si existe.


            lista String[] = 	getDLOObjectTypesInSTRAUTCOL()

            lista String[] = getFileSystemObjectTypesInSTRAUTCOL()

            lista String[] = getLibNameInSTRAUTCOL()

            lista String[] = getLocaleJobAttributes()
                Recupera una lista de los atributos del trabajo que se establecen
                a partir del nombre de la ruta del entorno local del usuario.

            long = getMaximumStorageAllowedInLong()


            lista String[] = getObjectNamesInSTRAUTCOL()

           (ver)UserObjectsOwnedList = getObjectsOwned()
                Devuelve un objeto que representa los objetos que posee este usuario.

           lista String[] = getObjectTypesInSTRAUTCOL()

           lista String[] = getOmitLibNamesInSTRAUTCOL()















        boolean = hasSpecialAuthority(String authority)
                Recupera si a este perfil de usuario se le ha otorgado la autoridad especificada,
                o si pertenece a un perfil de grupo al que se le ha otorgado la autoridad especificada.

        boolean = isAuthCollectionActive()

        boolean	 = isAuthCollectionDeleted()

        boolean	 = isAuthCollectionRepositoryExist()

        boolean	 = isGroupHasMember()
                Recupera si este usuario es un grupo que tiene miembros.

        boolean = isLocalPasswordManagement()
                Recupera si la contraseña se administra localmente.

        boolean = isNoPassword()
                Recupera si se especifica *NONE para la contraseña en el perfil de usuario.

        boolean	 = isPasswordSetExpire()
                Recupera si la contraseña del usuario está configurada como caducada,
                lo que requiere que el usuario cambie la contraseña al iniciar sesión.

        boolean = isUserEntitlementRequired()
                Recupera si se requiere un derecho de usuario para este perfil de usuario.

        boolean = isWithDigitalCertificates()
                Recupera si existen certificados digitales asociados a este usuario.

        loadUserInformation()
                Actualiza los valores de todos los atributos.

        refresh()
                Actualiza todos los valores de atributo para este objeto de Usuario
                recuperándolos del sistema.

        removePropertyChangeListener(PropertyChangeListener listener)
                Elimina PropertyChangeListener.

        removeVetoableChangeListener(VetoableChangeListener listener)
                Elimina VetoableChangeListener.

        setAccountingCode(String accountingCode)
                Establece el código de contabilidad asociado a este perfil de usuario.

        setAssistanceLevel(String assistanceLevel)
                Establece qué interfaz de usuario usar.

       	setAttentionKeyHandlingProgram(String attentionKeyHandlingProgram)
                Establece el programa que se usará como el programa de manejo de
                teclas Atención (ATTN) para este usuario.

        setCCSID(integer ccsid)
                Establece el identificador de conjunto de códigos de caracteres (CCSID)
                que se utilizará para este usuario.

        setCCSID(String ccsid)
                Establece el identificador de conjunto de códigos de caracteres (CCSID)
                que se utilizará para este usuario.

        setCHRIDControl(String chridControl)
                Establece el control de identificador de caracteres (CHRIDCTL) para el trabajo.

        setCountryID(String countryID)
                Establece el identificador de país o región que se utilizará para este usuario.

        setCurrentLibraryName(String currentLibraryName)
                Establece el nombre de la biblioteca actual asociada con el trabajo
                que se está ejecutando.

        setDescription(String description)
                Establece el texto que describe brevemente el objeto.

        setDisplaySignOnInformation(String displaySignOnInformation)
                Establece si se muestra la pantalla de información de inicio de sesión.

        setGroupAuthority(String groupAuthority)
                Establece la autoridad específica otorgada al perfil de grupo para los
                objetos recién creados.

        setGroupAuthorityType(String groupAuthorityType)
                Establece el tipo de autorización que se otorgará al perfil de grupo
                para los objetos recién creados.

        setGroupID(long groupID)
                Establece el número de ID de grupo (número gid) para este perfil de usuario.

        setGroupID(String groupID)
                Establece el número de ID de grupo (número gid) para este perfil de usuario.

        setGroupProfileName(String groupProfileName)
                Establece el nombre del perfil de grupo del usuario cuya autoridad
                se utiliza si no se otorga una autoridad específica para el usuario.

        setHighestSchedulingPriority(integer highestSchedulingPriority)
                Establece la prioridad de programación más alta que el usuario puede
                tener para cada trabajo enviado al sistema.

        setHomeDirectory(String homeDirectory)
                Establece el nombre de ruta del directorio de inicio para este perfil de usuario.

        setInitialMenu(String initialMenu)
                Establece el menú inicial que se muestra cuando el usuario inicia sesión
                en el sistema si el programa de enrutamiento del usuario es el
                procesador de comandos.

        setInitialProgram(String initialProgram)
                Establece, para un trabajo interactivo, el programa llamado cada vez
                que se inicia un nuevo paso de enrutamiento que tiene QCMD
                como programa de procesamiento de solicitudes.

        setJobDescription(String jobDescription)
                Establece el nombre de vía de acceso del sistema de archivos integrado completo
                de la descripción del trabajo que se utiliza para los trabajos que comienzan
                a través de las entradas de la estación de trabajo del subsistema.

        setKeyboardBuffering(String keyboardBuffering)
                Establece el valor de almacenamiento en búfer del teclado que se utilizará
                cuando se inicialice un trabajo para este perfil de usuario.

        setLanguageID(String languageID)
                Establece el ID de idioma que se utilizará para este usuario.

        setLimitCapabilities(String limitCapabilities)
                Establece el límite al que el usuario puede controlar el programa, el menú,
                la biblioteca actual y los valores del programa de manejo de teclas ATTN.

        setLimitDeviceSessions(String limitDeviceSessions)
                Establece si la cantidad de sesiones de dispositivo permitidas para un
                usuario está limitada a 1.

        setLocaleJobAttributes(lista String[] localeJobAttributes)
                Establece qué atributos de trabajo se tomarán de la configuración regional
                especificada para el parámetro Configuración regional (LOCALE)
                cuando se inicie el trabajo.

        setLocalePathName(String localePathName)
                Establece el nombre de ruta de la configuración regional que se asigna
                a la variable de entorno LANG para este usuario.

        setLocalPasswordManagement(boolean localPasswordManagement)
                Establece si la contraseña del perfil de usuario debe administrarse localmente.

        setMaximumStorageAllowed(integer maximumStorageAllowed)
                Establece la cantidad máxima de almacenamiento auxiliar
                (en kilobytes) asignada para almacenar objetos permanentes
                propiedad de este perfil de usuario (1 kilobyte equivale a 1024 bytes).

        setMaximumStorageAllowed(String maximumStorageAllowed)
                Establece la cantidad máxima de almacenamiento auxiliar
                (en kilobytes) asignada para almacenar objetos permanentes
                propiedad de este perfil de usuario (1 kilobyte equivale a 1024 bytes).

        setMessageQueue(String messageQueue)
                Establece la cola de mensajes a la que se envían los mensajes.

        setMessageQueueDeliveryMethod(String messageQueueDeliveryMethod)
                Establece cómo se enviarán los mensajes a la cola de mensajes para este usuario.

        setMessageQueueSeverity(integer messageQueueSeverity)
                Establece el código de gravedad más bajo que puede tener un mensaje
                y aun así ser entregado a un usuario en modo de interrupción o notificación.

        setName(String name)
                Establece el nombre del perfil de usuario.

        setObjectAuditingValue(String objectAuditingValue)
                Establece el valor de auditoría del objeto para el usuario.

        setOutputQueue(String outputQueue)
                Establece la cola de salida que utilizará este perfil de usuario.

        setOwner(java.lang.String owner)
                Establece el perfil de usuario que será el propietario de los objetos
                creados por este usuario.

        setPasswordChangeBlock(String pwdChangeBlock)
                Establece el período de tiempo durante el cual se bloquea el cambio
                de una contraseña después de la operación anterior de cambio de
                contraseña exitosa.

        setPasswordExpirationInterval(integer passwordExpirationInterval)
                Establece el intervalo de caducidad de la contraseña (en días).

        setPasswordExpirationInterval(String passwordExpirationInterval)
                Establece el intervalo de caducidad de la contraseña (en días).

        setPasswordSetExpire(boolean passwordSetExpire)
                Establece si la contraseña de este usuario está configurada como caducada.

        setPrintDevice(String printDevice)
                Establece el dispositivo de impresora predeterminado para este usuario.

        setSortSequenceTable(String sortSequenceTable)
                Establece la tabla de secuencia de clasificación que se utilizará para las
                comparaciones de cadenas para este perfil.

        setSpecialAuthority(lista String[] specialAuthority)
                Establece las autorizaciones especiales otorgadas a un usuario.

        setSpecialEnvironment(String specialEnvironment)
                Establece el entorno especial en el que opera el usuario después de iniciar sesión.

        setStatus(String status)
                Establece el estado del perfil de usuario.

        setSupplementalGroups(lista String[] supplementalGroups)
                Establece los perfiles de grupo complementarios del usuario.

        setSystem(AS400 system)
                Establece el objeto del sistema que representa el sistema en el
                que existe el perfil de usuario.

        setUserActionAuditLevel(lista String[] userActionAuditLevel)
                Establece el nivel de actividad que se audita para este perfil de usuario.

        setUserClassName(String userClassName)
                Establece el tipo de usuario asociado a este perfil de usuario:
                responsable de seguridad, administrador de seguridad, programador,
                operador del sistema o usuario.

        setUserExpirationDate(Date expirationDate)
                Establece la fecha de caducidad del perfil de usuario y se
                desactiva automáticamente.

        setUserExpirationInterval(integer expirationInterval)
                Establece el intervalo de caducidad (en días) antes de que el
                perfil de usuario se deshabilite automáticamente.

        setUserID(long userID)
                Establece el número de ID de usuario (número uid)
                para este perfil de usuario.

        setUserOptions(lista String[] userOptions)
                Establece el nivel de detalle de la información de ayuda que se mostrará
                y la función de las teclas Page Up y Page Down de forma predeterminada.

        String = toString()
                Establece la representación de cadena de este objeto Usuario.

        """
        # asigna la clase java de User
        self.usuario = jpype.JClass('com.ibm.as400.access.User')

        # instancio el usuario
        self.usuario = self.usuario(system, user)

        # inicializo el constructor de DirectoryEntry
        DirectoryEntry.__int__(self)

    # ***
    # Recupera el código de contabilidad asociado a este usuario.
    def getUserAccountingCode(self):
        """
            Recupera el código de contabilidad asociado a este usuario.
                    String = getAccountingCode()
        """
        return self.usuario.getAccountingCode()

    # ***
    # Determina si este perfil de usuario existe en el sistema.
    def getUserexists(self):
        """
            Determina si este perfil de usuario existe en el sistema.
                boolean = exists()

        """
        return self.usuario.exists()

    # ***
    # Recupera la interfaz de usuario que utilizará el usuario.
    def getUserAssistanceLeve(self):
        """
            Recupera la interfaz de usuario que utilizará el usuario.
                String = getAssistanceLevel()

        """
        return self.usuario.getAssistanceLevel()

    # ***
    # Recupera el programa de manejo de la llave de atención para este usuario.
    def getUserAttentionKeyHandlingProgram(self):
        """
            Recupera el programa de manejo de la llave de atención para este usuario.
                String = getAttentionKeyHandlingProgram()

        """
        return self.usuario.getAttentionKeyHandlingProgram()

    # ***
    # Recupera el ID del conjunto de códigos de caracteres que utilizará
    def getUserCCSID(self):

        """
            Recupera el ID del conjunto de códigos de caracteres que utilizará
            el sistema para este usuario.
                integer = getCCSID()
        """
        return self.usuario.getCCSID()

    # ***
    # Recupera el control de identificador de caracteres para el usuario.
    def getUserCHRIDControl(self):

        """
            Recupera el control de identificador de caracteres para el usuario.
                String = getCHRIDControl()
        """
        return self.usuario.getCHRIDControl()

    # ***
    # Recupera el ID de país o región utilizado por el sistema para este usuario.
    def getUserCountryID(self):

        """
            Recupera el ID de país o región utilizado por el sistema para este usuario.
                String = getCountryID()
        """
        return self.usuario.getCountryID()

    # ***
    # Recupera el nombre de la biblioteca actual del usuario.
    def getUserCurrentLibraryName(self):

        """
            Recupera el nombre de la biblioteca actual del usuario.
                String = getCurrentLibraryName()
        """
        return self.usuario.getCurrentLibraryName()

    # ***
    # Recupera el número de días hasta que caduque la contraseña.
    def getUserDaysUntilPasswordExpire(self):

        """
            Recupera el número de días hasta que caduque la contraseña.
                integer = getDaysUntilPasswordExpire()
        """
        return self.usuario.getDaysUntilPasswordExpire()


    # ***
    # Recupera el texto descriptivo del perfil de usuario.
    def getUserDescription(self):

        """
            Recupera el texto descriptivo del perfil de usuario.
                String = getDescription()
        """
        return self.usuario.getDescription()

    # ***
    #  String = getDetailInSTRAUTCOL()
    def getUserDetailInSTRAUTCOL(self):

        """
            String = getDetailInSTRAUTCOL()

        """
        return self.usuario.getDetailInSTRAUTCOL()

    # ***
    # Recupera si la pantalla de información de inicio de sesión
    def getUserDisplaySignOnInformation(self):

        """
            Recupera si la pantalla de información de inicio de sesión se
            nuestra cuando el usuario inicia sesión.
                String = getDisplaySignOnInformation()
        """
        return self.usuario.getDisplaySignOnInformation()

    # ***
    #  Recupera la autoridad que tiene el perfil de grupo del usuario
    def getUserGroupAuthority(self):

        """
            Recupera la autoridad que tiene el perfil de grupo del usuario sobre
            los objetos que crea el usuario.
                String = getGroupAuthority()
        """
        return self.usuario.getGroupAuthority()

    # ***
    # Recupera el tipo de autorización que tiene el grupo del usuario
    # sobre los objetos que crea el usuario.
    def getUserGroupAuthorityType(self):

        """
            Recupera el tipo de autorización que tiene el grupo del usuario
            sobre los objetos que crea el usuario.
            String = getGroupAuthorityType()
        """
        return self.usuario.getGroupAuthorityType()

    # ***
    # Recupera el número de ID de grupo para el perfil de usuario.
    def getUserGroupID(self):

        """
            Recupera el número de ID de grupo para el perfil de usuario.
            long = getGroupID()
        """
        return self.usuario.getGroupID()

    # ***
    # Recupera la prioridad de programación más alta que el usuario puede
    def getUserHighestSchedulingPriority(self):

        """
        Recupera la prioridad de programación más alta que el usuario puede
        tener para cada trabajo enviado al sistema.
            integer = getHighestSchedulingPriority()
        """
        return self.usuario.getHighestSchedulingPriority()

    # ***
    # Recupera el directorio de inicio para este perfil de usuario.
    def getUserHomeDirectory(self):

        """
            Recupera el directorio de inicio para este perfil de usuario.
            String = getHomeDirectory()
        """
        return self.usuario.getHomeDirectory()


    # ***
    # Recupera la lista de nombres de agrupación de almacenamiento auxiliar
    def getIUserASPNames(self):

        """
            Recupera la lista de nombres de agrupación de almacenamiento auxiliar
            independiente (IASP) que utiliza este usuario.
            lista String[] = getIASPNames()
        """
        return self.usuario.getIASPNames()


    # ***
    #  Recupera la cantidad máxima de almacenamiento auxiliar en kilobytes
    def getUserIASPStorageAllowed(self, iaspName):

        """
            Recupera la cantidad máxima de almacenamiento auxiliar en kilobytes
            que se puede asignar para almacenar objetos permanentes propiedad
            de este usuario en la ASP independiente dada.
            integer = getIASPStorageAllowed(String iaspName)
        """
        return self.usuario.getIASPStorageAllowed(iaspName)


    # ***
    #  Recupera la cantidad de almacenamiento auxiliar en kilobytes
    def getUserIASPStorageUsed(self, iaspName):

        """
            Recupera la cantidad de almacenamiento auxiliar en kilobytes
            que ocupan los objetos propiedad de este usuario en la ASP
            independiente dada.
            integer = getIASPStorageUsed(String iaspName)
        """
        return self.usuario.getIASPStorageUsed(iaspName)


    # ***
    # Recupera el menú inicial para el usuario.
    def getUserInitialMenu(self):

        """
            Recupera el menú inicial para el usuario.
            String = getInitialMenu()
        """
        return self.usuario.getInitialMenu()



    # ***
    # Recupera el programa inicial para el usuario.
    def getUserInitialProgram(self):

        """
            Recupera el programa inicial para el usuario.
            String = getInitialProgram()
        """
        return self.usuario.getInitialProgram()


    # ***
    # Recupera el nombre completo de la vía de acceso del sistema de
    # archivos integrado de la descripción del trabajo que se utiliza para los
    # trabajos que comienzan a través de las entradas de la estación
    # de trabajo del subsistema.
    def getUserJobDescription(self):

        """
            Recupera el nombre completo de la vía de acceso del sistema de
            archivos integrado de la descripción del trabajo que se utiliza para los
            trabajos que comienzan a través de las entradas de la estación
            de trabajo del subsistema.
            String = getJobDescription()
        """
        return self.usuario.getJobDescription()

    # ***
    # Recupera el valor de almacenamiento en búfer del teclado que se
    # utiliza cuando se inicializa un trabajo para este usuario.
    def getUserKeyboardBuffering(self):

        """
            Recupera el valor de almacenamiento en búfer del teclado que se
            utiliza cuando se inicializa un trabajo para este usuario.
            String = getKeyboardBuffering()
        """
        return self.usuario.getKeyboardBuffering()


    # ***
    # Recupera el ID de idioma utilizado por el sistema para este usuario.
    def getUserLanguageID(self):

        """
        Recupera el ID de idioma utilizado por el sistema para este usuario.
        String = getLanguageID()
        """
        return self.usuario.getLanguageID()


    # ***
    # Recupera si el usuario tiene capacidades limitadas.
    def getUserLimitCapabilities(self):

        """
        Recupera si el usuario tiene capacidades limitadas.
        String = getLimitCapabilities()
        """
        return self.usuario.getLimitCapabilities()


    # ***
    # Recupera si el usuario está limitado a una sesión de dispositivo.
    def getUserLimitDeviceSessions(self):

        """
        Recupera si el usuario está limitado a una sesión de dispositivo.
        String = getLimitDeviceSessions()
        """
        return self.usuario.getLimitDeviceSessions()

    # ***
    # Recupera el nombre de la ruta de configuración regional que se
    # asigna al perfil de usuario cuando se inicia un trabajo.
    def getUserLocalePathName(self):

        """
            Recupera el nombre de la ruta de configuración regional que se
            asigna al perfil de usuario cuando se inicia un trabajo.
            String = getLocalePathName()
        """
        return self.usuario.getLocalePathName()


    # ***
    # Recupera la cantidad máxima de almacenamiento auxiliar (en kilobytes)
    # que se puede asignar para almacenar objetos permanentes propiedad
    # del usuario.
    def getUserMaximumStorageAllowed(self):

        """
            Recupera la cantidad máxima de almacenamiento auxiliar (en kilobytes)
            que se puede asignar para almacenar objetos permanentes propiedad
            del usuario.
            integer = getMaximumStorageAllowed()
        """
        return self.usuario.getMaximumStorageAllowed()

    # ***
    # Recupera el nombre completo de la vía de acceso del sistema de archivos
    # integrado de la cola de mensajes que utiliza este usuario.
    def getUserMessageQueue(self):

        """
            Recupera el nombre completo de la vía de acceso del sistema de archivos
            integrado de la cola de mensajes que utiliza este usuario.
            String = getMessageQueue()
        """
        return self.usuario.getMessageQueue()


    # ***
    # Recupera cómo se entregan los mensajes a la cola de mensajes
    # utilizada por el usuario.
    def getUserMessageQueueDeliveryMethod(self):

        """
            Recupera cómo se entregan los mensajes a la cola de mensajes
            utilizada por el usuario.
            String = getMessageQueueDeliveryMethod()
        """
        return self.usuario.getMessageQueueDeliveryMethod()


    # ***
    # Recupera la gravedad más baja que puede tener un mensaje y aun
    # así ser entregado a un usuario en modo de interrupción o notificación.
    def getUserMessageQueueSeverity(self):

        """
            Recupera la gravedad más baja que puede tener un mensaje y aun
            así ser entregado a un usuario en modo de interrupción o notificación.
            integer = getMessageQueueSeverity()
        """
        return self.usuario.getMessageQueueSeverity()

    # ***
    # Devuelve el nombre del perfil de usuario.
    def getUserName(self):

        """
            Devuelve el nombre del perfil de usuario.
            String = getName()
        """
        return self.usuario.getName()


    # ***
    # Recupera la cola de salida utilizada por este usuario.
    def getUserOutputQueue(self):

        """
            Recupera la cola de salida utilizada por este usuario.
            String = getOutputQueue()
        """
        return self.usuario.getOutputQueue()

    # ***
    # Recupera el valor de auditoría del objeto del usuario.
    def getUserObjectAuditingValue(self):

        """
        Recupera el valor de auditoría del objeto del usuario.
        String = getObjectAuditingValue()
        """
        return self.usuario.getObjectAuditingValue()


    # ***
    # Recupera quién es propietario de los objetos creados por este usuario.
    def getUserOwner(self):

        """
        Recupera quién es propietario de los objetos creados por este usuario.
        String = getOwner()
        """
        return self.usuario.getOwner()


    # ***
    # Recupera el período de tiempo durante el cual se bloquea el cambio
    # de una contraseña después de la operación anterior de cambio
    # de contraseña exitosa.
    def getUserPasswordChangeBlock(self):

        """
            Recupera el período de tiempo durante el cual se bloquea el cambio
            de una contraseña después de la operación anterior de cambio
            de contraseña exitosa.
            String = getPasswordChangeBlock()
        """
        return self.usuario.getPasswordChangeBlock()


    # ***
    # Recupera el número de días que la contraseña del usuario puede
    # permanecer activa antes de que deba cambiarse.
    def getUserPasswordExpirationInterval(self):

        """
            Recupera el número de días que la contraseña del usuario puede
            permanecer activa antes de que deba cambiarse.

             integer = getPasswordExpirationInterval()

        """
        return self.usuario.getPasswordExpirationInterval()


    # ***
    # Recupera la fecha de caducidad de la contraseña del usuario.
    def getUserPasswordExpireDate(self):

        """
            Recupera la fecha de caducidad de la contraseña del usuario.
            Date = getPasswordExpireDate()

        """
        return self.usuario.getPasswordExpireDate()


    #  ***
    # Recupera la fecha en que se cambió por última vez la contraseña del usuario.
    def getUserPasswordLastChangedDate(self):

        """
            Recupera la fecha en que se cambió por última vez la contraseña del usuario.
            Date = getPasswordLastChangedDate()

        """
        return self.usuario.getPasswordLastChangedDate()


    # ***
    # Recupera la fecha y la hora en que el usuario inició sesión por última vez.
    def getUserPreviousSignedOnDate(self):
        """
            Recupera la fecha y la hora en que el usuario inició sesión por última vez.
            Date = getPreviousSignedOnDate()

        """
        return self.usuario.getPreviousSignedOnDate()


    # ***
    # Recupera la impresora utilizada para imprimir para este usuario.
    def getUserPrintDevice(self):

        """
            Recupera la impresora utilizada para imprimir para este usuario.
            String = getPrintDevice()

        """
        return self.usuario.getPrintDevice()


    # ***
    # Recupera el número de intentos de inicio de sesión que no fueron
    # válidos desde el último inicio de sesión correcto.
    def getUserSignedOnAttemptsNotValid(self):

        """
            Recupera el número de intentos de inicio de sesión que no fueron
            válidos desde el último inicio de sesión correcto.

            integer = getSignedOnAttemptsNotValid()

        """
        return self.usuario.getSignedOnAttemptsNotValid()


    # ***
    # Recupera el nombre de la tabla de secuencia de ordenación utilizada
    # para las comparaciones de cadenas.
    def getUserSortSequenceTable(self):

        """
            Recupera el nombre de la tabla de secuencia de ordenación utilizada
            para las comparaciones de cadenas.
            String = getSortSequenceTable()

        """
        return self.usuario.getSortSequenceTable()


    # ***
    # Recupera una lista de las autorizaciones especiales que tiene el usuario.
    def getUserSpecialAuthority(self):

        """
            Recupera una lista de las autorizaciones especiales que tiene el usuario.
            lista String[] = getSpecialAuthority()

        """
        return self.usuario.getSpecialAuthority()


    # ***
    # Recupera el entorno especial en el que opera el usuario después de iniciar sesión.
    def getUserSpecialEnvironment(self):

        """
            Recupera el entorno especial en el que opera el usuario después de iniciar sesión.

            String = getSpecialEnvironment()

        """
        return self.usuario.getSpecialEnvironment()



    #  ***
    # Recupera el estado del perfil de usuario.
    def getUserStatus(self):

        """
            Recupera el estado del perfil de usuario.
            String = getStatus()
        """
        return self.usuario.getStatus()


    # ***
    # Recupera la cantidad de almacenamiento auxiliar (en kilobytes)
    # ocupada por los objetos propiedad de este usuario.
    def getUserStorageUsed(self):
        """
        Recupera la cantidad de almacenamiento auxiliar (en kilobytes)
        ocupada por los objetos propiedad de este usuario.
        integer = getStorageUsed()
        """
        return self.usuario.getStorageUsed()


    # ***
    # Recupera la cantidad de almacenamiento auxiliar (en kilobytes)
    # ocupada por los objetos propiedad de este usuario.
    def getUserStorageUsedInLong(self):
        """
            Recupera la cantidad de almacenamiento auxiliar (en kilobytes)
            ocupada por los objetos propiedad de este usuario.
            long = getStorageUsedInLong()
        """
        return self.usuario.getStorageUsedInLong()


    # ***
    # Recupera los grupos complementarios para el perfil de usuario.
    def getUserSupplementalGroups(self):

        """
            Recupera los grupos complementarios para el perfil de usuario.
            lista String[] = getSupplementalGroups()

        """
        return self.usuario.getSupplementalGroups()


    # ***
    # Recupera el número de grupos complementarios para el perfil de usuario.
    def getUserSupplementalGroupsNumber(self):

        """
            Recupera el número de grupos complementarios para el perfil de usuario.
            integer = getSupplementalGroupsNumber()

        """
        return self.usuario.getSupplementalGroupsNumber()


    # ***
    # Recupera una lista de niveles de auditoría de acciones para el usuario.
    def getUserUserActionAuditLevel(self):
        """
            Recupera una lista de niveles de auditoría de acciones para el usuario.
            lista String[] = getUserActionAuditLevel()

        """
        return self.usuario.getUserActionAuditLevel()


    # ***
    # Devuelve el objeto del sistema que representa el sistema en el que
    # existe el perfil de usuario.
    def getUserSystem(self):

        """
            Devuelve el objeto del sistema que representa el sistema en el que
            existe el perfil de usuario.
            AS400 = getSystem()

        """
        return self.usuario.getSystem()


    # ***
    # Recupera el nombre de la clase de usuario.
    def getUserUserClassName(self):

        """
            Recupera el nombre de la clase de usuario.
            String = getUserClassName()

        """
        return self.usuario.getUserClassName()



    # ***
    # Recupera la acción que ocurrirá cuando el perfil de usuario haya expirado.
    def getUserUserExpirationAction(self):

        """
            Recupera la acción que ocurrirá cuando el perfil de usuario haya expirado.
            String = getUserExpirationAction()

        """
        return self.usuario.getUserExpirationAction()



    # ***
    # Recupera la fecha de caducidad del perfil de usuario y se
    # desactiva automáticamente.
    def getUserUserExpirationDate(self):

        """
            Recupera la fecha de caducidad del perfil de usuario y se
            desactiva automáticamente.

            Date = getUserExpirationDate()

        """
        return self.usuario.getUserExpirationDate()


    # ***
    # Recupera el número de días antes de que el perfil de usuario se
    # deshabilite automáticamente.
    def getUserUserExpirationInterval(self):

        """

            Recupera el número de días antes de que el perfil de usuario se
            deshabilite automáticamente.
            integer = getUserExpirationInterval()

        """
        return self.usuario.getUserExpirationInterval()


    # ***
    # Recupera el número de ID de usuario (UID) para el perfil de usuario.
    def getUserUserID(self):

        """
            Recupera el número de ID de usuario (UID) para el perfil de usuario.
            long = getUserID()

        """
        return self.usuario.getUserID()



    # ***
    # Recupera una lista de opciones para que los usuarios personalicen su entorno.
    def getUserUserOptions(self):

        """
            Recupera una lista de opciones para que los usuarios personalicen su entorno.
            lista String[] = getUserOptions()

        """
        return self.usuario.getUserOptions()



    # ***
    # Recupera el nombre del perfil de usuario para el que se devuelve la información.
    def getUserUserProfileName(self):

        """
            Recupera el nombre del perfil de usuario para el que se devuelve la información.
            String = getUserProfileName()

        """
        return self.usuario.getUserProfileName()
