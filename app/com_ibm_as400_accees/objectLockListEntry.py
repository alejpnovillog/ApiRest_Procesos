try:
        import jpype
        import os

except Exception as e:
    print(f'Falta algun modulo {e}')

class ObjectLockListEntry():


    # Atributos
    JOB_NAME_LOCK_SPACE = "*LCKSPC"
    JOB_NAME_MACHINE = "MACHINE"
    LOCK_SCOPE_JOB = 0
    LOCK_SCOPE_LOCK_SPACE = 2
    LOCK_SCOPE_THREAD = 1
    LOCK_SHARE_FILE_NOT_SHARED = 0
    LOCK_SHARE_FILE_SHARED = 1
    LOCK_STATE_EXCLUSIVE_ALLOW_READ = "*EXCLRD"
    LOCK_STATE_EXCLUSIVE_NO_READ = "*EXCL"
    LOCK_STATE_NONE = "*NONE"
    LOCK_STATE_SHARED_NO_UPDATE = "*SHRNUP"
    LOCK_STATE_SHARED_READ = "*SHRRD"
    LOCK_STATE_SHARED_UPDATE = "*SHRUPD"
    LOCK_STATUS_JOB_THREAD_WAITING_SYNC = 2
    LOCK_STATUS_LOCK_HELD = 1
    LOCK_STATUS_LOCK_REQUEST_OUTSTANDING_ASYNC = 3
    LOCK_TYPE_ACCESS_PATH = 3
    LOCK_TYPE_DATA_WITHIN_MEMBER = 4
    LOCK_TYPE_MEMBER_CONTROL_BLOCK = 2
    LOCK_TYPE_OBJECT = 1
    VALUE_CANNOT_BE_DETERMINED  = "*N"

    # Constructor
    def __init__(self):

        """
        String = getJobName()
                Devuelve el nombre de trabajo simple del trabajo que emitió la solicitud de bloqueo.

        String = getJobNumber()
                El número de trabajo asignado por el sistema del trabajo que emitió la solicitud de bloqueo.

        String = getJobUserName()
                El nombre de usuario con el que se ejecuta el trabajo que emitió la solicitud de bloqueo.

        integer = getLockScope()
                Devuelve el valor que indica el alcance del bloqueo.

        String = getLockState()
                Devuelve el valor que indica el estado de bloqueo.

        integer = getLockStatus()
                Devuelve el valor que indica el estado de bloqueo.

        integer = getLockType()
                Devuelve el valor que indica el tipo de bloqueo.

        integer = getShare()
                Share.

        long	= getThreadID()
                El identificador del subproceso que contiene un bloqueo de
                ámbito de subproceso o espera un bloqueo.

        String = toString()
                Devuelve una representación de cadena de este bloqueo de objeto.

        """
        self.objectLockListEntry = jpype.JClass('com.ibm.as400.access.ObjectLockListEntry')

