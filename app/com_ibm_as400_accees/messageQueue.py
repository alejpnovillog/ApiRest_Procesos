# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Definimos la clase Mensajes de colas de mensajes
class MessageQueue():

    ALL =  "*ALL"
    ANY =  "*ANY"
    BYKEY = "*BYKEY"
    COMPLETION = "*COMP"
    COPY = "*COPY"
    CURRENT = "*CURRENT"
    DIAGNOSTIC = "*DIAG"
    FIRST = "*FIRST"
    INFORMATIONAL = "*INFO"
    INQUIRY = "*INQ"
    KEEP_UNANSWERED = "*KEEPUNANS"
    LAST = "*LAST"
    MESSAGES_NEED_REPLY = "*MNR"
    MESSAGES_NO_NEED_REPLY = "*MNNR"
    NEW = "*NEW"
    NEXT = "*NEXT"
    OLD = "*OLD"
    PREVIOUS = "*PRV"
    REMOVE = "*REMOVE"
    REPLY = "*RPY"
    SAME = "*SAME"
    SENDERS_COPY_NEED_REPLY = "*SCNR"


    def __init__(self, messagequeue):
        self.messagequeue = jpype.JClass('com.ibm.as400.access.MessageQueue')
        self.messagequeue = messagequeue


    # Agrega un PropertyChangeListener.
    def addMQPropertyChangeListener(self, oyente):

        """
            Agrega un PropertyChangeListener.
            Se llamará al método propertyChange() del
            PropertyChangeListener especificado cada vez que se
            cambie el valor de cualquier propiedad enlazada.

        """
        self.messagequeue.addPropertyChangeListener(oyente)


    # Agrega un VetoableChangeListener.
    def addMQVetoableChangeListener(self, oyente):

        """
            Agrega un VetoableChangeListener.
            Se llamará al método vetoableChange() de VetoableChangeListener
            especificado cada vez que se cambie el valor de cualquier propiedad restringida.


        """
        self.messagequeue.addVetoableChangeListener(oyente)


    # Cierra la lista de mensajes en el sistema.
    def closeMQ(self):

        """
            Cierra la lista de mensajes en el sistema.
            Esto libera cualquier recurso del sistema que esta lista de mensajes haya utilizado previamente.

        """
        self.messagequeue.close()


    # Cierra la lista en el sistema cuando este objeto se recolecta como basura.
    def finalizeMQ(self):

        """
            Cierra la lista en el sistema cuando este objeto se recolecta como basura.

        """
        self.messagequeue.finalize()

    # Devuelve el estado del formato del texto de ayuda
    def getMQHelpTextFormatting(self):

        """
            Devuelve el estado del formato del texto de ayuda. Los valores posibles son:
                MessageFile.NO_FORMATTING- El texto de ayuda se devuelve como una cadena de caracteres. Este es el valor predeterminado.
                MessageFile.RETURN_FORMATTING_CHARACTERS- El texto de ayuda contiene caracteres de formato. Los caracteres de formato son:
                    &N -- Forzar una nueva línea.
                    &P -- Forzar una nueva línea y sangrar la nueva línea con seis caracteres.
                    &B -- Forzar una nueva línea y aplicar una sangría de cuatro caracteres a la nueva línea.
                MessageFile.SUBSTITUTE_FORMATTING_CHARACTERS- La clase MessageFile reemplaza los caracteres de formato con caracteres de nueva línea y espacio.

           return integer
           El estado del formato del texto de ayuda.

        """
        return self.messagequeue.getHelpTextFormatting()


    # Devuelve el número de mensajes en la lista. Este método llama implícitamente a load().
    def getMQLength(self):

        """

            return  integer
            El número de mensajes, o 0 si no se recuperó ninguna lista.

        """
        return self.messagequeue.getLength()


    # Devuelve la dirección de la lista.
    def getMQListDirection(self):

        """
            return
            True si los mensajes se enumeran en orden del más antiguo al más reciente;
            False si los mensajes se enumeran en orden del más reciente al más antiguo.

        """
        return self.messagequeue.getListDirection()

    # Devuelve la lista de mensajes en la cola de mensajes.
    def getMQMessages(self):

        """
            La enumeración recupera los mensajes en bloques de 1000.
            Si esto no produce el rendimiento o el uso de memoria deseados,
            utilice el getMessages()que devuelve una matriz de objetos QueuedMessage
            y acepta una longitud y una compensación de lista .
            Si se produce un error mientras la Enumeración está cargando el siguiente bloque de mensajes,
            se lanzará una NoSuchElementException mientras que el error real se registrará en .Trace.ERROR

            return  un objeto Enumeration de QueuedMessageobjetos.

        """
        return self.messagequeue.getMessages()


    # Devuelve el nombre completo de la vía de acceso del sistema de archivos integrado
    def getMQPath(self):

        """
            Devuelve el nombre completo de la vía de acceso del sistema de archivos integrado
            de la cola de mensajes, o CURRENTpara hacer referencia a la cola de mensajes predeterminada del usuario.

            return  string
            El nombre completo de la vía de acceso del sistema de archivos integrado de la cola de mensajes,
            o CURRENTpara hacer referencia a la cola de mensajes predeterminada del usuario.

        """
        self.messagequeue.getPath()

    # Devuelve la gravedad de los mensajes que se devuelven.
    def getMQSeverity(self):

        """

            return integer
            La gravedad de los mensajes que se devuelven.

        """
        return self.messagequeue.getSeverity()

    # Devuelve si los mensajes se ordenarán o no cuando ALL
    # se especifica para los criterios de selección. El valor predeterminado es falso.
    def getMQSort(self):

        """
            Devuelve si los mensajes se ordenarán o no cuando ALL
            se especifica para los criterios de selección. El valor predeterminado es falso.

            return  boolean
            True si los mensajes se ordenarán por tipo de mensaje;
            False en caso contrario.

        """
        return self.messagequeue.getSort()

    # Devuelve el objeto del sistema que representa el sistema en el que existe la cola de mensajes.
    def getMQSystem(self):

        """

            return objeto AS400
            El objeto del sistema que representa el sistema en el que existe la cola de mensajes. Si el sistema no se ha configurado, se devuelve nulo.

        """
        return self.messagequeue.getSystem()

    # Devuelve la clave del mensaje de inicio del usuario, si se ha establecido una.
    def getMQUserStartingMessageKey(self):

        """

            return  bytearray
            La clave, o nula si no se ha establecido ninguna.

        """
        return self.messagequeue.getUserStartingMessageKey()

    # Devuelve la clave de mensaje de inicio de la estación de trabajo, si se ha establecido una.
    def getMQWorkstationStartingMessageKey(self):

        """

            return  byte lista
            La clave, o nula si no se ha establecido ninguna.

        """
        return self.messagequeue.getWorkstationStartingMessageKey()

    # Devuelve si los mensajes que necesitan una respuesta están incluidos o
    def isSelectMessagesNeedReplyMQ(self):

        """
            Devuelve si los mensajes que necesitan una respuesta están incluidos o
            no en la lista de mensajes devueltos.
            Si los tres captadores de selección de mensajes devuelven verdadero,
            es el equivalente a que todos los mensajes se incluyan en la lista de mensajes devueltos.
            De forma predeterminada, se devuelven todos los mensajes, por lo que este método devuelve verdadero.

            return boolean(True, False)
            True si los mensajes que necesitan una respuesta están incluidos en la lista de mensajes devueltos;
            False si los mensajes que necesitan una respuesta se excluyen de la lista de mensajes devueltos.

        """
        self.messagequeue.isSelectMessagesNeedReply()


    # Devuelve si los mensajes que no necesitan una respuesta se incluyen o no en la lista de mensajes devueltos.
    def isSelectMessagesNoNeedReplyMQ(self):

        """
            Devuelve si los mensajes que no necesitan una respuesta se incluyen
            o no en la lista de mensajes devueltos.
            Si los tres captadores de selección de mensajes devuelven verdadero,
            es el equivalente a que todos los mensajes se incluyan en la lista de mensajes devueltos.
            De forma predeterminada, se devuelven todos los mensajes, por lo que este método devuelve verdadero.

            return boolean(True, False)
            True si los mensajes que no necesitan respuesta están incluidos en la lista de mensajes devueltos;
            False si los mensajes que no necesitan respuesta se excluyen de la lista de mensajes devueltos.

        """
        return self.messagequeue.isSelectMessagesNoNeedReply()


    # Devuelve si los mensajes de copia del remitente que necesitan una respuesta están o no incluidos en la lista de mensajes devueltos.
    def isSelectSendersCopyMessagesNeedReplyMQ(self):

        """
            Devuelve si los mensajes de copia del remitente que necesitan una respuesta están o no incluidos en la lista de mensajes devueltos.
            Si los tres captadores de selección de mensajes devuelven verdadero,
            es el equivalente a que todos los mensajes se incluyan en la lista de mensajes devueltos.
            De forma predeterminada, se devuelven todos los mensajes, por lo que este método devuelve verdadero.


            return boolean(True, False)
            True si los mensajes de copia del remitente que necesitan una respuesta están incluidos en la lista de mensajes devueltos;
            False si los mensajes de copia del remitente que necesitan una respuesta se excluyen de la lista de mensajes devueltos.

        """
        return self.messagequeue.isSelectSendersCopyMessagesNeedReply()


    # Carga la lista de mensajes en el sistema.
    def loadMQ(self):

        """
            Este método informa al sistema para que cree una lista de mensajes dados los atributos
            agregados previamente para seleccionar, recuperar y clasificar.
            Este método bloquea hasta que el sistema devuelve el número total de mensajes que ha compilado.
            Una llamada posterior a getMessages()recuperará la información
            y los atributos reales del mensaje para cada mensaje en la lista del sistema.


        """

    # Recibe un mensaje de la cola de mensajes por clave.
    def receiveMQ(self, messagekey = None, waitTime= -1, messageAction= 'REMOVE' , messageType= 'ANY' ):

        """
            Recibe un mensaje de la cola de mensajes por clave.
            Este método recibe un mensaje de cualquier tipo excepto la copia del remitente.
            El mensaje se elimina de la cola de mensajes.
            Consulte la lista de valores de atributo QueuedMessage que se establecen en un mensaje recibido.

            parametro messagekey byte lista
                               waitTime integer
                                messageAction string
                                messageType string

                                waitTime - El número de segundos de espera para que el mensaje llegue a la cola para poder recibirlo.
                                        Si el mensaje no se recibe dentro del tiempo de espera especificado, se devuelve nulo. Los valores especiales son:
                                            0 - No espere el mensaje. Si el mensaje no está en la cola y especificó una clave de mensaje, se devuelve un valor nulo.
                                            -1 - Espere hasta que el mensaje llegue a la cola y se reciba, sin importar cuánto tarde. El sistema no tiene límite para el tiempo de espera.

                                messageAction - El tipo de mensaje a devolver. Los valores válidos son:
                                        OLD -   mantenga el mensaje en la cola de mensajes y márquelo como un mensaje antiguo.
                                                    Puede volver a recibir el mensaje usando la tecla de mensaje o
                                                    especificando el tipo de mensaje SIGUIENTE, ANTERIOR, PRIMERO o ÚLTIMO.
                                        REMOVE - elimina el mensaje de la cola de mensajes. La clave del mensaje ya no es válida, por lo que no puede volver a recibir el mensaje.
                                        SAME - mantiene el mensaje en la cola de mensajes sin cambiar su designación nueva o antigua.
                                                    SAME le permite recibir el mensaje nuevamente más tarde sin usar la tecla de mensaje.

                                messageType - El tipo de mensaje a devolver. Los valores válidos son:
                                        ANY - recibe un mensaje de cualquier tipo excepto la copia del remitente. La clave del mensaje es opcional.
                                        COMPLETION - recibe un mensaje de finalización. La clave del mensaje es opcional.
                                        COPY - recibe la copia del remitente de un mensaje de consulta enviado anteriormente. La clave del mensaje es obligatoria.
                                        DIAGNOSTIC - recibe un mensaje de diagnóstico. La clave del mensaje es opcional.
                                        FIRST - recibe el primer mensaje nuevo o antiguo en la cola. La clave de mensaje no está permitida.
                                        INFORMATIONAL - Recibe un mensaje informativo. La clave del mensaje es opcional.
                                        INQUIRY - Recibe un mensaje de consulta. Si la acción es ELIMINAR y
                                                          aún no se ha enviado una respuesta al mensaje de consulta, la respuesta predeterminada
                                                          se envía automáticamente cuando se recibe el mensaje de consulta. La clave del mensaje es opcional.
                                        LAST - recibe el último mensaje nuevo o antiguo en la cola. La clave de mensaje no está permitida.
                                        NEXT - recibe el siguiente mensaje nuevo o antiguo después del mensaje con la clave especificada.
                                                    Puede utilizar el valor especial TOP para la clave del mensaje.
                                                    TOP designa el mensaje en la parte superior de la cola de mensajes. La clave del mensaje es obligatoria.
                                        PREVIOUS - recibe el mensaje nuevo o antiguo antes del mensaje con la clave especificada. La clave del mensaje es obligatoria.
                                        REPLY - Recibe la respuesta a un mensaje de consulta. Para la clave del mensaje,
                                                    puede usar la clave de la copia del remitente de la consulta o el mensaje de notificación. La clave del mensaje es opcional.


            return objeto  QueuedMessage
            El mensaje en cola, o nulo si no se puede recibir el mensaje.

        """

        return self.messagequeue.receive(messagekey)


    # Elimina todos los mensajes de la cola de mensajes.
    def removeMQ(self, messagekey=None, messagetype=None):

        """

            Elimina todos los mensajes de la cola de mensajes.

            param
                    messagekey byte lista
                    messagetype string



        """
        if  messagekey == None and messagetype == None:
            self.messagequeue.remove()

        if   messagekey != None:
            self.messagequeue.remove(messagekey)

        if   messagetype != None:
            self.messagequeue.remove(messagetype)

        if  messagekey != None and messagetype != None:
            self.messagequeue.remove(messagekey, messagetype)

    # Elimina PropertyChangeListener. Si PropertyChangeListener no está en la lista, no se hace nada.
    def removeMQPropertyChangeListener(self, oyente):

        """
            Elimina PropertyChangeListener. Si PropertyChangeListener no está en la lista, no se hace nada.

            parametro oyente objeto listener

        """
        self.messagequeue.removePropertyChangeListener(oyente)


    # Elimina VetoableChangeListener. Si VetoableChangeListener no está en la lista, no se hace nada.
    def removeMQVetoableChangeListener(self, oyente):

        """
             Elimina VetoableChangeListener. Si VetoableChangeListener no está en la lista, no se hace nada.

             parametro oyente objeto listener

         """
        self.messagequeue.removeVetoableChangeListener(oyente)


    # Responde y elimina un mensaje si se le solicita.
    def replyMQ(self, messagekey=None, replaytext=None, remove=False):


        """
            Responde y elimina un mensaje si se le solicita.

            parametro
                messagekey byte lista
                replaytext string
                remove boolean(True, False)


                messagekey La clave del mensaje.
                replaytext  La respuesta. Para enviar la respuesta predeterminada almacenada en la descripción del mensaje, utilice espacios en blanco para este parámetro.
                remove      True para eliminar el mensaje de consulta y la respuesta de la cola de mensajes después de enviar la respuesta,
                                 False para mantener el mensaje de consulta y la respuesta después de enviar la respuesta.


        """

        if  messagekey != None and replaytext != None:
            self.messagequeue.reply(messagekey, replaytext, remove)


    # Envía un mensaje informativo a la cola de mensajes.
    def sendMQInformational(self, messageid, messagefile, sustitutionData):
        """
            Envía un mensaje informativo a la cola de mensajes.

            parametro
                messageid  El ID del mensaje.
                messagefile  El nombre de vía de acceso del sistema de archivos integrado del archivo de mensajes.
                sustitutionData Los datos de sustitución del mensaje, o nulo si ninguno.


        """
        self.messagequeue.sendInformational(messageid, messagefile, sustitutionData)

    # Envía un mensaje de consulta a la cola de mensajes.
    def sendMQInquiry(self, messageid, messagefile, replaymessagequeue):

        """
            Envía un mensaje de consulta a la cola de mensajes.

            parametros
            messageid  El ID del mensaje.
            messagefile  El nombre de vía de acceso del sistema de archivos integrado del archivo de mensajes.
            replaymessagequeue El nombre de ruta del sistema de archivos integrado de la cola de mensajes de respuesta.

            return byte linea
            La clave del mensaje.

        """
        return self.messagequeue.sendInquiry(messageid, messagefile, replaymessagequeue)


    # Establece si incluir o no los mensajes que necesitan una respuesta en la lista de mensajes devueltos.
    def setMQSelectMessagesNeedReply(self, setmessageneedreply):

        """

            Establece si incluir o no los mensajes que necesitan una respuesta en la lista de mensajes devueltos.
            Pasar verdadero a los tres configuradores de selección de mensajes es equivalente a recuperar todos los mensajes.
            De forma predeterminada, se recuperan todos los mensajes.

            parametro boolean(True, False)
            True para incluir mensajes que necesitan una respuesta;
            False para excluir los mensajes que necesitan una respuesta.

        """
        self.messagequeue.setSelectMessagesNeedReply(setmessageneedreply)


    # Establece si incluir o no los mensajes que no necesitan una respuesta en la lista de mensajes devueltos.
    # Pasar verdadero a los tres configuradores de selección de mensajes es equivalente a recuperar todos los mensajes.
    # De forma predeterminada, se recuperan todos los mensajes.
    def setMQSelectMessagesNoNeedReply(self, selectmessagenoneedreply):

        """
            Establece si incluir o no los mensajes que no necesitan una respuesta en la lista de mensajes devueltos.
            Pasar verdadero a los tres configuradores de selección de mensajes es equivalente a recuperar todos los mensajes.
             De forma predeterminada, se recuperan todos los mensajes.

             parametro boolean(True, False)
             True para incluir mensajes que no necesitan respuesta;
             False para excluir mensajes que no necesitan una respuesta.

        """

        self.messagequeue.setSelectMessagesNoNeedReply(selectmessagenoneedreply)



    # Establece si incluir o no los mensajes de copia del remitente
    def setMQSelectSendersCopyMessagesNeedReply(self, setselectsenderscopymessageneedreply):

        """
            Establece si incluir o no los mensajes de copia del remitente
            que necesitan una respuesta en la lista de mensajes devueltos.
            Pasar verdadero a los tres configuradores de selección de mensajes es equivalente a recuperar todos los mensajes.
            De forma predeterminada, se recuperan todos los mensajes.

            parametro boolean(True, False)
            True para incluir los mensajes de copia del remitente que necesitan una respuesta;
            False para excluir los mensajes de copia del remitente que necesitan una respuesta.


        """
        self.messagequeue.setSelectSendersCopyMessagesNeedReply(setselectsenderscopymessageneedreply)



    # Establece la gravedad de los mensajes que se devuelven.
    def setMQSeverity(self, severity):

        """
            Establece la gravedad de los mensajes que se devuelven.
            Se devuelven todos los mensajes de la gravedad especificada y superior.
            El valor predeterminado es 0.
            Esto surte efecto la próxima vez que se recupere o actualice la lista de mensajes en cola.

            parametro integer
            La gravedad de los mensajes a devolver. El valor debe estar entre 0 y 99, ambos inclusive.


        """
        self.messagequeue.setSeverity(severity)

    # Establece si la lista debe ordenarse por tipo de mensaje cuando ALL
    def setMQSort(self, sort):

        """
            Establece si la lista debe ordenarse por tipo de mensaje cuando ALL
            se seleccionan mensajes para su recuperación.
            Si los criterios de selección se establecen en algo distinto de ALL, se ignora la configuración de clasificación.

            parametro boolean(True, False)
            True to indicate the messages should be sorted;
            False to indicate no sorting should be performed on the message list.

        """

        self.messagequeue,setSort(sort)


    # Establece el sistema. Esto no se puede cambiar si el objeto ha establecido una conexión con el sistema.
    def setMQSystem(self, system):

        """
            Establece el sistema. Esto no se puede cambiar si el objeto ha establecido una conexión con el sistema.

            parametro objeto AS400
            El objeto del sistema que representa el sistema en el que existe la cola de mensajes.

        """

        self.messagequeue.setSystem(system)

    # Establece la clave de mensaje inicial utilizada para comenzar a buscar mensajes
    def setMQUserStartingMessageKey(self, userstartingmessagekey):

        """
            Establece la clave de mensaje inicial utilizada para comenzar a buscar mensajes
            para enumerar desde la entrada correspondiente en la cola de mensajes.
            Cualquier tecla de mensaje válida funcionará, incluidos NEWESTy OLDEST.
            Si se especifica la clave de un mensaje de respuesta, la búsqueda de mensajes
            comienza con la consulta o el mensaje de copia del remitente asociado
            con esa respuesta, no con el mensaje de respuesta en sí.
            Si la cola de mensajes se establece en CURRENT,
            la clave representa la clave de mensaje inicial para la cola de mensajes de usuario del usuario actual.


            parametro byte lista
            La clave. Especifique nulo para restablecerlo al valor predeterminado, que será OLDEST o NEWEST según la dirección de la lista.


        """
        self.messagequeue.setUserStartingMessageKey(userstartingmessagekey)



    # Establece la clave de mensaje inicial utilizada para comenzar a
    def setMQWorkstationStartingMessageKey(self, workstationstartingmessagekey):

        """
            Establece la clave de mensaje inicial utilizada para comenzar a
            buscar mensajes para enumerar desde la entrada correspondiente en la cola de mensajes.
            Cualquier tecla de mensaje válida funcionará, incluidos NEWESTy OLDEST.
            Si se especifica la clave de un mensaje de respuesta, la búsqueda de mensajes comienza
            con la consulta o el mensaje de copia del remitente asociado con esa respuesta, no con el mensaje de respuesta en sí.
            Si la cola de mensajes se establece en CURRENT,
            la clave representa la clave de mensaje inicial para la cola de mensajes de la estación de trabajo del usuario actual.

            parametro byte lista
            La clave. Especifique nulo para restablecerlo al valor predeterminado.


        """
        self.messagequeue.setWorkstationStartingMessageKey(workstationstartingmessagekey)

