"""
        void	addPropertyChangeListener(java.beans.PropertyChangeListener listener)
            Agrega un PropertyChangeListener.

        void	addVetoableChangeListener(java.beans.VetoableChangeListener listener)
            Agrega un VetoableChangeListener.

        void	commitChanges()
            Confirma todos los cambios de atributos no confirmados.

        void	commitChanges(boolean callOnThread)
            Confirma todos los cambios de atributos no confirmados.

void	end(int delay)
Termina este trabajo.

int	getAuxiliaryIORequests()
Devuelve el número de solicitudes de E/S auxiliares realizadas por el trabajo en todos los pasos de enrutamiento.

java.lang.String	getBreakMessageHandling()
Devuelve un valor que representa cómo este trabajo maneja los mensajes de interrupción.

boolean	getCacheChanges()
Indica si los cambios del valor del atributo se almacenan en caché.

CallStackEntry[]	getCallStack(long threadID)
Devuelve la pila de llamadas para el subproceso especificado en este trabajo.

int	getCodedCharacterSetID()
Devuelve el identificador de juego de caracteres codificado (CCSID) utilizado para este trabajo.

java.lang.String	getCompletionStatus()
Devuelve el estado de finalización del trabajo.

java.lang.String	getCountryID()
Devuelve el identificador de país o región asociado con este trabajo.

int	getCPUUsed()
Devuelve la cantidad de tiempo de unidad de procesamiento (en milisegundos) que utilizó el trabajo.

java.lang.String	getCurrentLibrary()
Devuelve el nombre de la biblioteca actual para el subproceso inicial del trabajo.

boolean	getCurrentLibraryExistence()
Indica si existe una biblioteca actual.

java.util.Date	getDate()
Devuelve la fecha y la hora en que se colocó el trabajo en el sistema.

java.lang.String	getDateFormat()
Devuelve el formato en el que se presentan las fechas.

java.lang.String	getDateSeparator()
Devuelve el valor utilizado para separar días, meses y años al presentar una fecha.

java.lang.String	getDDMConversationHandling()
Devuelve si las conexiones que usan protocolos de administración de datos distribuidos (DDM) permanecen activas cuando no se usan.

java.lang.String	getDecimalFormat()
Devuelve el formato decimal utilizado para este trabajo.

int	getDefaultCodedCharacterSetIdentifier()
Devuelve el identificador de juego de caracteres codificado predeterminado (CCSID) utilizado para este trabajo.

int	getDefaultWait()
Devuelve el tiempo máximo predeterminado (en segundos) que un subproceso en el trabajo espera una instrucción del sistema, como una instrucción de interfaz de máquina (MI) LOCK, para adquirir un recurso.

java.lang.String	getDeviceRecoveryAction()
Devuelve la acción realizada para los trabajos interactivos cuando se produce un error de E/S para el dispositivo de programa que solicita el trabajo.

            int	getEndSeverity()
                Devuelve el nivel de gravedad del mensaje de los mensajes de escape que pueden hacer que finalice un trabajo por lotes.

java.lang.String	getFunctionName()
Devuelve información adicional (como se describe en el atributo FUNCTION_TYPE) sobre la última función de alto nivel iniciada por el subproceso inicial.

java.lang.String	getFunctionType()
Devuelve la última función de alto nivel iniciada por el subproceso inicial.

java.lang.String	getInquiryMessageReply()
Devuelve cómo responde el trabajo a los mensajes de consulta.

int	getInteractiveTransactions()
Devuelve el recuento de interacciones del operador, como presionar la tecla Intro o una tecla de función.

java.lang.String	getInternalJobID()
Obsoleto.
Utilice getInternalJobIdentifier()en su lugar. El identificador de trabajo interno debe tratarse como una matriz de bytes de 16 bytes.

byte[]	getInternalJobIdentifier()
Devuelve el identificador de trabajo interno.

java.lang.String	getJobAccountingCode()
Devuelve un identificador asignado al trabajo por el sistema para recopilar información sobre el uso de recursos para el trabajo cuando la contabilidad de trabajos está activa.

java.util.Date	getJobActiveDate()
Devuelve la fecha y la hora en que el trabajo comenzó a ejecutarse en el sistema.

java.lang.String	getJobAsp()
Obtener la información del grupo ASP del trabajo.

java.util.Date	getJobDate()
Devuelve la fecha que se utilizará para el trabajo.

java.lang.String	getJobDescription()
Devuelve el nombre de vía de acceso del sistema de archivos integrado completo para la descripción del trabajo.

java.util.Date	getJobEndedDate()
Devuelve la fecha y la hora en que finalizó la ejecución del trabajo en el sistema.

java.util.Date	getJobEnterSystemDate()
Devuelve la fecha y la hora en que se colocó el trabajo en el sistema.

JobLog	getJobLog()
Devuelve el registro de trabajo.

java.lang.String	getJobMessageQueueFullAction()
Devuelve la acción a realizar cuando la cola de mensajes está llena.

int	getJobMessageQueueMaximumSize()
Devuelve el tamaño máximo (en megabytes) que puede tener la cola de mensajes del trabajo.

java.util.Date	getJobPutOnJobQueueDate()
Devuelve la fecha y la hora en que este trabajo se colocó en esta cola de trabajos.

java.lang.String	getJobStatusInJobQueue()
Devuelve el estado de este trabajo en la cola de trabajos.

java.lang.String	getJobSwitches()
Devuelve la configuración actual de los conmutadores de trabajo utilizados por este trabajo.

java.lang.String	getLanguageID()
Devuelve el identificador de idioma asociado con este trabajo.

java.lang.String	getLoggingCLPrograms()
Devuelve un valor que indica si los comandos se registran o no para los programas CL que se ejecutan.

int	getLoggingLevel()
Devuelve qué tipo de información se registra.
int	getLoggingSeverity()
Devuelve el nivel de gravedad que se usa junto con el nivel de registro para determinar qué mensajes de error se registran en el registro del trabajo.
java.lang.String	getLoggingText()
Devuelve el nivel de texto del mensaje que se escribe en el registro de trabajo cuando se registra un mensaje de acuerdo con LOGGING_LEVEL y LOGGING_SEVERITY.
java.lang.String	getModeName()
Devuelve el nombre de modo del dispositivo de comunicaciones avanzadas programa a programa (APPC) que inició el trabajo.
java.lang.String	getName()
Devuelve el nombre del trabajo.
java.lang.String	getNumber()
Devuelve el número de trabajo.
int	getNumberOfLibrariesInSYSLIBL()
Devuelve el número de bibliotecas en la parte del sistema de la lista de bibliotecas del subproceso inicial del trabajo.
int	getNumberOfLibrariesInUSRLIBL()
Devuelve el número de bibliotecas en la parte del usuario de la lista de bibliotecas para el subproceso inicial del trabajo.
int	getNumberOfProductLibraries()
Devuelve el número de bibliotecas que contienen información del producto para el subproceso inicial del trabajo.
java.lang.String	getOutputQueue()
Devuelve el nombre completo de la vía de acceso del sistema de archivos integrado de la cola de salida predeterminada que se utiliza para la salida en cola producida por este trabajo.
int	getOutputQueuePriority()
Devuelve la prioridad de salida para los archivos de salida en cola que produce este trabajo.
int	getPoolIdentifier()
Devuelve el identificador del grupo relacionado con el sistema desde el que se asigna el almacenamiento principal del trabajo.
java.lang.String	getPrinterDeviceName()
Devuelve el dispositivo de impresora utilizado para imprimir la salida de este trabajo.
java.lang.String	getPrintKeyFormat()
Devuelve un valor que indica si se proporciona información de borde y encabezado cuando se presiona la tecla Imprimir.
java.lang.String	getPrintText()
Devuelve la línea de texto (si existe) que se imprime en la parte inferior de cada página de salida impresa para el trabajo.
java.lang.String[]	getProductLibraries()
Devuelve las bibliotecas que contienen información del producto para el subproceso inicial del trabajo.
boolean	getPurge()
Indica si el trabajo es elegible o no para ser movido del almacenamiento principal y colocado en el almacenamiento auxiliar al final de un intervalo de tiempo o al entrar en una espera larga (como esperar la respuesta de un usuario de la estación de trabajo).
java.lang.String	getQueue()
Devuelve el nombre completo de la vía de acceso del sistema de archivos integrado de la cola de trabajos en la que se encuentra actualmente el trabajo, o en la que estaba el trabajo si está actualmente activo.
int	getQueuePriority()
Devuelve la prioridad de programación del trabajo en comparación con otros trabajos en la misma cola de trabajos.
java.lang.String	getRoutingData()
Devuelve los datos de enrutamiento que se utilizan para determinar la entrada de enrutamiento que identifica el programa que se iniciará para el paso de enrutamiento.
int	getRunPriority()
Devuelve la prioridad con la que se ejecuta actualmente el trabajo, en relación con otros trabajos del sistema.
java.util.Date	getScheduleDate()
Devuelve la fecha y la hora en que el trabajo está programado para activarse.
boolean	getSignedOnJob()
Indica si el trabajo debe tratarse como un usuario registrado en el sistema.
java.lang.String	getSortSequenceTable()
Devuelve el nombre de la tabla de secuencia de clasificación asociada con este trabajo.
java.lang.String	getStatus()
Devuelve el estado de este trabajo.
java.lang.String	getStatusMessageHandling()
Devuelve si se muestran mensajes de estado para este trabajo.
java.lang.String	getStringValue(int attribute)
Devuelve el valor del atributo de trabajo especificado, como una cadena.
java.lang.String	getSubsystem()
Devuelve el nombre de ruta completo del sistema de archivos integrado de la descripción del subsistema para el subsistema en el que se ejecuta el trabajo.
java.lang.String	getSubtype()
Devuelve información adicional sobre el tipo de trabajo (si existe).
AS400	getSystem()
Devuelve el sistema.
java.lang.String[]	getSystemLibraryList()
Devuelve la parte del sistema de la lista de bibliotecas del subproceso inicial del trabajo.
java.lang.String	getTimeSeparator()
Devuelve el valor utilizado para separar horas, minutos y segundos al presentar una hora.
int	getTimeSlice()
Devuelve la cantidad máxima de tiempo de procesador (en milisegundos) otorgada a cada subproceso en este trabajo antes de que otros subprocesos en este trabajo y en otros trabajos tengan la oportunidad de ejecutarse.
java.lang.String	getTimeSliceEndPool()
Devuelve un valor que indica si un subproceso en un trabajo interactivo se mueve a otro grupo de almacenamiento principal al final de su intervalo de tiempo.
int	getTotalResponseTime()
Devuelve la cantidad total de tiempo de respuesta para el subproceso inicial, en milisegundos.
java.lang.String	getType()
Devuelve el tipo de trabajo.
java.lang.String	getUser()
Devuelve el nombre de usuario.
java.lang.String[]	getUserLibraryList()
Devuelve la parte del usuario de la lista de bibliotecas para el subproceso inicial del trabajo.
java.lang.Object	getValue(int attribute)
Devuelve el valor del atributo de trabajo especificado.
java.lang.String	getWorkIDUnit()
Devuelve el identificador de la unidad de trabajo.
void	hold(boolean holdSpooledFiles)
Tiene este trabajo.
void	loadInformation()
Actualiza los valores de todos los atributos.
void	loadInformation(int[] attributes)
Actualiza los valores de atributos específicos.
void	loadStatistics()
Actualiza solo los valores de las estadísticas transcurridas.
void	release()
Libera este trabajo.
void	removePropertyChangeListener(java.beans.PropertyChangeListener listener)
Elimina un PropertyChangeListener.
void	removeVetoableChangeListener(java.beans.VetoableChangeListener listener)
Elimina un VetoableChangeListener.
void	resetStatistics()
Restablece la hora de inicio de la medición utilizada para calcular las estadísticas de tiempo transcurrido.
void	setBreakMessageHandling(java.lang.String breakMessageHandling)
Establece cómo este trabajo maneja los mensajes de interrupción.
void	setCacheChanges(boolean cacheChanges)
Establece el valor que indica si los cambios en el valor del atributo se confirman inmediatamente.
void	setCodedCharacterSetID(int codedCharacterSetID)
Establece el identificador de juego de caracteres codificados (CCSID) utilizado para este trabajo.
void	setCountryID(java.lang.String countryID)
Establece el identificador de país o región asociado con este trabajo.
void	setDateFormat(java.lang.String dateFormat)
Establece el formato en el que se presentan las fechas.
void	setDateSeparator(java.lang.String dateSeparator)
Establece el valor utilizado para separar días, meses y años al presentar una fecha.
void	setDDMConversationHandling(java.lang.String ddmConversationHandling)
Establece si las conexiones que utilizan protocolos de gestión de datos distribuidos (DDM) permanecen activas cuando no se utilizan.
void	setDecimalFormat(java.lang.String decimalFormat)
Establece el formato decimal utilizado para este trabajo.
void	setDefaultWait(int defaultWait)
Establece el tiempo máximo predeterminado (en segundos) que un subproceso en el trabajo espera una instrucción del sistema, como una instrucción de interfaz de máquina (MI) LOCK, para adquirir un recurso.
void	setDeviceRecoveryAction(java.lang.String deviceRecoveryAction)
Establece la acción que se realiza para los trabajos interactivos cuando se produce un error de E/S para el dispositivo de programa que solicita el trabajo.
void	setInquiryMessageReply(java.lang.String inquiryMessageReply)
Establece cómo responde el trabajo a los mensajes de consulta.
void	setInternalJobID(java.lang.String internalJobID)
Obsoleto.
Utilice setInternalJobIdentifier(byte[])en su lugar. El identificador de trabajo interno debe tratarse como una matriz de bytes de 16 bytes.
void	setInternalJobIdentifier(byte[] internalJobID)
Establece el identificador de trabajo interno.
void	setJobAccountingCode(java.lang.String jobAccountingCode)
Establece un identificador asignado al trabajo por el sistema para recopilar información de uso de recursos para el trabajo cuando la contabilidad de trabajos está activa.
void	setJobDate(java.util.Date jobDate)
Establece la fecha que se asigna al trabajo.
void	setJobMessageQueueFullAction(java.lang.String jobMessageQueueFullAction)
Establece la acción a realizar cuando la cola de mensajes está llena.
void	setJobSwitches(java.lang.String jobSwitches)
Establece la configuración actual de los interruptores de trabajo que utiliza este trabajo.
void	setLanguageID(java.lang.String languageID)
Establece el identificador de idioma asociado con este trabajo.
void	setLoggingCLPrograms(java.lang.String loggingCLPrograms)
Establece si los comandos se registran o no para los programas CL que se ejecutan.
void	setLoggingLevel(int loggingLevel)
Establece qué tipo de información se registra.
void	setLoggingSeverity(int loggingSeverity)
Establece el nivel de gravedad que se usa junto con el nivel de registro para determinar qué mensajes de error se registran en el registro del trabajo.
void	setLoggingText(java.lang.String loggingText)
Establece el nivel de texto del mensaje que se escribe en el registro de trabajo cuando se registra un mensaje de acuerdo con LOGGING_LEVEL y LOGGING_SEVERITY.
void	setName(java.lang.String name)
Establece el nombre del trabajo.
void	setNumber(java.lang.String number)
Establece el número de trabajo.
void	setOutputQueue(java.lang.String outputQueue)
Establece el nombre de vía de acceso del sistema de archivos integrado completo de la cola de salida predeterminada que se utiliza para la salida en cola producida por este trabajo.
void	setOutputQueuePriority(int outputQueuePriority)
Establece la prioridad de salida para los archivos de salida en cola que produce este trabajo.
void	setPrinterDeviceName(java.lang.String printerDeviceName)
Establece el dispositivo de impresora utilizado para imprimir la salida de este trabajo.
void	setPrintKeyFormat(java.lang.String printKeyFormat)
Establece si se proporciona información de borde y encabezado cuando se presiona la tecla Imprimir.
void	setPrintText(java.lang.String printText)
Establece la línea de texto (si existe) que se imprime en la parte inferior de cada página de salida impresa para el trabajo.
void	setPurge(boolean purge)
Establece el valor que indica si el trabajo es elegible o no para ser movido del almacenamiento principal y colocado en el almacenamiento auxiliar al final de un intervalo de tiempo o al ingresar a una espera prolongada (como esperar la respuesta de un usuario de la estación de trabajo).
void	setQueue(java.lang.String jobQueue)
Establece el nombre de vía de acceso del sistema de archivos integrado completo de la cola de trabajos en la que debe estar el trabajo.
void	setQueuePriority(int queuePriority)
Establece la prioridad de programación del trabajo en comparación con otros trabajos en la misma cola de trabajos.
void	setRunPriority(int runPriority)
Establece la prioridad con la que el trabajo compite por la unidad de procesamiento en relación con los otros trabajos que están activos al mismo tiempo.
void	setScheduleDate(java.util.Date scheduleDate)
Establece la fecha y la hora en que el trabajo está programado para activarse.
void	setScheduleDate(java.lang.String scheduleDate)
Establece la fecha en que el trabajo está programado para activarse.
void	setScheduleTime(java.util.Date scheduleTime)
Establece la fecha y la hora en que el trabajo está programado para activarse.
void	setScheduleTime(java.lang.String scheduleTime)
Establece la hora a la que está programado que el trabajo se active.
void	setSortSequenceTable(java.lang.String sortSequenceTable)
Establece el nombre de la tabla de secuencia de clasificación asociada con este trabajo.
void	setStatusMessageHandling(java.lang.String statusMessageHandling)
Establece el valor que indica si se muestran mensajes de estado para este trabajo.
void	setSystem(AS400 system)
Establece el sistema.
void	setTimeSeparator(java.lang.String timeSeparator)
Establece el valor utilizado para separar horas, minutos y segundos al presentar una hora.
void	setTimeSlice(int timeSlice)
Establece la cantidad máxima de tiempo de procesador (en milisegundos) otorgado a cada subproceso en este trabajo antes de que otros subprocesos en este trabajo y en otros trabajos tengan la oportunidad de ejecutarse.
void	setTimeSliceEndPool(java.lang.String timeSliceEndPool)
Establece el valor que indica si un subproceso en un trabajo interactivo se mueve a otro grupo de almacenamiento principal al final de su intervalo de tiempo.
void	setUser(java.lang.String user)
Establece el nombre de usuario.
void	setValue(int attribute, java.lang.Object value)
Establece un valor para un atributo de trabajo.
java.lang.String	toString()
Devuelve la representación de cadena de este trabajo en el formato "número/usuario/nombre" o "" si alguno de estos atributos es nulo.

void	addJobAttributeToRetrieve(int attribute)
Agrega un atributo de trabajo que se recuperará para cada trabajo en esta lista de trabajos.
void	addJobAttributeToSortOn(int attribute, boolean sortOrder)
Agrega un atributo de trabajo utilizado para ordenar la lista.
void	addJobSelectionCriteria(int selectionType, java.lang.Object selectionValue)
Agrega un tipo de selección y un valor que se utilizará para filtrar la lista de trabajos.

        void	addPropertyChangeListener(java.beans.PropertyChangeListener listener)
Agrega un PropertyChangeListener.

        void	addVetoableChangeListener(java.beans.VetoableChangeListener listener)
            Agrega un VetoableChangeListener.
void	clearJobAttributesToRetrieve()
Borra los atributos del trabajo que se van a recuperar.
void	clearJobAttributesToSortOn()
Borra los atributos de trabajo utilizados para ordenar la lista.
void	clearJobSelectionCriteria()
Borra los tipos y valores de selección utilizados para filtrar la lista de trabajos.
            void	close()
                Cierra la lista de trabajos en el sistema.
protected void	finalize()
Cierra la lista en el sistema cuando este objeto se recolecta como basura.
java.util.Enumeration	getJobs()
Devuelve una enumeración que envuelve la lista de trabajos en el sistema.
Job[]	getJobs(int listOffset, int number)
Devuelve un subconjunto de la lista de trabajos en la lista de trabajos.
int	getLength()
Devuelve el número de trabajos en la lista.
java.lang.String	getName()
Devuelve el nombre del trabajo que describe qué trabajos se devuelven.
java.lang.String	getNumber()
Devuelve el número de trabajo que describe qué trabajos se devuelven.
AS400	getSystem()
Devuelve el objeto del sistema que representa el sistema en el que existen los trabajos.
java.lang.String	getUser()
Devuelve el nombre de usuario que describe qué trabajos se devuelven.
void	load()
Carga la lista de trabajos en el sistema.
void	removePropertyChangeListener(java.beans.PropertyChangeListener listener)
Elimina PropertyChangeListener.
void	removeVetoableChangeListener(java.beans.VetoableChangeListener listener)
Elimina VetoableChangeListener.
void	setName(java.lang.String name)
Establece el nombre del trabajo que describe qué trabajos se devuelven.
void	setNumber(java.lang.String number)
Establece el número de trabajo que describe qué trabajos se devuelven.
void	setSystem(AS400 system)
Establece el objeto del sistema que representa el sistema en el que existen los trabajos.
void	setUser(java.lang.String user)
Establece el valor del nombre de usuario que describe qué trabajos se devuelven.

void	addAttributeToRetrieve(int attribute)
Adds a message attribute that will be retrieved for each joblog.

        void	addPropertyChangeListener(java.beans.PropertyChangeListener listener)
        Adds a PropertyChangeListener.

        void	addVetoableChangeListener(java.beans.VetoableChangeListener listener)
            Adds a VetoableChangeListener.

void	clearAttributesToRetrieve()
Clears the message attributes to be retrieved for a given Joblog.
            void	close()
                    Closes the message list on the system.
protected void	finalize()
Closes the list on the system when this object is garbage collected.
int	getLength()
Returns the number of messages in the job log.
boolean	getListDirection()
Returns the list direction.
java.util.Enumeration	getMessages()
Returns the list of messages in the job log.
QueuedMessage[]	getMessages(int listOffset, int number)
Returns a subset of the list of messages in the job log.
java.lang.String	getName()
Returns the job name.
java.lang.String	getNumber()
Returns the job number.
byte[]	getStartingMessageKey()
Returns the starting message key.
AS400	getSystem()
Returns the system object representing the system on which the job log exists.
java.lang.String	getUser()
Returns the job user name.
void	load()
Loads the list of messages on the system.
void	removePropertyChangeListener(java.beans.PropertyChangeListener listener)
Removes the PropertyChangeListener.
void	removeVetoableChangeListener(java.beans.VetoableChangeListener listener)
Removes the VetoableChangeListener.
void	setListDirection(boolean listDirection)
Sets the list direction.
void	setName(java.lang.String name)
Sets the job name.
void	setNumber(java.lang.String number)
Sets the job number.
void	setStartingMessageKey(byte[] startingMessageKey)
Sets the message key used to begin searching for messages to list from the corresponding entry in the job log.
void	setSystem(AS400 system)
Sets the system.
void	setUser(java.lang.String user)
Sets the job user name.
static void	writeMessage(AS400 system, java.lang.String messageID, int messageType)
Writes a program message to the job log for the job in which the program is running.
static void	writeMessage(AS400 system, java.lang.String messageID, int messageType, byte[] substitutionData)
Writes a program message to the job log for the job in which the program is running.
static void	writeMessage(AS400 system, java.lang.String messageID, int messageType, java.lang.String messageFile)
Writes a program message to the job log for the job in which the program is running.
static void	writeMessage(AS400 system, java.lang.String messageID, int messageType, java.lang.String messageFile, byte[] substitutionData)
Writes a program message to the job log for the job in which the program is running.
static void	writeMessage(AS400 system, java.lang.String messageID, int messageType, java.lang.String messageFile, byte[] substitutionData, boolean onThread)
Writes a program message to the job log for the job in which the program is running.

boolean	exists()
Determines if the subsystem currently exists on the system.
java.lang.String	getAuthorityCheck()
Whether the user must be the owner of the queue in order to control the queue by holding or releasing the queue
int	getCurrentActive()
Return The current number of jobs that are active that came through this job queue entry
java.lang.String	getJobQLibrary()
Return the library containing the job queue.
java.lang.String	getJobQName()
Return the job queue name
java.lang.String	getJobQueueStatus()
Return The status of the job queue
int	getMaxActive()
Return The maximum number of jobs that can be active at the same time through this job queue entry.
int	getNumberOfJobs()
Return The number of jobs in the queue
ObjectDescription	getObjectDescription()
Returns an ObjectDescription instance representing the subsystem.
java.lang.String	getOperatorControlled()
Return Whether a user who has job control authority is allowed to control this job queue and manage the jobs on the queue.
int	getSequenceNumber()
Return The job queue entry sequence number
java.lang.String	getSubsystemLibrary()
Return The library in which the subsystem description resides
java.lang.String	getSubsystemName()
Return The name of the subsystem that can receive jobs from this job queue
java.lang.String	getTextDescription()
Return Text that briefly describes the job queue
void	refresh()
Refreshes the values for all attributes of the job queue.
void	setFormat(java.lang.String format)
Set retrieve Job Queue format
void	setLibraryName(java.lang.String library)
Sets the job queue library.
void	setName(java.lang.String name)
Sets the job queue name.
void	setSystem(AS400 system)
Sets the system.

boolean	exists()
Determines if the Job Description currently exists on the system.
java.lang.String	getAccountingCode()
Returns the accounting code associated with this job description.
java.lang.String	getCYMDJobDate()
Returns the job date in CYMD format.
java.lang.String	getDDMConversation()
Returns whether Distributed Data Management conversations are kept or dropped when they are not being used.
java.lang.String	getDeviceRecoveryAction()
Returns the action to take when an I/O error occurs for the interactive job's requesting program device.
            int	getEndSeverity()
                Returns the message severity level of escape messages that can cause a batch job to end.
java.lang.String[]	getInitialASPGroupNames()
Returns the list of initial ASP groups for jobs that use this job description.
java.lang.String[]	getInitialLibraryList()
Returns the initial library list that is used for jobs that use this job description.
java.lang.String	getInquiryMessageReply()
Indicates how inquiry messages are answered for jobs that use this job description.
java.lang.String	getJobDateString()
Returns the date that will be assigned to jobs using this job description when they are started.
java.lang.String	getJobLogOutput()
Indicates how the job log will be produced when the job completes.
java.lang.String	getJobMessageQueueFullAction()
Returns the action to be taken when the job message queue becomes full.
int	getJobMessageQueueMaximumSize()
Returns the maximum size (in megabytes) of the job message queue.
java.lang.String	getJobQueueLibraryName()
Returns the library of the job queue into which batch jobs using this job description are placed.
java.lang.String	getJobQueueName()
Returns the name of the job queue into which batch jobs using this job description are placed.
int	getJobQueuePriority()
Returns the scheduling priority of each job that uses this job description.
byte	getJobSwitches()
Returns the initial settings for a group of eight job switches used by jobs that use this job description.
java.lang.String	getLibraryName()
Returns name of the library in which the job description resides.
int	getMessageLoggingLevel()
Returns the type of information logged.
int	getMessageLoggingSeverity()
Returns the severity level that is used in conjunction with the logging level to determine which error messages are logged in the job log.
java.lang.String	getMessageLoggingText()
Returns the level of message text that is written in the job log when a message is logged according to the logging level and logging severity.
java.lang.String	getName()
Returns name of the job description about which information is being returned.
ObjectDescription	getObjectDescription()
Returns an ObjectDescription instance representing the job description.
java.lang.String	getOutputQueueLibraryName()
Returns the name of the library in which the output queue resides.
java.lang.String	getOutputQueueName()
Returns the name of the default output queue that is used for spooled output produced by jobs that use this job description.
int	getOutputQueuePriority()
Returns the output priority for spooled files that are produced by jobs using this job description.
java.lang.String	getPrinterDeviceName()
Returns the name of the printer device or the source for the name of the printer device that is used for all spooled files created by jobs that use this job description.
java.lang.String	getPrintText()
Returns the line of text (if any) that is printed at the bottom of each page of printed output for jobs using this job description.
java.lang.String	getRoutingData()
Returns the routing data that is used with this job description to start jobs.
java.lang.String	getSpooledFileAction()
Returns the value that specifies whether spooled files can be accessed through job interfaces once a job has completed its normal activity.
int	getSyntaxCheckSeverity()
Returns whether requests placed on the job's message queue are checked for syntax as CL commands, and the message severity that causes a syntax error to end processing of a job.
AS400	getSystem()
Returns the system where the job description is located.
java.lang.String	getTextDescription()
Returns the user text, if any, used to briefly describe the job description.
java.lang.String	getTimeSliceEndPool()
Returns whether interactive jobs using this job description should be moved to another main storage pool when they reach time-slice end.
java.lang.String	getUserName()
Returns the name of the user profile associated with this job description.
boolean	isAllowMultipleThreads()
Returns whether or not the job is allowed to run with multiple user threads.
boolean	isHoldOnJobQueue()
Returns whether jobs using this job description are put on the job queue in the hold condition.
boolean	isLoggingOfCLPrograms()
Returns whether or not commands are logged for CL programs that are run.
void	refresh()
Refreshes the values for all attributes of the job description.
void	setLibraryName(java.lang.String library)
Sets the library where the job description is located.
void	setName(java.lang.String name)
Sets the job description name.
void	setSystem(AS400 system)
Sets the system.



"""