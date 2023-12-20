# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        import datetime

except Exception as e:
    print(f'Falta algun modulo {e}')


class HistoryLog():

    AVAIL = "*AVAIL"
    BEGIN	 = "*BEGIN"
    CURRENT_DATE = "*CURRENT"
    END = "*END"
    OMIT = 1
    SELECT = 0
    TYPE_COMPLETION	 = "*COMP"
    TYPE_COPY = "*COPY"
    TYPE_DIAGNOSTIC = "*DIAG"
    TYPE_ESCAPE = "*ESCAPE"
    TYPE_INFORMATIONAL = "*INFO"
    TYPE_INQUIRY = "*INQ"
    TYPE_NOTIFY = "*NOTIFY"
    TYPE_REPLY = "*RPY"
    TYPE_REQUEST	 = "*RQS"



    def __init__(self, system):

        """

        protected void	finalize()
        Cierra la lista en el sistema cuando este objeto se recolecta como basura.







        QueuedMessage[]	getMessages(int listOffset, int number)
        Devuelve un subconjunto de la lista de mensajes en el registro del historial.




        AS400	getSystem()
        Devuelve el objeto del sistema que representa el sistema en el que existe el registro histórico.




        void	setMessageIDs(java.lang.String[] ids)
        Especifica los ID de mensajes específicos que se recuperarán u omitirán.

        void	setMessageIDsListIndicator(int indicator)
        Especifica si los ID de mensaje de la lista se deben omitir o seleccionar.



        void	setMessageTypes(java.lang.String[] types)
        Especifica los tipos de mensajes específicos que se recuperarán u omitirán.


        void	setStartingDate(java.lang.String date, java.lang.String time)
        Especifica la fecha y la hora de inicio de la lista de mensajes y trabajos.

        void	setEndingDate(java.lang.String date, java.lang.String time)
        Especifica la fecha y hora de finalización para que se enumeren los mensajes y trabajos.


        """



        # asigna la clase java de User
        self.Enumerate = jpype.JClass('java.util.Enumeration')
        self.historylog = jpype.JClass('com.ibm.as400.access.HistoryLog')
        self.historylog = self.historylog(system)
        self.fechamessage = jpype.JClass('java.util.Date')

    # ***
    # Devuelve el número de mensajes en el registro del historial.
    def getHLLength(self):

        """
        Devuelve el número de mensajes en el registro del historial.
        int	getLength()

        """
        return self.historylog.getLength()


    # ***
    # Devuelve la lista de mensajes en el registro histórico.
    def getHLMessages(self):

        """
        Devuelve la lista de mensajes en el registro histórico.
        java.util.Enumeration = 	getMessages()

        """
        return list(self.historylog.getMessages())


    # ***
    # Devuelve la lista de ID de mensajes utilizados para filtrar qué mensajes se enumeran en el registro.
    def getHLMessageIDs(self):

        """
        Devuelve la lista de ID de mensajes utilizados para filtrar qué mensajes se enumeran en el registro.
        java.lang.String[] = getMessageIDs()

        """
        return list(self.historylog.getMessageIDs())


    # ***
    # Devuelve la lista de trabajos utilizados para filtrar qué mensajes se enumeran en el registro.
    def getHLgetJobs(self):

        """
        Devuelve la lista de trabajos utilizados para filtrar qué mensajes se enumeran en el registro.
        Job[]  = getJobs()

        """
        return list(self.historylog.getJobs())



    # ***
    # Devuelve la fecha de inicio de la lista de mensajes y trabajos.
    def getHLStartingDate(self):

        """
            Devuelve la fecha de inicio de la lista de mensajes y trabajos.
            java.util.Date = getStartingDate()


        """
        valor = self.historylog.getStartingDate()
        return self.historylog.getStartingDate()


    # ***
    # Devuelve la fecha de finalización de la lista de mensajes y trabajos.
    def getHLEndingDate(self):

        """
        Devuelve la fecha de finalización de la lista de mensajes y trabajos.
        java.util.Date = getEndingDate()

        """
        return self.historylog.getEndingDate()


    # ***
    # Devuelve el indicador de lista que indica si los ID de mensaje de la lista se omiten o se seleccionan.
    def getHLMessageIDsListIndicator(self):

        """
        Devuelve el indicador de lista que indica si los ID de mensaje de la lista se omiten o se seleccionan.
        int = getMessageIDsListIndicator()

        """

        return self.historylog.getMessageIDsListIndicator()


    # ***
    # Devuelve el indicador de lista que indica si los tipos de mensaje de la lista deben omitirse o seleccionarse.
    def getHLMessageTypeListIndicator(self):

        """
        Devuelve el indicador de lista que indica si los tipos de mensaje de la lista deben omitirse o seleccionarse.
        int = getMessageTypeListIndicator()


        """
        return self.historylog.getMessageTypeListIndicator()


    # ***
    # Devuelve los tipos de mensajes que se seleccionarán u omitirán de la lista.
    def getHLMessageTypes(self):
        """
        Devuelve los tipos de mensajes que se seleccionarán u omitirán de la lista.

        java.lang.String[] = getMessageTypes()

        """
        return self.historylog.getMessageTypes()


    # ***
    # Devuelve la gravedad mínima de los mensajes a listar.
    def getHLMessageSeverity(self):

        """
        Devuelve la gravedad mínima de los mensajes a listar.

        int = getMessageSeverity()

        """
        return self.historylog.getMessageSeverity()


    # ***
    # Especifica la fecha y la hora de inicio de la lista de mensajes y trabajos.
    def setHLStartingDate(self):

        """
        Especifica la fecha y la hora de inicio de la lista de mensajes y trabajos.
        setStartingDate(java.util.Date date)

        """
        # self.fechamessage = fecha
        self.historylog.setStartingDate(self.CURRENT_DATE, '000000')


    # ***
    # Especifica la fecha y hora de finalización para que se enumeren los mensajes y trabajos.
    def setHLEndingDate(self):

        """
        Especifica la fecha y hora de finalización para que se enumeren los mensajes y trabajos.
        setEndingDate(java.util.Date date)

        """
        # self.fechamessage = fecha
        self.historylog.setEndingDate(self.CURRENT_DATE, self.AVAIL)


    # ***
    # Carga la lista de mensajes en el sistema.
    def loadHL(self):

        """
        Carga la lista de mensajes en el sistema. que estan seteados
        void	load()

        """
        self.historylog.load()


    # ***
    # Cierra la lista de mensajes en el sistema.
    def closeHL(self):

        """
        Cierra la lista de mensajes en el sistema.
        void	close()

        """
        self.historylog.close()


    # ***
    # La gravedad mínima de los mensajes que se enumerarán.
    def setHLMessageSeverity(self, gravedad):
        """
        La gravedad mínima de los mensajes que se enumerarán.
        void	setMessageSeverity(int severity)

        """
        self.historylog.setMessageSeverity(gravedad)



    # ***
    # Especifica si los tipos de mensajes de la lista deben omitirse o seleccionarse.
    def setHLMessageTypeListIndicator(self, tipomessage):

        """
        Especifica si los tipos de mensajes de la lista deben omitirse o seleccionarse.
        void	setMessageTypeListIndicator(int indicator)

        """
        self.historylog.setMessageTypeListIndicator(tipomessage)


    #  ***
    # Especifica los trabajos específicos (si los hay) para los que se enumeran los mensajes en el registro.
    def setHLJobs(self, listajob):

        """
        Especifica los trabajos específicos (si los hay) para los que se enumeran los mensajes en el registro.
        void	setJobs(Job[] jobs)

        """
        self.historylog.setJobs(listajob)