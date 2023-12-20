# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Definimos la clase Job
class Job():

    ACCOUNTING_CODE = 1001
    ACCOUNTING_CODE_BLANK = '*BLANK'
    ACTIVE_JOB_STATUS = 101
    ACTIVE_JOB_STATUS_DISCONNECTED = 'DSC '
    ACTIVE_JOB_STATUS_ENDED = 'END '
    ACTIVE_JOB_STATUS_ENDING = 'EOJ '
    ACTIVE_JOB_STATUS_FOR_JOBS_ENDING = 103
    ACTIVE_JOB_STATUS_HELD = "HLD "
    ACTIVE_JOB_STATUS_HELD_THREAD = "HLDT"
    ACTIVE_JOB_STATUS_INELIGIBLE = "INEL"
    ACTIVE_JOB_STATUS_NONE = ' '
    ACTIVE_JOB_STATUS_RUNNING = "RUN "
    ACTIVE_JOB_STATUS_STOPPED = "SIGS"
    ACTIVE_JOB_STATUS_SUSPENDED = "GRP "
    ACTIVE_JOB_STATUS_SUSPENDED_SYSTEM_REQUEST = "SRQ "
    ACTIVE_JOB_STATUS_WAIT_BIN_SYNCH_DEVICE = "BSCW"
    ACTIVE_JOB_STATUS_WAIT_BIN_SYNCH_DEVICE_AND_ACTIVE = "BSCA"
    ACTIVE_JOB_STATUS_WAIT_CHECKPOINT = "CMTW"
    ACTIVE_JOB_STATUS_WAIT_COMM_DEVICE = "CMNW"
    ACTIVE_JOB_STATUS_WAIT_COMM_DEVICE_AND_ACTIVE = "CMNA"
    ACTIVE_JOB_STATUS_WAIT_CONDITION = "CNDW"
    ACTIVE_JOB_STATUS_WAIT_CPI_COMM = "CPCW"
    ACTIVE_JOB_STATUS_WAIT_DATABASE_EOF = "EOFW"
    ACTIVE_JOB_STATUS_WAIT_DATABASE_EOF_AND_ACTIVE = "EOFA"
    ACTIVE_JOB_STATUS_WAIT_DELAY = "DLYW"
    ACTIVE_JOB_STATUS_WAIT_DELAYED = "DLYW"
    ACTIVE_JOB_STATUS_WAIT_DEQUEUE = "DEQW"
    ACTIVE_JOB_STATUS_WAIT_DEQUEUE_AND_ACTIVE = "DEQA"
    ACTIVE_JOB_STATUS_WAIT_DISKETTE = "DKTW"
    ACTIVE_JOB_STATUS_WAIT_DISKETTE_AND_ACTIVE = "DKTA"
    ACTIVE_JOB_STATUS_WAIT_DISPLAY = "DSPW"
    ACTIVE_JOB_STATUS_WAIT_DISPLAY_AND_ACTIVE = "DSPA"
    ACTIVE_JOB_STATUS_WAIT_EVENT = "EVTW"
    ACTIVE_JOB_STATUS_WAIT_ICF_FILE = "ICFW"
    ACTIVE_JOB_STATUS_WAIT_ICF_FILE_AND_ACTIVE = "ICFA"
    ACTIVE_JOB_STATUS_WAIT_JAVA = "JVAW"
    ACTIVE_JOB_STATUS_WAIT_JAVA_AND_ACTIVE = "JVAA"
    ACTIVE_JOB_STATUS_WAIT_LOCK = "LCKW"
    ACTIVE_JOB_STATUS_WAIT_LOCK_SPACE = "LSPW"
    ACTIVE_JOB_STATUS_WAIT_LOCK_SPACE_AND_ACTIVE = "LSPA"
    ACTIVE_JOB_STATUS_WAIT_MESSAGE = "MSGW"
    ACTIVE_JOB_STATUS_WAIT_MIXED_DEVICE_FILE = "MXDW"
    ACTIVE_JOB_STATUS_WAIT_MULTIPLE_FILES = "MLTW"
    ACTIVE_JOB_STATUS_WAIT_MULTIPLE_FILES_AND_ACTIVE = "MLTA"
    ACTIVE_JOB_STATUS_WAIT_MUTEX = "MTXW"
    ACTIVE_JOB_STATUS_WAIT_OPTICAL_DEVICE = "OPTW"
    ACTIVE_JOB_STATUS_WAIT_OPTICAL_DEVICE_AND_ACTIVE = "OPTA"
    ACTIVE_JOB_STATUS_WAIT_OSI = "OSIW"
    ACTIVE_JOB_STATUS_WAIT_PRESTART = "PSRW"
    ACTIVE_JOB_STATUS_WAIT_PRINT = "PRTW"
    ACTIVE_JOB_STATUS_WAIT_PRINT_AND_ACTIVE = "PRTA"
    ACTIVE_JOB_STATUS_WAIT_SAVE_FILE = "SVFW"
    ACTIVE_JOB_STATUS_WAIT_SAVE_FILE_AND_ACTIVE = "SVFA"
    ACTIVE_JOB_STATUS_WAIT_SELECTION = "SELW"
    ACTIVE_JOB_STATUS_WAIT_SEMAPHORE = "SEMW"
    ACTIVE_JOB_STATUS_WAIT_SIGNAL = "SIGW"
    ACTIVE_JOB_STATUS_WAIT_TAPE_DEVICE = "TAPW"
    ACTIVE_JOB_STATUS_WAIT_TAPE_DEVICE_AND_ACTIVE = "TAPA"
    ACTIVE_JOB_STATUS_WAIT_THREAD = "THDW"
    ACTIVE_JOB_STATUS_WAIT_TIME_INTERVAL = "TIMW"
    ACTIVE_JOB_STATUS_WAIT_TIME_INTERVAL_AND_ACTIVE = "TIMA"
    ALLOW_MULTIPLE_THREADS = 102
    ALLOW_MULTIPLE_THREADS_NO = "0"
    ALLOW_MULTIPLE_THREADS_YES = "1"
    AUXILIARY_IO_REQUESTS = 1401
    AUXILIARY_IO_REQUESTS_LARGE = 406
    BREAK_MESSAGE_HANDLING = 201
    BREAK_MESSAGE_HANDLING_HOLD = "*HOLD"
    BREAK_MESSAGE_HANDLING_NORMAL = "*NORMAL"
    BREAK_MESSAGE_HANDLING_NOTIFY = "*NOTIFY"
    CCSID = 302
    CCSID_INITIAL_USER  = - 2
    CCSID_SYSTEM_VALUE = - 1
    CHARACTER_ID_CONTROL = 311
    CHARACTER_ID_CONTROL_DEVICE = "*DEVD"
    CHARACTER_ID_CONTROL_INITIAL_USER = "*USRPRF"
    CHARACTER_ID_CONTROL_JOB = "*JOBCCSID"
    CHARACTER_ID_CONTROL_SYSTEM_VALUE = "*SYSVAL"
    CLIENT_IP_ADDRESS = 318
    COMPLETION_STATUS = 306
    COMPLETION_STATUS_COMPLETED_ABNORMALLY = "1"
    COMPLETION_STATUS_COMPLETED_NORMALLY = "0"
    COMPLETION_STATUS_NOT_COMPLETED = " "
    CONTROLLED_END_REQUESTED = 502
    COUNTRY_ID = 303
    COUNTRY_ID_INITIAL_USER = "*USRPRF"
    COUNTRY_ID_SYSTEM_VALUE = "*SYSVAL"
    CPU_TIME_USED = 304
    CPU_TIME_USED_FOR_DATABASE = 313
    CPU_TIME_USED_LARGE = 312
    CURRENT_LIBRARY = 10000
    CURRENT_LIBRARY_EXISTENCE = 10001
    CURRENT_SYSTEM_POOL_ID = 307
    CURRENT_USER = 305
    DATE_ENDED = 418
    DATE_ENTERED_SYSTEM = 402
    DATE_FORMAT = 405
    DATE_FORMAT_DMY = "*DMY"
    DATE_FORMAT_JULIAN = "*JUL"
    DATE_FORMAT_MDY = "*MDY"
    DATE_FORMAT_SYSTEM_VALUE = "*SYS"
    DATE_FORMAT_YMD = "*YMD"
    DATE_SEPARATOR = 406
    DATE_SEPARATOR_BLANK = " "
    DATE_SEPARATOR_COMMA = ","
    DATE_SEPARATOR_DASH = "-"
    DATE_SEPARATOR_PERIOD = "."
    DATE_SEPARATOR_SLASH = "/"
    DATE_SEPARATOR_SYSTEM_VALUE = "S"
    DATE_STARTED = 401
    DBCS_CAPABLE = 407
    DBCS_CAPABLE_NO = "0"
    DBCS_CAPABLE_YES = "1"
    DECIMAL_FORMAT = 413
    DECIMAL_FORMAT_COMMA_I = "I"
    DECIMAL_FORMAT_COMMA_J = "J"
    DECIMAL_FORMAT_PERIOD = ""
    DECIMAL_FORMAT_SYSTEM_VALUE = "*SYSVAL"
    DEFAULT_CCSID = 412
    DEFAULT_WAIT_TIME = 409
    DEVICE_RECOVERY_ACTION = 410
    DEVICE_RECOVERY_ACTION_DISCONNECT_END_REQUEST = "*DSCENDRQS"
    DEVICE_RECOVERY_ACTION_DISCONNECT_MESSAGE = "*DSCMSG"
    DEVICE_RECOVERY_ACTION_END_JOB = "*ENDJOB"
    DEVICE_RECOVERY_ACTION_END_JOB_NO_LIST = "*ENDJOBNOLIST"
    DEVICE_RECOVERY_ACTION_MESSAGE = "*MSG"
    DEVICE_RECOVERY_ACTION_SYSTEM_VALUE = "*SYSVAL"
    ELAPSED_CPU_PERCENT_USED = 314
    ELAPSED_CPU_PERCENT_USED_FOR_DATABASE = 316
    ELAPSED_CPU_TIME_USED = 315
    ELAPSED_CPU_TIME_USED_FOR_DATABASE = 317
    ELAPSED_DISK_IO = 414
    ELAPSED_DISK_IO_ASYNCH = 416
    ELAPSED_DISK_IO_SYNCH = 417
    ELAPSED_INTERACTIVE_RESPONSE_TIME = 904
    ELAPSED_INTERACTIVE_TRANSACTIONS = 905
    ELAPSED_LOCK_WAIT_TIME = 10008
    ELAPSED_PAGE_FAULTS = 1609
    ELAPSED_TIME = 10007
    ELIGIBLE_FOR_PURGE = 1604
    ELIGIBLE_FOR_PURGE_IGNORED = ""
    ELIGIBLE_FOR_PURGE_NO = "*NO"
    ELIGIBLE_FOR_PURGE_YES = "*YES"
    END_SEVERITY = 501
    END_STATUS_CANCELLED = "1"
    END_STATUS_JOB_NOT_RUNNING = " "
    END_STATUS_NOT_CANCELLED = "0"
    FUNCTION_NAME = 601
    FUNCTION_TYPE = 602
    FUNCTION_TYPE_BLANK = ""
    FUNCTION_TYPE_COMMAND = "C"
    FUNCTION_TYPE_DELAY = "D"
    FUNCTION_TYPE_GROUP = "G"
    FUNCTION_TYPE_INDEX = "I"
    FUNCTION_TYPE_IO = "O"
    FUNCTION_TYPE_JAVA = "J"
    FUNCTION_TYPE_LOG = "L"
    FUNCTION_TYPE_MENU = "N"
    FUNCTION_TYPE_MRT = "M"
    FUNCTION_TYPE_PROCEDURE = "R"
    FUNCTION_TYPE_PROGRAM = "P"
    FUNCTION_TYPE_SPECIAL = "*"
    INITIAL_THREAD = -1
    INQUIRY_MESSAGE_REPLY = 901
    INQUIRY_MESSAGE_REPLY_DEFAULT = "*DFT"
    INQUIRY_MESSAGE_REPLY_REQUIRED = "*RQD"
    INQUIRY_MESSAGE_REPLY_SYSTEM_REPLY_LIST = "*SYSRPYL"
    INSTANCE = 21011
    INTERACTIVE_TRANSACTIONS = 1402
    INTERNAL_JOB_ID = 11000
    INTERNAL_JOB_IDENTIFIER = 11007
    JOB_DATE = 1002
    JOB_DESCRIPTION = 1003
    JOB_END_REASON = 1014
    JOB_LOG_OUTPUT = 1018
    JOB_LOG_OUTPUT_JOB_END = "*JOBEND"
    JOB_LOG_OUTPUT_JOB_LOG_SERVER  = "*JOBLOGSVR"
    JOB_LOG_OUTPUT_PENDING = "*PND"
    JOB_LOG_OUTPUT_SYSTEM_VALUE = "*SYSVAL"
    JOB_LOG_PENDING = 1015
    JOB_LOG_PENDING_NO = "0"
    JOB_LOG_PENDING_YES = "1"
    JOB_NAME = 11001
    JOB_NAME_CURRENT = "*"
    JOB_NAME_INTERNAL = "*INT"
    JOB_NUMBER = 11002
    JOB_NUMBER_BLANK = ""
    JOB_QUEUE = 1004
    JOB_QUEUE_DATE = 404
    JOB_QUEUE_PRIORITY = 1005
    JOB_QUEUE_STATUS = 1903
    JOB_QUEUE_STATUS_BLANK = ""
    JOB_QUEUE_STATUS_HELD = "HLD"
    JOB_QUEUE_STATUS_READY = "RLS"
    JOB_QUEUE_STATUS_SCHEDULED = "SCD"
    JOB_STATUS = 11003
    JOB_STATUS_ACTIVE = "*ACTIVE"
    JOB_STATUS_JOBQ = "*JOBQ"
    JOB_STATUS_OUTQ = "*OUTQ"
    JOB_SUBTYPE = 11004
    JOB_SUBTYPE_ALTERNATE_SPOOL_USER = "U"
    JOB_SUBTYPE_BLANK = ""
    JOB_SUBTYPE_IMMEDIATE = "D"
    JOB_SUBTYPE_MACHINE_SERVER_JOB = "F"
    JOB_SUBTYPE_MRT = "T"
    JOB_SUBTYPE_PRESTART = "J"
    JOB_SUBTYPE_PRINT_DRIVER = "P"
    JOB_SUBTYPE_PROCEDURE_START_REQUEST = "E"
    JOB_SWITCHES = 1006
    JOB_TYPE = 11005
    JOB_TYPE_AUTOSTART = "A"
    JOB_TYPE_BATCH = "B"
    JOB_TYPE_ENHANCED = 1016
    JOB_TYPE_INTERACTIVE = "I"
    JOB_TYPE_NOT_VALID = ""
    JOB_TYPE_SCPF_SYSTEM = "X"
    JOB_TYPE_SPOOLED_READER = "R"
    JOB_TYPE_SPOOLED_WRITER = "W"
    JOB_TYPE_SUBSYSTEM_MONITOR = "M"
    JOB_TYPE_SYSTEM = "S"
    JOB_USER_IDENTITY = 1012
    JOB_USER_IDENTITY_SETTING = 1013
    JOB_USER_IDENTITY_SETTING_APPLICATION = "1"
    JOB_USER_IDENTITY_SETTING_DEFAULT = "0"
    JOB_USER_IDENTITY_SETTING_SYSTEM = "2"
    KEEP_DDM_CONNECTIONS_ACTIVE = 408
    KEEP_DDM_CONNECTIONS_ACTIVE_DROP = "*DROP"
    KEEP_DDM_CONNECTIONS_ACTIVE_KEEP = "*KEEP"
    LANGUAGE_ID = 1201
    LANGUAGE_ID_INITIAL_USER = "*USRPRF"
    LANGUAGE_ID_SYSTEM_VALUE = "*SYSVAL"
    LOCATION_NAME = 21012
    LOG_CL_PROGRAMS = 1203
    LOG_CL_PROGRAMS_NO = "*NO"
    LOG_CL_PROGRAMS_YES = "*YES"
    LOGGING_LEVEL = 1202
    LOGGING_LEVEL_ALL_REQUESTS_AND_ASSOCIATED_MESSAGES = "3"
    LOGGING_LEVEL_ALL_REQUESTS_AND_MESSAGES = "4"
    LOGGING_LEVEL_MESSAGES_BY_SEVERITY = "1"
    LOGGING_LEVEL_NONE = "0"
    LOGGING_LEVEL_REQUESTS_BY_SEVERITY_AND_ASSOCIATED_MESSAGES = "2"
    LOGGING_SEVERITY = 1204
    LOGGING_TEXT = 1205
    LOGGING_TEXT_MESSAGE = "*MSG"
    LOGGING_TEXT_NO_LIST = "*NOLIST"
    LOGGING_TEXT_SECLVL = "*SECLVL"
    MAX_CPU_TIME = 1302
    MAX_TEMP_STORAGE = 1303
    MAX_TEMP_STORAGE_LARGE = 1305
    MAX_THREADS = 1304
    MEMORY_POOL = 1306
    MEMORY_POOL_BASE = "*BASE"
    MEMORY_POOL_INTERACTIVE = "*INTERACT"
    MEMORY_POOL_MACHINE = "*MACHINE"
    MEMORY_POOL_SPOOL = "*SPOOL"
    MESSAGE_QUEUE_ACTION = 1007
    MESSAGE_QUEUE_ACTION_NO_WRAP = "*NOWRAP"
    MESSAGE_QUEUE_ACTION_PRINT_WRAP = "*PRTWRAP"
    MESSAGE_QUEUE_ACTION_SYSTEM_VALUE = "*SYSVAL"
    MESSAGE_QUEUE_ACTION_WRAP = "*WRAP"
    MESSAGE_QUEUE_MAX_SIZE = 1008
    MESSAGE_REPLY = 1307
    MESSAGE_REPLY_NOT_IN_MESSAGE_WAIT = "0"
    MESSAGE_REPLY_NOT_WAITING = "2"
    MESSAGE_REPLY_WAITING = "1"
    MODE = 1301
    NETWORK_ID = 21013
    OUTPUT_QUEUE = 1501
    OUTPUT_QUEUE_DEVICE = "*DEV"
    OUTPUT_QUEUE_INITIAL_USER = "*USRPRF"
    OUTPUT_QUEUE_PRIORITY = 1502
    OUTPUT_QUEUE_WORK_STATION = "*WRKSTN"
    PRINT_KEY_FORMAT = 1601
    PRINT_KEY_FORMAT_ALL = "*PRTALL"
    PRINT_KEY_FORMAT_BORDER = "*PRTBDR"
    PRINT_KEY_FORMAT_HEADER = "*PRTHDR"
    PRINT_KEY_FORMAT_NONE = "*NONE"
    PRINT_KEY_FORMAT_SYSTEM_VALUE = "*SYSVAL"
    PRINT_TEXT = 1602
    PRINT_TEXT_BLANK = "*BLANK"
    PRINT_TEXT_SYSTEM_VALUE = "*SYSVAL"
    PRINTER_DEVICE_NAME = 1603
    PRINTER_DEVICE_NAME_INITIAL_USER = "*USRPRF"
    PRINTER_DEVICE_NAME_SYSTEM_VALUE = "*SYSVAL"
    PRINTER_DEVICE_NAME_WORK_STATION = "*WRKSTN"
    PRODUCT_LIBRARIES = 10002
    PRODUCT_RETURN_CODE = 1605
    PROGRAM_RETURN_CODE = 1606
    ROUTING_DATA = 1803
    RUN_PRIORITY = 1802
    SCHEDULE_DATE = 1920
    SCHEDULE_DATE_CURRENT = "*CURRENT"
    SCHEDULE_DATE_FRIDAY = "*FRI"
    SCHEDULE_DATE_MONDAY = "*MON"
    SCHEDULE_DATE_MONTH_END = "*MONTHEND"
    SCHEDULE_DATE_MONTH_START = "*MONTHSTR"
    SCHEDULE_DATE_SATURDAY = "*SAT"
    SCHEDULE_DATE_SUNDAY = "*SUN"
    SCHEDULE_DATE_THURSDAY = "*THU"
    SCHEDULE_DATE_TUESDAY = "*TUE"
    SCHEDULE_DATE_WEDNESDAY = "*WED"
    SCHEDULE_TIME = 1921
    SCHEDULE_TIME_CURRENT = "*CURRENT"
    SEQUENCE_NUMBER = 21014
    SERVER_TYPE = 1911
    SIGNED_ON_JOB = 701
    SIGNED_ON_JOB_FALSE = "1"
    SIGNED_ON_JOB_TRUE = "0"
    SORT_SEQUENCE_TABLE = 1901
    SORT_SEQUENCE_TABLE_INITIAL_USER = "*USRPRF"
    SORT_SEQUENCE_TABLE_LANGUAGE_SHARED_WEIGHT = "*LANGIDSHR"
    SORT_SEQUENCE_TABLE_LANGUAGE_UNIQUE_WEIGHT = "*LANGIDUNQ"
    SORT_SEQUENCE_TABLE_NONE = "*HEX"
    SORT_SEQUENCE_TABLE_SYSTEM_VALUE = "*SYSVAL"
    SPECIAL_ENVIRONMENT = 1908
    SPECIAL_ENVIRONMENT_NONE = "*NONE"
    SPECIAL_ENVIRONMENT_NOT_ACTIVE = ""
    SPECIAL_ENVIRONMENT_SYSTEM_36 = "*S36"
    SPOOLED_FILE_ACTION = 1982
    SPOOLED_FILE_ACTION_DETACH = "*DETACH"
    SPOOLED_FILE_ACTION_KEEP = "*KEEP"
    SPOOLED_FILE_ACTION_SYSTEM_VALUE = "*SYSVAL"
    STATUS_MESSAGE_HANDLING = 1902
    STATUS_MESSAGE_HANDLING_INITIAL_USER = "*USRPRF"
    STATUS_MESSAGE_HANDLING_NONE = "*NONE"
    STATUS_MESSAGE_HANDLING_NORMAL = "*NORMAL"
    STATUS_MESSAGE_HANDLING_SYSTEM_VALUE = "*SYSVAL"
    SUBMITTED_BY_JOB_NAME = 1904
    SUBMITTED_BY_JOB_NUMBER = 10005
    SUBMITTED_BY_USER = 10006
    SUBSYSTEM = 1906
    SYSTEM_LIBRARY_LIST = 10003
    SYSTEM_POOL_ID = 1907
    TEMP_STORAGE_USED = 2004
    TEMP_STORAGE_USED_LARGE = 2009
    THREAD_COUNT = 2008
    TIME_SEPARATOR = 2001
    TIME_SEPARATOR_BLANK = " "
    TIME_SEPARATOR_COLON = ":"
    TIME_SEPARATOR_COMMA = ","
    TIME_SEPARATOR_PERIOD = "."
    TIME_SEPARATOR_SYSTEM_VALUE = "S"
    TIME_SLICE = 2002
    TIME_SLICE_END_POOL = 2003
    TIME_SLICE_END_POOL_BASE = "*BASE"
    TIME_SLICE_END_POOL_NONE = "*NONE"
    TIME_SLICE_END_POOL_SYSTEM_VALUE = "*SYSVAL"
    TOTAL_RESPONSE_TIME = 1801
    UNIT_OF_WORK_ID = 2101
    USER_LIBRARY_LIST = 10004
    USER_NAME = 11006
    USER_NAME_BLANK =  ""
    USER_RETURN_CODE = 2102

    def __init__(self, system, jobname=None, jobuser=None, jobnumber=None):

        self.job = jpype.JClass('com.ibm.as400.access.Job')
        self.CallStackEntry = jpype.JClass('com.ibm.as400.access.CallStackEntry')
        self.stack = jpype.JClass('com.ibm.as400.access.CallStackEntry')

        if jobname == None:
            self.job =self.job(system)
        else:
            self.job = self.job(system, jobname, jobuser, jobnumber)



        # Inicializo el constructor del JobLog
        #JobLog.__init__(self, self.system)



    # *** probar
    # obtiene un valor que representa cómo este trabajo maneja los mensajes de interrupción.
    def getJobBreakMessageHandling(self):

        """
        Cómo maneja este trabajo los mensajes de interrupción. Los valores posibles son:
        BREAK_MESSAGE_HANDLING_NORMAL
                El estado de la cola de mensajes determina el manejo de los mensajes de interrupción.

        BREAK_MESSAGE_HANDLING_HOLD
            La cola de mensajes contiene mensajes de interrupción hasta que un usuario o programa los solicita.
            El usuario de la estación de trabajo utiliza el comando Mostrar mensaje (DPSMSG) para mostrar los mensajes;
            un programa debe emitir un comando Recibir mensaje (RCVMSG) para recibir un mensaje y manejarlo.

        BREAK_MESSAGE_HANDLING_NOTIFY
            El sistema notifica a la cola de mensajes del trabajo cuando llega un mensaje.
            Para trabajos interactivos, la alarma audible suena si hay una y la luz de mensaje en espera se enciende.

        retorna un string
        """
        break_message_handling = {
            self.BREAK_MESSAGE_HANDLING_NORMAL : 'BREAK_MESSAGE_HANDLING_NORMAL',
            self.BREAK_MESSAGE_HANDLING_HOLD : 'BREAK_MESSAGE_HANDLING_HOLD',
            self.BREAK_MESSAGE_HANDLING_NOTIFY:  'BREAK_MESSAGE_HANDLING_NOTIFY'
        }


        return break_message_handling[self.job.getBreakMessageHandling()]

    # ***
    # obtiene el nombre del job
    def getJobName(self):

        """
        retorna un string
        """
        return self.job.getName()

    # ***
    # obtiene el número de solicitudes de E/S auxiliares realizadas por el trabajo
    # en todos los pasos de enrutamiento.
    def getJobAuxiliaryIORequests(self):

        """
        Devuelve el número de solicitudes de E/S auxiliares realizadas por el trabajo en todos los pasos de enrutamiento.
        Esto incluye la paginación de bases de datos y no bases de datos.
        Si el número de solicitudes de E/S auxiliares es mayor o igual a 2 147 483 647,
        se devuelve un valor de -1.
        Utilice el atributo AUXILIARY_IO_REQUESTS_LARGE para recuperar valores mayores o iguales a 2.147.483.647.

        retorna un integer

        """
        # se obtien el valor por default
        valor = self.job.getAuxiliaryIORequests()

        if valor == -1:
            valor = self.job.getAuxiliaryIORequests(self.job.AUXILIARY_IO_REQUESTS_LARGE)

        return valor


    # ***
    # Indica si los cambios del valor del atributo se almacenan en caché.
    def getJobCacheChanges(self):

        """
        retorna un boolen
        """
        return self.job.getCacheChanges()

    # ***
    # obtenemos la pila de llamadas para el subproceso especificado en este trabajo.
    def getJobCallStack(self, threadID):

        """
        retorna un objeto tipo CallStackEntry
        """
        return list(self.job.getCallStack(threadID))

    # *** probar
    # obtiene el identificador de juego de caracteres codificado (CCSID) utilizado para este trabajo.
    def getJobCodedCharacterSetID(self):

        """
        retorna un integer
        """
        return self.job.getCodedCharacterSetID()

    # ***
    # obtiene el estado de finalización del trabajo.
    def getJobCompletionStatus(self):

        """
        retorna un string
        """
        return self.job.getCompletionStatus()

    # ***
    # obtiene el identificador de país o región asociado con este trabajo.
    def getJobCountryID(self):

        """
        retorna un string
        """

        return self.job.getCountryID()

    # ***
    # obtiene la cantidad de tiempo de unidad de procesamiento (en milisegundos) que utilizó el trabajo.
    def getJobCPUUsed(self):

        """
        retorna un integer
        """
        return self.job.getCPUUsed()

    # ***
    # obtiene el nombre de la biblioteca actual para el subproceso inicial del trabajo.
    def getJobCurrentLibrary(self):

        """
        retorna un string
        """
        return self.job.getCurrentLibrary()

    # ***
    # Indica si existe una biblioteca actual.
    def getJobCurrentLibraryExistence(self):

        """
        retorna un boolen
        """
        return self.job.getCurrentLibraryExistence()

    # ***
    # Devuelve la fecha y la hora en que se colocó el trabajo en el sistema.
    def getJobDate(self):

        """
        retorna un Date
        """
        return self.job.getDate()

    # ***
    # Devuelve el formato en el que se presentan las fechas.
    def getJobDateFormat(self):

        """
        retorna un string
        """
        return self.job.getDateFormat()

    # ***
    # Devuelve el valor utilizado para separar días, meses y años al presentar una fecha.
    def getJobDateSeparator(self):

        """
        retorna un string
        """
        return self.job.getDateSeparator()

    # ***
    # Devuelve si las conexiones que usan protocolos de administración de datos distribuidos (DDM) permanecen activas cuando no se usan.
    def getJobDDMConversationHandling(self):

        """
        retorna un string
        """
        return self.job.getDDMConversationHandling()

    # ***
    # Devuelve el formato decimal utilizado para este trabajo.
    def getJobDecimalFormat(self):

        """
        retorna un string
        """
        return self.job.getDecimalFormat()


    # ***
    # Devuelve el identificador de juego de caracteres codificado predeterminado (CCSID) utilizado para este trabajo.
    def getJobDefaultCodedCharacterSetIdentifier(self):

        """
        retorna un integer
        """
        return self.job.getDefaultCodedCharacterSetIdentifier()

    # ***
    # Devuelve el tiempo máximo predeterminado (en segundos) que un subproceso en el trabajo espera una instrucción
    # del sistema, como una instrucción de interfaz de máquina (MI) LOCK, para adquirir un recurso.
    def getJobDefaultWait(self):

        """
        retorna un integer
        """
        return self.job.getDefaultWait()

    # ***
    # Devuelve la acción realizada para los trabajos interactivos cuando se produce un error de E/S
    # para el dispositivo de programa que solicita el trabajo.
    def getJobDeviceRecoveryAction(self):

        """
        retorna un string
        """
        return self.job.getDeviceRecoveryAction()


    # ***
    # Devuelve el nivel de gravedad del mensaje de los mensajes de escape que pueden hacer que finalice un trabajo por lotes.
    def 	getJobEndSeverity(self):

        """
        retorna un integer
        """
        return self.job.getEndSeverity()


   # ***
    # Devuelve información adicional (como se describe en el atributo FUNCTION_TYPE)
    # sobre la última función de alto nivel iniciada por el subproceso inicial.
    def getJobFunctionName(self):

        """
        retorna un string
        """
        return self.job.getFunctionName()


   # ***
    # Devuelve la última función de alto nivel iniciada por el subproceso inicial.
    def getJobFunctionType(self):

        """
        retorna un string
        """
        accion = {
            self.FUNCTION_TYPE_BLANK : 'FUNCTION_TYPE_BLANK',
            self.FUNCTION_TYPE_COMMAND : 'FUNCTION_TYPE_COMMAND',
            self.FUNCTION_TYPE_DELAY : 'FUNCTION_TYPE_DELAY',
            self.FUNCTION_TYPE_GROUP : 'FUNCTION_TYPE_GROUP',
            self.FUNCTION_TYPE_INDEX : 'FUNCTION_TYPE_INDEX',
            self.FUNCTION_TYPE_JAVA : 'FUNCTION_TYPE_JAVA',
            self.FUNCTION_TYPE_LOG : 'FUNCTION_TYPE_LOG',
            self.FUNCTION_TYPE_MRT : 'FUNCTION_TYPE_MRT',
            self.FUNCTION_TYPE_MENU : 'FUNCTION_TYPE_MENU',
            self.FUNCTION_TYPE_IO : 'FUNCTION_TYPE_IO',
            self.FUNCTION_TYPE_PROCEDURE : 'FUNCTION_TYPE_PROCEDURE',
            self.FUNCTION_TYPE_PROGRAM : 'FUNCTION_TYPE_PROGRAM',
            self.FUNCTION_TYPE_SPECIAL : 'FUNCTION_TYPE_SPECIAL'
            }
        return accion[str(self.job.getFunctionType()).rstrip('\x00')]


   # ***
    # Devuelve cómo responde el trabajo a los mensajes de consulta.
    def getJobInquiryMessageReply(self):

        """
        retorna un string
        """

        accion = {
            self.INQUIRY_MESSAGE_REPLY_REQUIRED : 'INQUIRY_MESSAGE_REPLY_REQUIRED',
            self.INQUIRY_MESSAGE_REPLY_DEFAULT : 'INQUIRY_MESSAGE_REPLY_DEFAULT',
            self.INQUIRY_MESSAGE_REPLY_SYSTEM_REPLY_LIST : 'INQUIRY_MESSAGE_REPLY_SYSTEM_REPLY_LIST'
        }

        return accion[self.job.getInquiryMessageReply()]


    # ***
    # Devuelve el recuento de interacciones del operador, como presionar la tecla Intro o una tecla de función.
    def getJobInteractiveTransactions(self):

        """
        retorna un integer
        """

        return int(self.job.getInteractiveTransactions())


    # ***
    # Atributo de trabajo que representa la entrada de valor a otras API para aumentar la velocidad de localización del trabajo en el sistema.
    # El identificador no es válido después de una carga del programa inicial (IPL).
    # Si intenta utilizarlo después de una IPL, se produce una excepción.
    def getJobInternalJobIdentifier(self):

        """
        retorna un bytes
        """
        retorno = bytearray(self.job.getInternalJobIdentifier())

        lista = list()
        for x in retorno:
            lista.append(x)

        return lista

    # ***
    # Devuelve el identificador de trabajo interno.
    def getJobAccountingCode(self):

        """
        retorna un string
        """
        return self.job.getJobAccountingCode()


    # ***
    # Devuelve la fecha y la hora en que el trabajo comenzó a ejecutarse en el sistema.
    def getJobActiveDate(self):

        """
        retorna un Date
        """
        return self.job.getJobActiveDate()


    # ***
    # Devuelve la fecha que se utilizará para el trabajo.
    def getJobDate(self):

        """
        retorna un Date
        """
        return self.job.getJobDate()


    # ***
    # Devuelve el nombre de vía de acceso del sistema de archivos integrado completo para la descripción del trabajo.
    def getJobDescription(self):

        """
        retorna un string
        """
        return self.job.getJobDescription()


    # ***
    # Devuelve la fecha y la hora en que finalizó la ejecución del trabajo en el sistema.
    def getJobEndedDate(self):

        """
        retorna un Date
        """
        return self.job.getJobEndedDate()


    # ***
    # Devuelve la fecha y la hora en que se colocó el trabajo en el sistema.
    def getJobEnterSystemDate(self):

        """
        retorna un Date
        """
        return self.job.getJobEnterSystemDate()


    # ***VER
    # Devuelve el registro de trabajo.
    def getJobLog(self):

        """
        retorna un objeto JobLog
        """
        return self.job.getJobLog()


    # ***
    # Devuelve la acción a realizar cuando la cola de mensajes está llena.
    def getJobMessageQueueFullAction(self):

        """
        La acción a realizar cuando la cola de mensajes está llena. Los valores posibles son:
        MESSAGE_QUEUE_ACTION_NO_WRAP
            Cuando la cola de mensajes de trabajo esté llena, no se ajuste. Esta acción hace que el trabajo finalice.

        MESSAGE_QUEUE_ACTION_WRAP
            Cuando la cola de mensajes de trabajo esté llena, vuelva al principio y comience a llenarse nuevamente.

        MESSAGE_QUEUE_ACTION_PRINT_WRAP
            Cuando la cola de mensajes del trabajo esté llena, ajuste la cola de mensajes e imprima los mensajes que se superponen debido al ajuste.


        retorna un string
        """
        action = {
            self.MESSAGE_QUEUE_ACTION_SYSTEM_VALUE : 'MESSAGE_QUEUE_ACTION_SYSTEM_VALUE',
            self.MESSAGE_QUEUE_ACTION_NO_WRAP : 'MESSAGE_QUEUE_ACTION_NO_WRAP',
            self.MESSAGE_QUEUE_ACTION_WRAP : 'MESSAGE_QUEUE_ACTION_WRAP',
            self.MESSAGE_QUEUE_ACTION_PRINT_WRAP : 'MESSAGE_QUEUE_ACTION_PRINT_WRAP'
        }

        return action[self.job.getJobMessageQueueFullAction()]


    # ***
    # Devuelve el tamaño máximo (en megabytes) que puede tener la cola de mensajes del trabajo.
    def getJobMessageQueueMaximumSize(self):

        """
        retorna un integer
        """
        return self.job.getJobMessageQueueMaximumSize()



    # ***
    # Devuelve la fecha y la hora en que este trabajo se colocó en esta cola de trabajos.
    def getJobPutOnJobQueueDate(self):

        """
        retorna un Date
        """

        return self.job.getJobPutOnJobQueueDate()


    # ***
    # Devuelve el estado de este trabajo en la cola de trabajos.
    def getJobStatusInJobQueue(self):

        """
        retorna un string
        """
        return self.job.getJobStatusInJobQueue()


    # ***
    # Devuelve la configuración actual de los conmutadores de trabajo utilizados por este trabajo
    def getJobSwitches(self):

        """
        retorna un string
        """
        return self.job.getJobSwitches()


    # ***
    # Devuelve el identificador de idioma asociado con este trabajo.
    def getJobLanguageID(self):

        """
        retorna un string
        """
        return self.job.getLanguageID()


    # ***
    # Devuelve un valor que indica si los comandos se registran
    # o no para los programas CL que se ejecutan.
    def getJobLoggingCLPrograms(self):

        """
        retorna un string
        """
        return self.job.getLoggingCLPrograms()

    # ***
    # Devuelve qué tipo de información se registra.
    def getJobLoggingLevel(self):

        """
        Atributo de trabajo que representa qué tipo de información se registra. Los valores posibles son:
            LOGGING_LEVEL_NONE
            LOGGING_LEVEL_MESSAGES_BY_SEVERITY
            LOGGING_LEVEL_REQUESTS_BY_SEVERITY_AND_ASSOCIATED_MESSAGES
            LOGGING_LEVEL_ALL_REQUESTS_AND_ASSOCIATED_MESSAGES
            LOGGING_LEVEL_ALL_REQUESTS_AND_MESSAGES
        retorna un string
        """

        action = {
            self.LOGGING_LEVEL_NONE : 'LOGGING_LEVEL_NONE',
            self.LOGGING_LEVEL_MESSAGES_BY_SEVERITY : 'LOGGING_LEVEL_MESSAGES_BY_SEVERITY',
            self.LOGGING_LEVEL_REQUESTS_BY_SEVERITY_AND_ASSOCIATED_MESSAGES : 'LOGGING_LEVEL_REQUESTS_BY_SEVERITY_AND_ASSOCIATED_MESSAGES',
            self.LOGGING_LEVEL_ALL_REQUESTS_AND_ASSOCIATED_MESSAGES : 'LOGGING_LEVEL_ALL_REQUESTS_AND_ASSOCIATED_MESSAGES',
            self.LOGGING_LEVEL_ALL_REQUESTS_AND_MESSAGES : 'LOGGING_LEVEL_ALL_REQUESTS_AND_MESSAGES'
        }


        return action[str(self.job.getLoggingLevel())]


    # ***
    # Devuelve el nivel de gravedad que se usa junto con el nivel de registro
    # para determinar qué mensajes de error se registran en el registro del trabajo.
    def getJobLoggingSeverity(self):

        """
        retorna un integer
        """
        return self.job.getLoggingSeverity()


    # ***
    # Devuelve el nivel de texto del mensaje que se escribe en el registro de trabajo
    # cuando se registra un mensaje de acuerdo con LOGGING_LEVEL y LOGGING_SEVERITY.
    def getJobLoggingText(self):

        """

        Atributo de trabajo que representa el nivel de texto del mensaje que se escribe en el registro de trabajo
        cuando un mensaje se registra de acuerdo con LOGGING_LEVEL y LOGGING_SEVERITY. Los valores posibles son:

                LOGGING_TEXT_MESSAGE
                LOGGING_TEXT_SECLVL
                LOGGING_TEXT_NO_LIST
        retorna un string
        """

        accion = {
            self.LOGGING_TEXT_MESSAGE : 'LOGGING_TEXT_MESSAGE',
            self.LOGGING_TEXT_SECLVL: 'LOGGING_TEXT_SECLVL',
            self.LOGGING_TEXT_NO_LIST: 'LOGGING_TEXT_NO_LIST'
        }

        return accion[self.job.getLoggingText()]


    # ***
    # Devuelve el nombre de modo del dispositivo de
    # comunicaciones avanzadas programa a programa (APPC) que inició el trabajo.
    def getJobModeName(self):

        """
        retorna un string
        """
        return self.job.getModeName()

    # ***
    # Devuelve el número de trabajo.
    def getJobNumber(self):

        """
        retorna un string
        """
        return self.job.getNumber()


    # ***
    # Devuelve el número de bibliotecas en la parte del sistema
    # de la lista de bibliotecas del subproceso inicial del trabajo.
    def getJobNumberOfLibrariesInSYSLIBL(self):

        """
        retorna un integer
        """
        return self.job.getNumberOfLibrariesInSYSLIBL()


    # ***
    # Devuelve el número de bibliotecas en la parte del usuario de la
    # lista de bibliotecas para el subproceso inicial del trabajo.
    def getJobNumberOfLibrariesInUSRLIBL(self):

        """
        retorna un integer
        """
        return self.job.getNumberOfLibrariesInUSRLIBL()


    # ***
    # Devuelve el número de bibliotecas que contienen información del
    # producto para el subproceso inicial del trabajo.
    def getJobNumberOfProductLibraries(self):

        """
        retorna un integer
        """
        return self.job.getNumberOfProductLibraries()


    # ***
    # Devuelve el nombre completo de la vía de acceso del sistema de archivos integrado
    # de la cola de salida predeterminada que se utiliza para la salida en cola producida por este trabajo.
    def getJobOutputQueue(self):

        """
        retorna un string
        """
        accion = {
            self.OUTPUT_QUEUE_DEVICE : 'OUTPUT_QUEUE_DEVICE',
            self.OUTPUT_QUEUE_WORK_STATION : 'OUTPUT_QUEUE_WORK_STATION',
            self.OUTPUT_QUEUE_INITIAL_USER : 'OUTPUT_QUEUE_INITIAL_USER'
        }

        valor = self.job.getOutputQueue()
        if valor in accion:
            retorno = accion[valor]
        else:
            retorno = valor
        return retorno

    # ***
    # Devuelve la prioridad de salida para los archivos de salida en cola que produce este trabajo.
    def getJobOutputQueuePriority(self):

        """
        retorna un integer
        """
        return self.job.getOutputQueuePriority()


    # ***
    # Devuelve el identificador del grupo relacionado con el sistema
    # desde el que se asigna el almacenamiento principal del trabajo.
    def getJobPoolIdentifier(self):

        """
        retorna un integer
        """
        return self.job.getPoolIdentifier()


    # ***
    # Devuelve el dispositivo de impresora utilizado para imprimir la salida de este trabajo.
    def getJobPrinterDeviceName(self):

        """
        retorna un string
        """
        accion = {
            self.PRINTER_DEVICE_NAME_SYSTEM_VALUE : 'PRINTER_DEVICE_NAME_SYSTEM_VALUE',
            self.PRINTER_DEVICE_NAME_WORK_STATION : 'PRINTER_DEVICE_NAME_WORK_STATION',
            self.PRINTER_DEVICE_NAME_INITIAL_USER : 'PRINTER_DEVICE_NAME_INITIAL_USER'
        }

        valor = self.job.getPrinterDeviceName()
        if valor in accion:
            retorno = accion[valor]
        else:
            retorno = valor

        return retorno

    # ***
    # Devuelve un valor que indica si se proporciona información de borde
    # y encabezado cuando se presiona la tecla Imprimir.
    def getJobPrintKeyFormat(self):

        """
        retorna un string
        """
        accion = {
            self.PRINT_KEY_FORMAT_SYSTEM_VALUE : 'PRINT_KEY_FORMAT_SYSTEM_VALUE',
            self.PRINT_KEY_FORMAT_NONE : 'PRINT_KEY_FORMAT_NONE',
            self.PRINT_KEY_FORMAT_BORDER : 'PRINT_KEY_FORMAT_BORDER',
            self.PRINT_KEY_FORMAT_HEADER : 'PRINT_KEY_FORMAT_HEADER',
            self.PRINT_KEY_FORMAT_ALL : 'PRINT_KEY_FORMAT_ALL'
        }


        return accion[self.job.getPrintKeyFormat()]


    # ***
    # Devuelve la línea de texto (si existe) que se imprime en la
    # parte inferior de cada página de salida impresa para el trabajo.
    def getJobPrintText(self):

        """
        retorna un string
        """
        accion = {
            self.PRINT_TEXT_SYSTEM_VALUE : 'PRINT_TEXT_SYSTEM_VALUE',
            self.PRINT_TEXT_BLANK : 'PRINT_TEXT_BLANK'
        }

        valor = str(self.job.getPrintText())

        if valor in accion:
            retorno = accion[valor]
        else:
            retorno = valor

        return retorno

    # ***
    # Devuelve las bibliotecas que contienen información
    # del producto para el subproceso inicial del trabajo.
    def getJobProductLibraries(self):

        """
        retorna un list string
        """
        valor = self.job.getProductLibraries()

        return valor

    # ***
    # Indica si el trabajo es elegible o no para ser movido del almacenamiento
    # principal y colocado en el almacenamiento auxiliar al final
    # de un intervalo de tiempo o al entrar en una espera larga
    # (como esperar la respuesta de un usuario de la estación de trabajo).
    def getJobPurge(self):

        """
        retorna un boolean
        """

        return self.job.getPurge()


    # ***
    # Devuelve el nombre completo de la vía de acceso del sistema de archivos integrado
    # de la cola de trabajos en la que se encuentra actualmente el trabajo,
    # o en la que estaba el trabajo si está actualmente activo.
    # Este valor es para trabajos cuyo estado es *JOBQ o *ACTIVE. Para trabajos con un estado de *OUTQ,
    # el valor de este campo está en blanco.
    def getJobQueue(self):

        """
        retorna un string
        """
        return self.job.getQueue()

    # ***
    # Devuelve la prioridad de programación del trabajo en comparación
    # con otros trabajos en la misma cola de trabajos.
    def getJobQueuePriority(self):

        """
        retorna un integer
        """
        return self.job.getQueuePriority()

    # ***
    # Devuelve los datos de enrutamiento que se utilizan para determinar
    # la entrada de enrutamiento que identifica el programa que se iniciará para el paso de enrutamiento.
    def getJobRoutingData(self):

        """
        retorna un string
        """
        return self.job.getRoutingData()

    # ***
    # Devuelve la prioridad con la que se ejecuta actualmente el trabajo,
    # en relación con otros trabajos del sistema.
    def getJobRunPriority(self):

        """
        retorna un integer
        """
        return self.job.getRunPriority()

    # ***
    # Devuelve la fecha y la hora en que el trabajo está programado para activarse.
    def getJobScheduleDate(self):

        """
        retorna un date
        """
        return self.job.getScheduleDate()

    # ***
    # Indica si el trabajo debe tratarse como un usuario registrado en el sistema.
    def getJobSignedOnJob(self):

        """
        retorna un boolean
        """
        return self.job.getSignedOnJob()


    # ***
    # Devuelve el nombre de la tabla de secuencia de clasificación asociada con este trabajo.
    def getJobSortSequenceTable(self):

        """
        retorna un string
        """
        return self.job.getSortSequenceTable()


    # ***
    # Devuelve el estado de este trabajo.
    def getJobStatus(self):

        """
        retorna un string
        """

        accion = {
            self.JOB_STATUS_ACTIVE : 'JOB_STATUS_ACTIVE',
            self.JOB_STATUS_JOBQ : 'JOB_STATUS_JOBQ',
            self.JOB_STATUS_OUTQ : 'JOB_STATUS_OUTQ'
        }
        return accion[self.job.getStatus()]


    # ***
    # Devuelve si se muestran mensajes de estado para este trabajo.
    def getJobStatusMessageHandling(self):

        """
        retorna un string
        """
        accion = {
            self.STATUS_MESSAGE_HANDLING_SYSTEM_VALUE : 'STATUS_MESSAGE_HANDLING_SYSTEM_VALUE',
            self.STATUS_MESSAGE_HANDLING_INITIAL_USER : 'STATUS_MESSAGE_HANDLING_INITIAL_USER',
            self.STATUS_MESSAGE_HANDLING_NONE : 'STATUS_MESSAGE_HANDLING_NONE',
            self.STATUS_MESSAGE_HANDLING_NORMAL : 'STATUS_MESSAGE_HANDLING_NORMAL'
        }


        return accion[self.job.getStatusMessageHandling()]

    # *** ver como funciona
    # Devuelve el valor del atributo de trabajo especificado, como una cadena.
    def getJobStringValue(self, attribute):

        """
        retorna un string
        """
        return self.job.getStringValue(attribute)


    # ***
    # Devuelve el nombre de ruta completo del sistema de
    # archivos integrado de la descripción del subsistema para el subsistema en el que se ejecuta el trabajo.
    def getJobSubsystem(self):

        """
        retorna un string
        """
        return self.job.getSubsystem()

    # ***
    # Devuelve información adicional sobre el tipo de trabajo (si existe).
    def getJobSubtype(self):

        """
        retorna un string
        """

        accion = {
            self.JOB_SUBTYPE_BLANK : 'JOB_SUBTYPE_BLANK',
            self.JOB_SUBTYPE_IMMEDIATE : 'JOB_SUBTYPE_IMMEDIATE',
            self.JOB_SUBTYPE_PROCEDURE_START_REQUEST : 'JOB_SUBTYPE_PROCEDURE_START_REQUEST',
            self.JOB_SUBTYPE_MACHINE_SERVER_JOB : 'JOB_SUBTYPE_MACHINE_SERVER_JOB',
            self.JOB_SUBTYPE_PRESTART : 'JOB_SUBTYPE_PRESTART',
            self.JOB_SUBTYPE_PRINT_DRIVER : 'JOB_SUBTYPE_PRINT_DRIVER',
            self.JOB_SUBTYPE_MRT : 'JOB_SUBTYPE_MRT',
            self.JOB_SUBTYPE_ALTERNATE_SPOOL_USER : 'JOB_SUBTYPE_ALTERNATE_SPOOL_USER'
        }
        return accion[self.job.getSubtype()]


    # *** ya esta invocado
    # Devuelve el sistema
    def getJobSystem(self):

        """
        retorna un objeto AS400
        """
        return self.job.getSystem()


    # ***
    # Devuelve la parte del sistema de la lista de bibliotecas del subproceso inicial del trabajo.
    def getJobSystemLibraryList(self):

        """
        retorna una lista string
        """
        return self.job.getSystemLibraryList()


    # ***
    # Devuelve el valor utilizado para separar horas, minutos y segundos al presentar una hora.
    def getJobTimeSeparator(self):

        """
        retorna una string
        """
        accion = {
            self.TIME_SEPARATOR_SYSTEM_VALUE : 'TIME_SEPARATOR_SYSTEM_VALUE',
            self.TIME_SEPARATOR_COLON : 'TIME_SEPARATOR_COLON',
            self.TIME_SEPARATOR_PERIOD : 'TIME_SEPARATOR_PERIOD',
            self.TIME_SEPARATOR_BLANK : 'TIME_SEPARATOR_BLANK',
            self.TIME_SEPARATOR_COMMA :'TIME_SEPARATOR_COMMA'
        }

        return accion[self.job.getTimeSeparator()]

    # ***
    # Devuelve la cantidad máxima de tiempo de procesador (en milisegundos) otorgada a cada
    # subproceso en este trabajo antes de que otros subprocesos en este trabajo y
    # en otros trabajos tengan la oportunidad de ejecutarse.
    def getJobTimeSlice(self):

        """
        retorna un integer
        """
        return self.job.getTimeSlice()

    # ***
    # Devuelve un valor que indica si un subproceso en un trabajo interactivo
    # se mueve a otro grupo de almacenamiento principal al final de su intervalo de tiempo.
    def getJobTimeSliceEndPool(self):

        """
        retorna una string
        """
        accion = {
            self.TIME_SLICE_END_POOL_SYSTEM_VALUE : 'TIME_SLICE_END_POOL_SYSTEM_VALUE',
            self.TIME_SLICE_END_POOL_NONE : 'TIME_SLICE_END_POOL_NONE',
            self.TIME_SLICE_END_POOL_BASE : 'TIME_SLICE_END_POOL_BASE'
        }


        return accion[self.job.getTimeSliceEndPool()]

    # ***
    # Devuelve la cantidad total de tiempo de respuesta para el subproceso inicial, en milisegundos.
    def getJobTotalResponseTime(self):

        """
        retorna un integer
        """
        return self.job.getTotalResponseTime()

    # ***
    # Devuelve el tipo de trabajo.
    def getJobType(self):

        """
        retorna un string
        """
        accion = {
            self.JOB_TYPE_NOT_VALID : 'JOB_TYPE_NOT_VALID',
            self.JOB_TYPE_AUTOSTART : 'JOB_TYPE_AUTOSTART',
            self.JOB_TYPE_BATCH : 'JOB_TYPE_BATCH',
            self.JOB_TYPE_INTERACTIVE : 'JOB_TYPE_INTERACTIVE',
            self.JOB_TYPE_SUBSYSTEM_MONITOR : 'JOB_TYPE_SUBSYSTEM_MONITOR',
            self.JOB_TYPE_SPOOLED_READER : 'JOB_TYPE_SPOOLED_READER',
            self.JOB_TYPE_SYSTEM : 'JOB_TYPE_SYSTEM',
            self.JOB_TYPE_SPOOLED_WRITER : 'JOB_TYPE_SPOOLED_WRITER',
            self.JOB_TYPE_SCPF_SYSTEM: 'JOB_TYPE_SCPF_SYSTEM'
        }


        return accion[self.job.getType()]


    # ***
    # Devuelve el nombre de usuario.
    def getJobUser(self):

        """
        retorna un string
        """
        return self.job.getUser()


    # ***
    # Devuelve la parte del usuario de la lista de bibliotecas para el subproceso inicial del trabajo.
    def getJobUserLibraryList(self):

        """
        retorna una lista  string
        """
        return self.job.getUserLibraryList()


    # *** ver como funciona
    # Devuelve el valor del atributo de trabajo especificado.
    def getJobValue(self, attribute):

        """
        retorna un objeto
        """
        return self.job.getValue(attribute)


    # ***
    # Devuelve el identificador de la unidad de trabajo.
    def getJobWorkIDUnit(self):

        """
        retorna un string
        """

        return self.job.getWorkIDUnit()

    # *** ver
    # Tiene este trabajo spool el trabajo.
    def holdJob(self, holdSpooledFiles):

        """
        holdSpooledFiles = valor boolean
        donde indica si los spool generados por el job se los holdean
        """
        return self.job.hold(holdSpooledFiles)


    # *** ver
    # Actualiza los valores de todos los atributos.
    def loadJobInformation(self):

        """
        Actualiza los valores de todos los atributos.
        Esto no cancela los cambios no confirmados.
        Para actualizar solo las estadísticas de tiempo transcurrido, utilice loadStatistics().

        """
        return self.job.loadInformation()


    # *** ver
    # Actualiza los valores de atributos específicos.
    def loadInformationAtributes(self, attributes):

        """
        attributes es un integer
        Actualiza los valores de atributos específicos. Esto no cancela los cambios no confirmados.
        Nota: Los atributos especificados se actualizarán,
        junto con otros atributos en su "grupo de formato".
        Para obtener más información sobre los grupos de formatos de atributos,
        consulte la especificación de la API QUSRJOBI.

        """
        return self.job.loadInformation(attributes)

    # *** ver
    # Actualiza solo los valores de las estadísticas transcurridas.
    def loadJobStatistics(self):

        """
        Actualiza solo los valores de las estadísticas transcurridas.
        Internamente, esto llama a la API QUSRJOBI usando el formato JOBI1000.

        """
        return self.job.loadStatistics()


    # ***
    # Libera este trabajo.
    def releaseJob(self):

        """
        Libera este trabajo

        """
        return self.job.release()
