try:
    import sys
    import os
    import platform
    import pickle
    from app_Config import constantes

except Exception as e:
    print(f'Falta algun modulo {e}')

class ConfigHost(object):
    """
    Esta clase tiene como objetivo realizar la gestion de los Host de conexion donde\n
    actualizar la informacion gestionada por un web service.\n

        parametros\n
            (str) serverhost        = Tipo servidor de base de datos.\n
            (str) iphost            = La ip del servidor de base de datos.\n
            (str) usuariohost       = El usuario de conexion al host.\n
            (str) passhost          = La password de la conexion al host.\n
            (str) host              = Nombre del alias del host\n
            (str) databasehost      = Nombre de la base de datos\n
            (str) schemahost        = Nombre del esquema\n


        metodos\n
            list_host  (self)   = Lista los datos de configuracion del host\n
            add_host   (self)   = Agregar datos de la configuracion de un nuevo host\n
            del_host   (self)   = Eliminacion del host\n
            chg_host   (self)   = Cambio de los datos de configuracion del host\n
            new_dbm    (self)   = Nuevo Tipo de Servidor\n

    """

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Constructor
    def __init__(self, serverhost=None, iphost=None,
                 usuariohost=None, passhost=None,
                 host=None, databasehost=None, schemahost=None, accion=None):
        self.SERVER = {'IBM': True}
        self.ERROR = {}


        # Atributos Encapsulados
        self.__serverhost = None
        self.__iphost = None
        self.__usuariohost = None
        self.__passhost = None
        self.__host = None
        self.__databasehost = None
        self.__schemahost = None
        self.__stringConect = None
        self.__accion = None
        self.__hostValidator = None


        # Definicion de Atributos
        self.serverhost = serverhost
        self.iphost = iphost
        self.usuariohost = usuariohost
        self.passhost = passhost
        self.host = host
        self.databasehost = databasehost
        self.schemahost = schemahost
        self.accion = accion


        self.__tipoServer = [ '(iseries ) = (Ibm Iseries)', '(  db2   ) = (Motor DB2)', '( mssql3 ) = (MSSQL >= 2005)',
            '( mssql4 ) = (MSSQL >= 2012)', '( sqlite ) = (extension sqlite)', '(sqlite3 ) = (extension sqlite3)',
            '(  db3   ) = (extension db3 para sqlite)', '(  db    ) = (extension db para sqlite)',
            '(  mysql ) = (MySql)', '(postgres) = (Postgres Sql)', '(firebird) = (FireBird)', '( oracle ) = (Oracle)',
            '( ingres ) = (Ingres)', '( sysbase) = (Sysbase)', '(informix) = (Informix)', '(teradata) = (Teradata)',
            '( cubrid ) = (Cubrid)', '(  sapdb ) = (Sapdb)', '(  imap  ) = (Imap)', '( mongodb) = (MongoDb)',
        ]


        # Valores por default
        if os.getcwd().split('\\')[-1] == constantes.DIR_PROYECTO:         #'ProyectoRegistrosAutomotor':
            self.__pathHost = os.getcwd() + '\\archivos_Estaticos\\Host\\'
        else:
            os.chdir('..')

            # determinamos en que plataforma estamos ejeutando el script
            if platform.system() == 'Linux':
                self.__pathHost = os.getcwd() + '/archivos_Estaticos/Host/'
            else:
                self.__pathHost = os.getcwd() + '\\archivos_Estaticos\\Host\\'

        self.__default_file = self.__pathHost + 'host.pck'
        self.__host_dict = {}
        self.__habilitado = False
        self.__error_key = ''

        # Determina si esta dado de alta el Validator
        #self.__setValidator()

        # Ubicacion de los datos de configuracion
        self.__loadfile()

    # ---------TIPO DE SERVER----------------------------------------------------------------
    # getter del atributo tipoServer
    @property
    def tipoServer(self):
        return self.__tipoServer

    # ---------SERVER HOST-------------------------------------------------------------------
    # getter del atributo serverhost
    @property
    def serverhost(self):
        return self.__serverhost

    # setter del atributo serverhost
    @serverhost.setter
    def serverhost(self, valor):
        """
        Tipo de dato string\n
        Debe ingresar alguna de las siguientes opciones:\n
        iseries     = Ibm Iseries\n
        db2         = Motor DB2\n
        mssql3      = MSSQL >= 2005\n
        mssql4      = MSSQL >= 2012\n
        sqlite      = extension sqlite\n
        sqlite3     = extension sqlite3\n
        db3         = extension db3 para sqlite\n
        db          = extension db para sqlite\n
        mysql       = MySql\n
        postgres    = Postgres Sql\n
        firebird    = FireBird\n
        oracle      = Oracle\n
        ingres      = Ingres\n
        sysbase     = Sysbase\n
        informix    = Informix\n
        teradata    = Teradata\n
        cubrid      = Cubrid\n
        sapdb       = Sapdb\n
        imap        = Imap\n
        mongodb     = MongoDb\n
        """

        self.__serverhost = valor

    # ---------IP HOST-------------------------------------------------------------------
    # getter del atributo iphost
    @property
    def iphost(self):
        return self.__iphost

    # setter del atributo iphost
    @iphost.setter
    def iphost(self, valor):
        """
        Tipo de dato string\n
        Debe ingresar la direccion IP del host por ejemplo:\n
        172.16.5.19\n
        """
        self.__iphost = valor

    # ---------USUARIO DEL HOST----------------------------------------------------------
    # getter del atributo usuariohost de conexion
    @property
    def usuariohost(self):
        return self.__usuariohost

    # setter del atributo usuariohost de conexion
    @usuariohost.setter
    def usuariohost(self, valor):
        """
        Tipo de dato string\n
        Debe ingresar el Usuario para ingresar al Host\n
        """
        self.__usuariohost = valor

    # ---------PASSWORD DEL HOST---------------------------------------------------------
    # getter del atributo passhost de conexion
    @property
    def passhost(self):
        return self.__passhost

    # setter del atributo passhost de conexion
    @passhost.setter
    def passhost(self, valor):
        """
        Tipo de dato string\n
        Debe ingresar la Password del Usuario para ingresar al Host\n
        """
        self.__passhost = valor

    # ---------HOST-------------------------------------------------------------------
    # getter del atributo host
    @property
    def host(self):
        return self.__host

    # setter del atributo host
    @host.setter
    def host(self, valor):
        """
        Tipo de dato string\n
        Debe ingresar el Alias del Host por ejemplo:\n
        IngresoTest
        """
        self.__host = valor

    # ---------DATABASEHOST-------------------------------------------------------------------
    # getter del atributo databasehost
    @property
    def databasehost(self):
        return self.__databasehost

    # setter del atributo databasehost
    @databasehost.setter
    def databasehost(self, valor):
        """
        Tipo de dato string\n
        Debe ingresar el Nombre de la Base de Datos del Host\n
        """
        self.__databasehost = valor

    # ---------SCHEMAHOST-------------------------------------------------------------------
    # getter del atributo schemahost
    @property
    def schemahost(self):
        return self.__schemahost

    # setter del atributo schemahost
    @schemahost.setter
    def schemahost(self, valor):
        """
        Tipo de dato string\n
        Debe ingresar el Nombre del Esquema la Base de Datos del Host\n
        Se utiliza solo para el host iseries\n

        """
        self.__schemahost = valor

    # ---------ACCION-------------------------------------------------------------------
    # geter del atributo accion
    @property
    def accion(self):
        return self.__accion

    # seter del atributo accions
    @accion.setter
    def accion(self, valor):
        """
        Tipo de dato string\n
        Debe ingresar la Accion que deseamos por ejemplo:\n
        list = Lista los datos de configuracion del host\n
        add  = Agregar datos de la configuracion de un nuevo host\n
        del  = Eliminacion del host\n
        chg  = Cambio de los datos de configuracion del host\n

        """
        self.__accion = valor

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Obtener la descripcion del host
    # es el string de conexion de las distintas bases de datos
    def __string_conexion_database(self):
        """
        String de conexion a distintos database\n

        """
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de Iseries
        if self.serverhost == 'iseries':

            self.__habilitado = (
            self.serverhost != None and  self.usuariohost != None and self.passhost !=None and self.schemahost != None
            )
            if self.__habilitado == False: return ''

            drive = '{iSeries Access ODBC Driver}'
            host = self.iphost
            uid  = self.usuariohost
            pwd  = self.passhost
            dbq  = self.schemahost
            return f'db2:pyodbc://driver={drive}; system={host}; uid={uid}; pwd={pwd}; dbq={dbq}'

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de db2
        if self.serverhost == 'db2':
            self.__habilitado = (
            self.serverhost != None and  self.usuariohost != None and self.passhost !=None
            )
            if self.__habilitado == False: return ''

            host = self.serverhost
            uid  = self.usuariohost
            pwd  = self.passhost
            return f'db2:pyodbc://DSN=QDSN_{host};UID={uid};PWD={pwd};'

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de mssql >= 2005
        if self.serverhost == 'mssql3':
            self.__habilitado = (
            self.serverhost != None and  self.usuariohost != None and self.passhost !=None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            host = self.serverhost
            uid = self.usuariohost
            pwd = self.passhost
            Db = self.databasehost

            return f'mssql3//{uid}:{pwd}@{host}/{Db}'

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de mssql >= 2012
        if self.serverhost == 'mssql4':
            self.__habilitado = (
            self.serverhost != None and  self.usuariohost != None and self.pashost !=None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            host = self.serverhost
            Db = self.databasehost

            return f'mssql4//{uid}:{pwd}@{host}/{Db}'


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de sqlite
        if self.serverhost == 'sqlite':
            self.__habilitado = ( self.databasehost != None )
            if self.__habilitado == False: return ''

            Db = self.databasehost

            return f'sqlite://{Db}.sqlite'


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de sqlite3
        if self.serverhost == 'sqlite3':
            self.__habilitado = ( self.databasehost != None )
            if self.__habilitado == False: return ''

            Db = self.databasehost

            return f'sqlite://{Db}.sqlite3'

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de sqlite db
        if self.serverhost == 'db':
            self.__habilitado = ( self.databasehost != None )
            if self.__habilitado == False: return ''

            Db = self.databasehost

            return f'sqlite://{Db}.db'


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de sqlite db3
        if self.serverhost == 'db3':
            self.__habilitado = ( self.databasehost != None )
            if self.__habilitado == False: return ''

            Db = self.databasehost

            return f'sqlite://{Db}.db3'


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de Postgres Sql
        if self.serverhost == 'postgres':
            self.__habilitado = (
            self.serverhost != None and  self.usuariohost != None and self.passhost !=None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            host = self.serverhost
            Db = self.databasehost
            ip = self.iphost

            return f'postgres://{uid}:{pwd}@{ip}/{Db}'


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de MySql
        if self.serverhost == 'mysql':
            self.__habilitado = (
            self.serverhost != None and  self.usuariohost != None and self.passhost !=None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            host = self.serverhost
            ip   = self.iphost
            Db = self.databasehost

            return f'mysql://{uid}:{pwd}@{ip}/{Db}?set_encoding = utf8mb4'


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de Firebird
        if self.serverhost == 'firebird':
            self.__habilitado = (
            self.serverhost != None and  self.usuariohost != None and self.passhost !=None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            host = self.serverhost
            Db = self.databasehost

            return f'firebird://{uid}:{pwd}@{host}/{Db}'


        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de Oracle
        if self.serverhost == 'oracle':
            self.__habilitado = (
            self.usuariohost != None and self.passhost !=None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            Db = self.databasehost

            return f'oracle://{uid}:{pwd}@{Db}'

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de Ingres
        if self.serverhost == 'ingres':
            self.__habilitado = (
            self.serverhost != None and  self.usuariohost != None and self.passhost !=None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            host = self.serverhost
            Db = self.databasehost

            return f'ingres://{uid}:{pwd}@{host}/{Db}'

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de Sysbase
        if self.serverhost == 'sysbase':
            self.__habilitado = (
            self.serverhost != None and self.usuariohost != None and self.passhost != None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            host = self.serverhost
            Db = self.databasehost

            return f'sybase://{uid}:{pwd}@{host}/{Db}'

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de Informix
        if self.__serverhost == 'informix':
            self.__habilitado = (
                    self.usuariohost != None and self.passhost != None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            Db = self.databasehost

            return f'informix://{uid}:{pwd}@{Db}'

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de Teradata
        if self.serverhost == 'teradata':
            self.__habilitado = (
            self.serverhost != None and self.usuariohost != None and self.passhost != None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            host = self.serverhost
            Db = self.databasehost

            return f'teradata://DSN=qdsn_{host};UID={uid};PWD={pwd};DATABASE={Db}'

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de Cubrid
        if self.serverhost == 'cubrid':
            self.__habilitado = (
            self.serverhost != None and self.usuariohost != None and self.passhost != None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            host = self.serverhost
            Db = self.databasehost

            return f'cubrid://{uid}:{pwd}@{host}/{Db}'

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de SapDb
        if self.serverhost == 'sapdb':
            self.__habilitado = (
            self.serverhost != None and self.usuariohost != None and self.passhost != None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            host = self.serverhost
            Db = self.databasehost

            return f'sapdb://{uid}:{pwd}@{host}/{Db}'

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de Imap
        if self.serverhost == 'imap':
            self.__habilitado = (
            self.serverhost != None and self.usuariohost != None and self.passhost != None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            host = self.serverhost
            Db = self.databasehost
            port = '80'

            return f'imap://{uid}:{pwd}@{host}:{port}'

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # para el caso de MongoDb
        if self.serverhost == 'mongodb':
            self.__habilitado = (
            self.serverhost != None and self.usuariohost != None and self.passhost != None and self.databasehost != None
            )
            if self.__habilitado == False: return ''

            uid = self.usuariohost
            pwd = self.passhost
            host = self.serverhost
            Db = self.databasehost

            return f'mongodb://{uid}:{pwd}@{host}/{Db}'

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Obtener la descripcion del host
    def __get_host(self):
        """
        Obtiene los datos del host\n
        Parametros de clase\n
        (str) host   = Nombre del alias del host\n\n
        Retorna una descripcion\n
        Descripcion de los datos del host\n
        o\n
        Mensaje de error del metodo de la clase\n

        """
        # Verifica si el host tiene datos
        if self.host != None:

            if len(self.__host_dict) == 0:
                self.__loadfile()

            # Averigua si el error esta en el diccionario
            self.__error_key = self.host

            # si encuentra el error
            if self.__host_dict[self.__error_key]:
                return self.__host_dict[self.__error_key]

            # si no se encuentra el error
            else:
                return '** EL HOST INEXISTENTE **'
        else:
            return '** DEBE INGRESAR EL HOST **'

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Este metodo realiza el listado de los host
    def list_host(self):
        """
        Este metodo realiza el listado de los host\n
        Parametros de clase\n
        (str) host     = Nombre del alias del host o (*all) para ver todos\n
        Retorna una descripcion\n
        (True) si la operacion fue realizada correctamente\n
        o\n
        (False) con Mensaje de error del metodo de la clase
        """
        # Verifica la accion
        if self.accion != 'list':
            print('** ATENCION CONSULTE LA DOCUMENTACION. LA ACCION DEBE SER (list) **')
            return False

        # Si tiene el valor el host
        if self.host == None:
            return print('** ATENCION CONSULTE LA DOCUMENTACION. DEBE INGRESAR UN HOST O (*all) para (list) **')
            return False

        if not self.__host_dict:
            print(
                '** ATENCION LA TABLA DE HOST DE LA ACCION {}  ESTA VACIA **'.format(self.accion))
            return False

        # navegacion en la lista de errores
        retorno = False
        for k, v in self.__host_dict.items():
            if self.host == k:
                print('{} = {} '.format(k, v))
                return True

            if self.host == '*all':
                print('{} = {} '.format(k, v))
                retorno = True

        if not retorno:
            print('** ATENCION EL HOST NO EXISTE **')
        return retorno

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Devuelve el contenido en un formato string
    def __datos__(self):
        """
        Devuelve el contenido en un formato string
        """
        return self.__get_host()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Agregar un nuevo host
    def add_host(self):
        """
        Agrega un nuevo host del metodo a la clase\n
        parametros\n
        (str) serverhost    = Tipo servidor de base de datos.\n
        (str) iphost        = La ip del servidor de base de datos.\n
        (str) usuariohost   = El usuario de conexion al host.\n
        (str) passhost      = La password de la conexion al host.\n
        (str) host          = Nombre del alias del host\n
        (str) databasehost  = Nombre de la base de datos\n
        (str) schemahost    = Nombre del esquema\n


        Retorna Un valor Booleano\n
        (True) si el host fue agregado\n
        (False) si los parametros son igual a None\n
        (False) si el host YA EXISTE\n
        """

        # Verifica la accion y el server host
        if self.accion == None or self.serverhost == None:
            print(
                '** ATENCION CONSULTE LA DOCUMENTACION. PARA LA ACCION DEBE SER (add) **')
            return False

        if self.accion != 'add':
            print(
                '** ATENCION CONSULTE LA DOCUMENTACION. PARA LA ACCION DEBE SER (add) **')
            return False

        # Obtiene si esta habilitado
        rply = self.__string_conexion_database()

        # averigua si hay datos para dar de alta
        return self.__enabled()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Elimincacion del host
    def del_host(self):
        """
        Elimina el Host de la clase ConfigHost\n
        parametros\n
        (str) host  = Nombre del alias del host\n

        Retorna Un valor Booleano\n
        (True) si la eliminacion fue existosa\n
        (False) si los parametros son igual a None\n
        (False) si el host NO EXISTE como error en la clase\n
        """

        if self.accion != 'del':
            print('** ATENCION CONSULTE LA DOCUMENTACION. LA ACCION DEBE SER (del)**')
            return False

        # Obtiene si esta habilitado
        self.__habilitado = (self.__host != None)

        # Averigua si hay Datos para Eliminar
        return self.__enabled()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Cambio de los datos del host
    def chg_host(self):
        """
        Cambia lod datos del host\n
        parametros\n
        (str) iphost        = La ip del servidor de base de datos.\n
        (str) usuariohost   = El usuario de conexion al host.\n
        (str) passhost      = La password de la conexion al host.\n
        (str) host          = Nombre del alias del host\n
        (str) databasehost  = Nombre de la base de datos\n
        (str) schemahost    = Nombre del esquema\n



        Retorna Un valor Booleano\n
        (True) si el cambio fue exitoso\n
        (False) si los parametros son igual a None\n
        (False) si el codigo y el metodo NO EXISTE como error en la clase\n
        """

        # Verifica que la accion sea 'chg'
        if self.accion != 'chg':
            print('** ATENCION CONSULTE LA DOCUMENTACION. LA ACCION DEBE SER (chg) **')
            return False

        # Obtiene si esta habilitado
        self.__habilitado = (self.serverhost != None or self.iphost != None or self.usuariohost != None or self.passhost !=
                             None or self.databasehost != None or self.schemahost != None)

        # Obtiene si esta habilitado
        rply = self.__string_conexion_database()


        # Verifica si el procedimiento esta habilitado
        return self.__enabled()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Salvar en forma permanente los datos de configuracion del host
    def __savefile(self):
        """
        Graba en forma permanente los datos del host
            Para poder realizar el salvado los datos del host el host no puede estar en None
        """

        if self.__default_file != None:
            try:
                outfile = open(self.__default_file, 'wb')
                pickle.dump(self.__host_dict, outfile)
                outfile.close()

            # Control de cancelacion
            except Exception as inst:
                raise ValueError(inst)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Carga el diccionario de los host
    # abre el archivo y recupera los datos de conexion a las bases de datos
    def __loadfile(self):

        # Realiza la apertura del archivo
        try:

            infile = open(self.__default_file, 'rb')
            self.__host_dict = pickle.load(infile)
            infile.close()

        # Control de cancelacion
        # Si no existe el archivo
        except FileNotFoundError as e:

            # creacion del archivo
            outfile = open(self.__default_file, 'wb')
            pickle.dump(self.__host_dict, outfile)
            outfile.close()

            # Apertura del archivo
            infile = open(self.__default_file, 'rb')
            self.__host_dict = pickle.load(infile)

            infile.close()
            return False

        except IOError as e:
            raise ValueError(e)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Re Carga los atributos encapsulados
    def __atributos(self):

        # Atributos Encapsulados

        self.__serverhost = self.serverhost
        self.__iphost = self.iphost
        self.__usuariohost = self.usuariohost
        self.__passhost = self.passhost
        self.__host = self.host
        self.__databasehost = self.databasehost
        self.__schemahost = self.schemahost
        self.__accion = self.accion


        # Carga los datos del archivo
        self.__loadfile()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Actualicacion del diccionario host
    def __update_host_dic(self):

        try:
            # Verifica si el elemento existe
            if self.__host_dict[self.__error_key]:

                # Envia un error
                if self.accion == 'add':
                    print('** ATENCION EL HOST YA EXISTE **')
                    return False

                # Elimina el elemento
                if self.accion == 'del':
                    cadena = self.__host_dict.pop(self.__error_key)
                    self.__savefile()
                    return True

                # Actualiza el elemento
                detalle_dict = self.__host_dict[self.host]

                if self.__serverhost != None:
                    detalle_dict['server'] = self.serverhost

                if self.__iphost != None:
                    detalle_dict['ip'] = self.iphost

                if self.__usuariohost != None:
                    detalle_dict['usuario'] = self.usuariohost

                if self.__passhost != None:
                    detalle_dict['password'] = self.passhost

                if self.__databasehost != None:
                    detalle_dict['database'] = self.databasehost

                if self.__schemahost != None:
                    detalle_dict['schema'] = self.schemahost

                if self.__stringConect != None:
                    detalle_dict['strcon'] = self.__string_conexion_database()


                self.__host_dict[self.__error_key] = detalle_dict
                self.__savefile()
                return True

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        # En el caso que no exista el elemento
        except KeyError as e:

            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            # Agrega un nuevo elemento
            if self.accion == 'add':


                detalle_dict = {'server': self.serverhost, 'ip': self.iphost,
                                'usuario': self.usuariohost, 'password': self.passhost,
                                'database': self.databasehost, 'schema': self.schemahost,
                                'strcon': self.__string_conexion_database()}

                self.__host_dict[self.__error_key] = detalle_dict
                self.__savefile()
                return True

            # Visualiz un Error
            print('** ATENCION EL HOST NO EXISTE **')
            return False

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Verifica si la actualizacion esta habilitado
    def __enabled(self):

        # La accion de chg carga los atributos para encapsular
        #self.__atributos()

        # Averigua si hay datos para cambiar valor
        if self.__habilitado:

            # Averigua si el error esta en el diccionario
            self.__error_key = self.host

            # Actualiza el diccionario de los datos del host
            return self.__update_host_dic()

        # Si hay algun parametro que tiene None
        else:
            print(
                '** ATENCION CONSULTE LA DOCUMENTACION. PARA ({}) EL HOST **'.format(self.__accion))
            return False

        pass

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Determina si existe el Validator
    def __setValidator(self):

        # Verifica el contenido del host Validator
        if self.__hostValidator == None:
            self.serverhost = 'sqlite3'
            self.host = 'Validator'
            self.databasehost = 'Automotor'
            self.accion = 'add'

            # Ingresa un nuevo host
            self.add_host()
            self.__hostValidator = 'Validator'

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Nuevo server dbm
    def __newserver(self):
        pass

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # Validacion server IBM
    def __valida_IBM(self):
        pass


