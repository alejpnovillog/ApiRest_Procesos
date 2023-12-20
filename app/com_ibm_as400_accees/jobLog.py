# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        from app_Config.config import ConfigurarAplicacion
        from com_ibm_as400_accees.queuedMessage import QueuedMessage

except Exception as e:
    print(f'Falta algun modulo {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Definimos la clase JobLog
class JobLog():

    ALERT_OPTION = 101
    CCSID_CONVERSION_STATUS_DATA = 1304
    CCSID_CONVERSION_STATUS_TEXT = 1302
    CCSID_FOR_DATA = 1303
    CCSID_FOR_TEXT = 1301
    DEFAULT_REPLY = 501
    MESSAGE = 301
    MESSAGE_FILE_LIBRARY_USED = 801
    MESSAGE_HELP = 401
    MESSAGE_HELP_WITH_FORMATTING_CHARACTERS = 403
    MESSAGE_HELP_WITH_REPLACEMENT_DATA = 402
    MESSAGE_HELP_WITH_REPLACEMENT_DATA_AND_FORMATTING_CHARACTERS = 404
    MESSAGE_WITH_REPLACEMENT_DATA = 302
    RECEIVING_MODULE_NAME = 704
    RECEIVING_PROCEDURE_NAME = 705
    RECEIVING_PROGRAM_NAME = 703
    RECEIVING_STATEMENT_NUMBERS = 706
    RECEIVING_TYPE = 702
    REPLACEMENT_DATA = 201
    REPLY_STATUS = 1001
    REQUEST_LEVEL = 1201
    REQUEST_STATUS = 1101
    SENDER_TYPE = 602
    SENDING_MODULE_NAME = 604
    SENDING_PROCEDURE_NAME = 605
    SENDING_PROGRAM_NAME = 603
    SENDING_STATEMENT_NUMBERS = 606
    SENDING_USER_PROFILE = 607

    def __init__(self, system, jobName, jobUser, jobNumber):

        self.jobLog = jpype.JClass('com.ibm.as400.access.JobLog')
        self.Enumerate = jpype.JClass('java.util.Enumeration')
        self.jobLog = self.jobLog(system, jobName, jobUser, jobNumber)


    # Agrega un atributo de mensaje que se recuperará para cada registro de trabajo.
    def addJobLogAttributeToRetrieve(self, atribute):
        """
            Este método permite que los objetos de registro de trabajo que se recuperan de
            esta lista de registro de trabajo tengan algunos de sus atributos de mensaje elegidos por la persona que llama.
            La lista de atributos del mensaje se mantiene internamente incluso cuando esta JobList
            se cierra y se reutiliza. Para comenzar de nuevo con un nuevo conjunto de atributos de trabajo para recuperar,
            llame al clearAttributesToRetrieve(). Esto establecerá todos los atributos en nulo, incluidos los atributos predeterminados.


        """
        self.jobLog.addAttributeToRetrieve(atribute)

    # Agrega un PropertyChangeListener.
    def addJobLogPropertyChangeListener(self, oyente):
        """
            Se llamará al método propertyChange() del PropertyChangeListener
            especificado cada vez que se cambie el valor de cualquier propiedad enlazada.

        """
        self.jobLog.addPropertyChangeListener(oyente)

    # Agrega un VetoableChangeListener.
    def addJobLogVetoableChangeListener(self, oyente):
        """
            Se llamará al método vetoableChange() de VetoableChangeListener
            especificado cada vez que se cambie el valor de cualquier propiedad restringida.

        """
        self.jobLog.addVetoableChangeListener(oyente)


    # Borra los atributos del mensaje que se recuperarán para un registro de trabajo determinado.
    def clearJobLogAttributesToRetrieve(self):
        """
            Esto elimina todos los atributos del registro de trabajo que se recuperarían,
            incluidos los atributos de mensaje predeterminados. Si se borran todos los atributos del mensaje,
            se debe llamar a addAttributeToRetrieve o se lanzará una excepción.

        """
        self.jobLog.clearAttributesToRetrieve()

    # Cierra la lista de mensajes en el sistema.
    # Esto libera cualquier recurso del sistema que esta lista de mensajes haya utilizado previamente.
    def closeJobLog(self):

        self.jobLog.close()


    # Cierra la lista en el sistema cuando este objeto se recolecta como basura.
    def finalizeJobLog(self):

        self.jobLog.finalize()


    # Devuelve el número de mensajes en el registro de trabajo.
    def getJobLogLength(self):

        return self.jobLog.getLength()

    # Devuelve la dirección de la lista.
    def getJobLogListDirection(self):

        """
        True si los mensajes se ordenarán del más antiguo al más reciente;
        False si se ordenarán del más nuevo al más antiguo.
        El default es True.

        """

        return self.jobLog.getListDirection()

    # Devuelve la lista de mensajes en el registro de trabajo.
    def getJobLogMessages(self):
        """
            Una enumeración de objetos QueuedMessage .

        """
        for m in list(self.jobLog.getMessages()):
            self.qm = QueuedMessage(m)
            print(f'Message =  ({self.qm.toQMString()})')
            print(f'Desde el Program = ({self.qm.getQMFromProgram()})')

        return

    # Devuelve el nombre del trabajo.
    def getJobLogName(self):

        """
            El nombre del trabajo, o "*" si no se ha establecido ninguno.

            return string
        """
        return self.jobLog.getName()


    # Devuelve el número de trabajo.
    def getJobLogNumber(self):

        """
            El número de trabajo, o "" si no se ha configurado ninguno.

            return string

        """

        return self.jobLog.getNumber()


    # Devuelve la clave del mensaje inicial.
    def getJobLogStartingMessageKey(self):
        """
                devuelve la clave

                return lista con el el contenido del array byte
        """
        retorno = self.jobLog.getStartingMessageKey()
        if retorno == None:
            return retorno

        lista = list()
        for x in retorno:
            lista.append(x)

        return lista

    # Carga la lista de mensajes en el sistema.
    def loadJobLog(self):

        """
            Este método informa al sistema para construir una lista de mensajes.
            Este método bloquea hasta que el sistema devuelve el número total de mensajes que ha compilado.
            Una llamada posterior a getMessages()recuperará la información y
            los atributos reales del mensaje para cada mensaje en la lista del sistema.
            Este método actualiza la longitud de la lista.

        """
        return self.jobLog.load()

    # Agrega un PropertyChangeListener.
    # Se llamará al método propertyChange() del PropertyChangeListener
    # especificado cada vez que se cambie el valor de cualquier propiedad enlazada.
    def addJobLogPropertyChangeListener(self, oyente):

        """
            Se llamará al método propertyChange() del PropertyChangeListener
            especificado cada vez que se cambie el valor de cualquier propiedad enlazada.

        """
        return self.jobLog.addPropertyChangeListener()

    # Agrega un VetoableChangeListener.
    def addJobLogVetoableChangeListener(self, oyente):

        """
            Se llamará al método vetoableChange() de VetoableChangeListener
            especificado cada vez que se cambie el valor de cualquier propiedad restringida.

        """

        return self.jobLog.addVetoableChangeListener()


    # Establece la dirección de la lista.
    def setJobLogListDirection(self, valor):

        """
            listDirection- true para ordenar los mensajes más antiguos a los más nuevos;
            false para ordenarlos del más nuevo al más antiguo. El defecto es cierto.

        """
        return self.jobLog.setListDirection()


    # Establece el nombre del trabajo.
    def setJobLogName(self, valor):

        """
            Esto no se puede cambiar si el objeto ha establecido una conexión con el sistema.

        """
        self.jobLog.setName(valor)

    # Establece el número de trabajo.
    def setJobLogNumber(self, valor):

        """
            Esto no se puede cambiar si el objeto ha establecido una conexión con el sistema.

        """
        self.jobLog.setNumber(valor)


    # Establece la clave de mensaje que se utiliza para comenzar a buscar mensajes en la lista de la entrada
    def setJobLogStartingMessageKey(self, valor):

        """
            correspondiente en el registro de trabajo. Cualquier tecla de mensaje válida funcionará,
            incluidos MessageQueue.OLDESTy MessageQueue#NEWEST.

            el parametro recibido es una lista y se convierte a bytearray

        """
        valorbytes = bytearray(valor)

        self.jobLog.setStartingMessageKey(valorbytes)

    # Establece el sistema.
    def setJobLogSystem(self, valor):

        """
            Esto no se puede cambiar si el objeto ha establecido una conexión con el sistema.
        """
        self.jobLog.setSystem(valor)


    # Establece el nombre de usuario del trabajo.
    def setJobLogUser(self, valor):

        """
          Esto no se puede cambiar si el objeto ha establecido una conexión con el sistema.
        """

        self.jobLog.setUser(valor)

    # Escribe un mensaje de programa en el registro de trabajo para el trabajo en el que se está ejecutando el programa.
    def  writeJobLogMessage(self, system=None, messageid=None, messagetype=None, messagefile=None, sustitutiondata = None, thread = None):

        """
                El mensaje se envía al servidor host de comandos remotos (QZRCSRVS) a menos que se especifique verdadero
                para el parámetro onThread y se invoque mientras se ejecuta en el sistema.

                system- El sistema. El sistema no puede ser nulo.
                messageID- El ID del mensaje. El ID del mensaje no puede ser nulo.
                messageType- El tipo de mensaje. Los valores posibles son:
                    AS400Message.COMPLETION
                    AS400Mensaje.DIAGNOSTICO
                    AS400Message.INFORMATIONAL
                    AS400Message.ESCAPE

                El tipo de mensaje debe ser AS400Message.INFORMATIONAL para un mensaje inmediato.
                messageFile- El nombre de vía de acceso del sistema de archivos integrado del archivo de mensajes.
                        Si se especifica nulo, el archivo de mensajes utilizado es /QSYS.LIB/QCPFMSG.MSGF.
                substitutionData- Los datos de sustitución.
                        Los datos de sustitución pueden ser de 0-32767 bytes para un mensaje convencional y
                        de 1-6000 bytes para un mensaje inmediato.
                        Si se especifica nulo, no se utilizan datos de sustitución.
                onThread- Si permanecer o no en el hilo al llamar a la API para escribir el mensaje en el registro de trabajo.
                        true para escribir el mensaje en el registro de trabajo del trabajo actual,
                        false para escribir el mensaje en el registro de trabajo del servidor host de comandos remotos.
                        Tenga en cuenta que este parámetro no tiene sentido a menos que este programa Java se esté ejecutando
                        en el sistema y el objeto del sistema esté utilizando optimizaciones nativas.

        """

        if messagefile == None and sustitutiondata == None and thread == None:
            self.jobLog.writeMessage(system, messageid, messagetype)

        if  messagefile == None and  thread == None and  sustitutiondata != None:
            self.jobLog.writeMessage(system, messageid, messagetype, sustitutiondata)

        if messagefile != None and sustitutiondata == None:
            self.jobLog.writeMessage(system, messageid, messagetype, messagefile)

        if messagefile != None and sustitutiondata != None:
            self.jobLog.writeMessage(system, messageid, messagetype, messagefile, sustitutiondata)

        if messagefile != None and sustitutiondata != None and thread != None:
            self.jobLog.writeMessage(system, messageid, messagetype, messagefile, sustitutiondata, thread)
