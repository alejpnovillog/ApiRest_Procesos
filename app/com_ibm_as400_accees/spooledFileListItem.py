# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os


except Exception as e:
    print(f'Falta algun modulo {e}')


class SpooledFileListItem():

    ASP = 14
    COPIES_LEFT_TO_PRINT	 = 18
    CURRENT_PAGE = 22
    DATE_OPENED = 6
    DEVICE_TYPE = 23
    FORM_TYPE = 11
    FORMAT_0100	 = "OSPL0100"
    FORMAT_0200	 = "OSPL0200"
    FORMAT_0300	= "OSPL0300"
    JOB_NAME =	0
    JOB_NUMBER = 2
    JOB_SYSTEM = 9
    JOB_USER = 1
    NAME = 3
    NUMBER = 4
    OUTPUT_QUEUE_LIBRARY = 13
    OUTPUT_QUEUE_NAME = 12
    PRINTER_ASSIGNED	 = 21
    PRINTER_NAME = 20
    PRIORITY = 19
    SCHEDULE = 8
    SIZE = 15
    STATUS = 5
    TIME_OPENED = 7
    TOTAL_PAGES = 17
    USER_DATA = 10


    def __init__(self):

        """

            byte[]	getInternalJobIdentifier()
            Devuelve el identificador de trabajo interno para el trabajo que creó el archivo en spool.

            byte[]	getInternalSpooledFileIdentifier()
            Devuelve el identificador de archivo en spool interno para el archivo en spool.

            int	getIPPJobIdentifier()
            Devuelve el identificador de trabajo del Protocolo de impresión de Internet (IPP) asignado por el sistema en función de la cola de salida a la que se agregó o movió el archivo.


        """

        self.spoolfilelistitem = jpype.JClass('com.ibm.as400.access.list.SpooledFileListItem')


    # ***
    # Devuelve el número restante de copias para imprimir.
    def getSPLLSTITMCopiesLeftToPrint(self):

        """
            Devuelve el número restante de copias para imprimir.

            int = getCopiesLeftToPrint()

        """
        return self.spoolfilelistitem.getCopiesLeftToPrint()


    # ***
    # Devuelve la fecha y la hora en que se creó el archivo en spool.
    def getSPLLSTITMCreationDate(self):

        """
            Devuelve la fecha y la hora en que se creó el archivo en spool.

            java.util.Date = 	getCreationDate()

        """
        return self.spoolfilelistitem.getCreationDate()


    # ***
    # Devuelve el número de página o el número de registro que se está escribiendo actualmente.
    def getSPLLSTITMCurrentPage(self):

        """
            Devuelve el número de página o el número de registro que se está escribiendo actualmente.

            int = getCurrentPage()

        """
        return self.spoolfilelistitem.getCurrentPage()



    # ***
    # Devuelve la fecha en que se creó el archivo en spool.
    def getSPLLSTITMDateOpened(self):

        """
            Devuelve la fecha en que se creó el archivo en spool.

            java.lang.String = getDateOpened()

        """
        return self.spoolfilelistitem.getDateOpened()



    # ***
    # Devuelve el tipo de dispositivo para el que está destinado el archivo en spool.
    def getSPLLSTITMDeviceType(self):

        """
            Devuelve el tipo de dispositivo para el que está destinado el archivo en spool.

            java.lang.String = getDeviceType()

        """
        return self.spoolfilelistitem.getDeviceType()



    # ***
    # Devuelve el formato que utilizó SpooledFileOpenList para generar este elemento.
    def getSPLLSTITMFormat(self):

        """
            Devuelve el formato que utilizó SpooledFileOpenList para generar este elemento.

            java.lang.String = getFormat()

        """
        return self.spoolfilelistitem.getFormat()


    # ***
    # Devuelve el tipo de formularios que deben cargarse en la impresora
    # antes de que se imprima este archivo en cola.
    def getSPLLSTITMFormType(self):

        """
            Devuelve el tipo de formularios que deben cargarse en la impresora
            antes de que se imprima este archivo en cola.

            java.lang.String = getFormType()

        """
        return self.spoolfilelistitem.getFormType()



    # ***
    # Devuelve la vía de acceso del sistema de archivos integrado completamente
    # calificada de la cola de salida en la que se encuentra el archivo en spool.
    def getSPLLSTITMOutputQueue(self):

        """
            Devuelve la vía de acceso del sistema de archivos integrado completamente
            calificada de la cola de salida en la que se encuentra el archivo en spool.

            java.lang.String =	getOutputQueue()


        """
        return self.spoolfilelistitem.getOutputQueue()



    # ***
    # Devuelve la biblioteca de la cola de salida en la que se encuentra el archivo en spool.
    def getSPLLSTITMOutputQueueLibrary(self):

        """
            Devuelve la biblioteca de la cola de salida en la que se encuentra el archivo en spool.

            java.lang.String = getOutputQueueLibrary()

        """
        return self.spoolfilelistitem.getOutputQueueLibrary()




    # ***
    # Devuelve el nombre de la cola de salida en la que se encuentra el archivo en spool.
    def getSPLLSTITMOutputQueueName(self):

        """
            Devuelve el nombre de la cola de salida en la que se encuentra el archivo en spool.

            java.lang.String = getOutputQueueName()


        """
        return self.spoolfilelistitem.getOutputQueueName()



    # ***
    # Devuelve cómo se asigna el archivo en spool.
    def getSPLLSTITMPrinterAssignment(self):

        """
            Devuelve cómo se asigna el archivo en spool.

             java.lang.String = getPrinterAssignment()

        """
        return self.spoolfilelistitem.getPrinterAssignment()





    # ***
    # Devuelve el nombre de la impresora en la que se ha asignado
    # la impresión del archivo en spool.
    def getSPLLSTITMPrinterName(self):

        """
            Devuelve el nombre de la impresora en la que se ha asignado
            la impresión del archivo en spool.

            java.lang.String =	getPrinterName()

        """
        return self.spoolfilelistitem.getPrinterName()





    # ***
    # Devuelve la prioridad del archivo en spool.
    def getSPLLSTITMPriority(self):

        """
            Devuelve la prioridad del archivo en spool.

            java.lang.String = getPriority()


        """
        return self.spoolfilelistitem.getPriority()




    # ***
    # Devuelve la programación del archivo en spool.
    def getSPLLSTITMSchedule(self):

        """
            Devuelve la programación del archivo en spool.

            java.lang.String = getSchedule()

        """
        return self.spoolfilelistitem.getSchedule()




    # ***
    # Devuelve el tamaño del archivo en spool en bytes.
    def getSPLLSTITMSize(self):

        """
            Devuelve el tamaño del archivo en spool en bytes.

            long =	getSize()

        """
        return self.spoolfilelistitem.getSize()




    # ***
    # Devuelve el estado del archivo en spool.
    def getSPLLSTITMStatus(self):

        """
            Devuelve el estado del archivo en spool.

             java.lang.String = getStatus()

        """
        return self.spoolfilelistitem.getStatus()




    # ***
    # Devuelve la hora en que se creó el archivo en spool.
    def getSPLLSTITMTimeOpened(self):

        """
            Devuelve la hora en que se creó el archivo en spool.

            java.lang.String =	getTimeOpened()

        """
        return self.spoolfilelistitem.getTimeOpened()





    # ***
    # Devuelve el número total de páginas o el número de registros de este archivo en spool.
    def getSPLLSTITMTotalPages(self):

        """
            Devuelve el número total de páginas o el número de registros de este archivo en spool.

            int =getTotalPages()

        """
        return self.spoolfilelistitem.getTotalPages()




    # ***
    # Devuelve los 10 caracteres de datos especificados
    # por el usuario que describen el archivo en spool.
    def getSPLLSTITMUserData(self):

        """
            Devuelve los 10 caracteres de datos especificados
            por el usuario que describen el archivo en spool.

            java.lang.String =	getUserData()

        """
        return self.spoolfilelistitem.getUserData()



    # ***
    # Devuelve el nombre del archivo en spool.
    def getSPLLSTITMName(self):

        """
            Devuelve el nombre del archivo en spool.

            java.lang.String =	getName()

        """
        return self.spoolfilelistitem.getName()



    # ***
    # Devuelve el número del archivo en spool.
    def getSPLLSTITMNumber(self):

        """
        Devuelve el número del archivo en spool.

        int = getNumber()

        """
        return self.spoolfilelistitem.getNumber()



    # ***
    # Devuelve el nombre del trabajo que creó el archivo en spool.
    def grtSPLLSTITMJobName(self):

        """
            Devuelve el nombre del trabajo que creó el archivo en spool.

            java.lang.String =	getJobName()

        """
        return self.spoolfilelistitem.getJobName()



    # ***
    # Devuelve el número del trabajo que creó el archivo en spool.
    def getSPLLSTITMJobNumber(self):

        """
            Devuelve el número del trabajo que creó el archivo en spool.

            java.lang.String =	getJobNumber()

        """
        return self.spoolfilelistitem.getJobNumber()




    # ***
    # Devuelve el nombre del sistema donde se ejecutó el trabajo que creó el archivo en spool.
    def getSPLLSTITMJobSystemName(self):

        """
            Devuelve el nombre del sistema donde se ejecutó el trabajo que creó el archivo en spool.

            java.lang.String =	getJobSystemName()

        """

        return self.spoolfilelistitem.getJobSystemName()




    # ***
    # Devuelve el usuario del trabajo que creó el archivo en spool.
    def getSPLLSTITMJobUser(self):

        """
            Devuelve el usuario del trabajo que creó el archivo en spool.

            java.lang.String = getJobUser()

        """
        return self.spoolfilelistitem.getJobUser()



    #             int	getASP()
    # Devuelve la agrupación de almacenamiento auxiliar (ASP) en la que reside el archivo en spool.
    def getSPLLSTITMASP(self):

        """
            Devuelve la agrupación de almacenamiento auxiliar (ASP) en la que reside el archivo en spool.

            int =getASP()

        """
        return self.spoolfilelistitem.getASP()
