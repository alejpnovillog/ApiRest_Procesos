# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Definimos la clase Cola de Mensaje
class QueuedMessage():

    COMPLETION = 1
    DIAGNOSTIC = 2
    ESCAPE = 15
    ESCAPE_NOT_HANDLED = 17
    INFORMATIONAL = 4
    INQUIRY = 5
    MESSAGE_OPTION_ALL = 2
    MESSAGE_OPTION_NONE = 1
    MESSAGE_OPTION_UP_TO_10 = 0
    NOTIFY = 14
    NOTIFY_NOT_HANDLED = 16
    REPLY_FROM_SYSTEM_REPLY_LIST = 25
    REPLY_MESSAGE_DEFAULT_USED = 23
    REPLY_NOT_VALIDITY_CHECKED = 21
    REPLY_SYSTEM_DEFAULT_USED = 24
    REPLY_VALIDITY_CHECKED = 22
    REQUEST = 8
    REQUEST_WITH_PROMPTING = 10
    SENDERS_COPY = 6

    ALERT_OPTION_SIN_INFORMACION = ""
    ALERT_OPTION = "ALERT_OPTION"
    ALERT_OPTION_DEFER = "*DEFER"
    ALERT_OPTION_IMMEDIATE = "*IMMED"
    ALERT_OPTION_NO = "*NO"
    ALERT_OPTION_UNATTENDED = "*UNATTEND"
    DATE_SENT = "DATE_SENT"
    DEFAULT_REPLY = "DEFAULT_REPLY"
    MESSAGE_FILE = "MESSAGE_FILE"
    MESSAGE_HELP = "MESSAGE_HELP"
    MESSAGE_ID = "MESSAGE_ID"
    MESSAGE_KEY = "MESSAGE_KEY"
    MESSAGE_QUEUE = "MESSAGE_QUEUE"
    MESSAGE_SEVERITY = "MESSAGE_SEVERITY"
    MESSAGE_TEXT = "MESSAGE_TEXT"
    MESSAGE_TYPE = "MESSAGE_TYPE"
    REPLY_STATUS = "REPLY_STATUS"
    REPLY_STATUS_ACCEPTS_NOT_SENT = "W"
    REPLY_STATUS_ACCEPTS_SENT = "A"
    REPLY_STATUS_NOT_ACCEPT = "N"
    SENDER_JOB_NAME = "SENDER_JOB_NAME"
    SENDER_JOB_NUMBER = "SENDER_JOB_NUMBER"
    SENDER_USER_NAME = "SENDER_USER_NAME"
    SENDING_PROGRAM_NAME = "SENDING_PROGRAM_NAME"
    SUBSTITUTION_DATA = "SUBSTITUTION_DATA"




    def __init__(self, queuedmessage):
        self.queuedmessage = jpype.JClass('com.ibm.as400.access.QueuedMessage')
        self.queuedmessage = queuedmessage


    # Devuelve la opción de alerta.
    def getQMAlertOption(self):

        """
            La opción de alerta. Los valores posibles son:

                *DEFER: se envía una alerta después del análisis del problema local.
                *IMMED: se envía una alerta inmediatamente cuando el mensaje se envía a una cola de mensajes que tiene el atributo de permitir alertas establecido en *YES.
                *NO - No se envía ninguna alerta.
                *UNATTEND: se envía una alerta inmediatamente cuando el sistema se ejecuta en modo desatendido. Consulte el atributo de red ALRSTS.
                "": la opción de alerta no se especificó cuando se envió el mensaje.

        """

        accion = {
            self.ALERT_OPTION_DEFER : 'ALERT_OPTION_DEFER',
            self.ALERT_OPTION_IMMEDIATE : 'ALERT_OPTION_IMMEDIATE',
            self.ALERT_OPTION_NO : 'ALERT_OPTION_NO',
            self.ALERT_OPTION_SIN_INFORMACION : 'ALERT_OPTION_SIN_INFORMACION',
            self.ALERT_OPTION_UNATTENDED : 'ALERT_OPTION_UNATTENDED'
        }

        return accion[self.queuedmessage.getAlertOption()]

    # Devuelve el identificador de juego de caracteres codificado (CCSID) en el que se devuelven los datos de reemplazo.
    def getQMCcsidCodedCharacterSetIdentifierForData(self):

        """
            Esto solo se aplica a la parte de los datos de reemplazo que corresponde a un tipo de datos de caracteres convertibles (*CCHAR).
            Todos los demás datos de reemplazo no se convertirán antes de que se devuelvan y se puede considerar que tienen un CCSID de 65535.
            Si se produce un error de conversión o si el CCSID al que solicitó convertir los datos es 65535, se devuelve el CCSID de los datos. .
            Si no hay datos de reemplazo *CCHAR, se devuelve 65535. De lo contrario, se devuelve el CCSID al que deseaba convertir los datos.

            retorna integer


        """

        return self.queuedmessage.getCcsidCodedCharacterSetIdentifierForData()

    # Devuelve el identificador de juego de caracteres codificado (CCSID) en el que se devuelve el texto del mensaje.
    def getQMCcsidCodedCharacterSetIdentifierForText(self):

        """
            Si se produce un error de conversión o si el CCSID que solicitó en el texto del mensaje para convertirlo es 65535,
            se devuelve el CCSID en el que se almacena el texto del mensaje. .
            De lo contrario, se devuelve el CCSID al que deseaba convertir el texto de su mensaje.
            Si no desea que el texto se convierta antes de que se lo devuelvan, pero desea conocer el CCSID
            en el que se almacena el texto del mensaje, especifique 65535 en el identificador del conjunto de caracteres
            codificados para devolver el texto y los datos en el parámetro. El CCSID en el que se almacena el texto del mensaje
            se devuelve en el identificador de conjunto de caracteres codificados para el campo de texto.

            Devolucion
                El identificador de juego de caracteres codificado (CCSID) en el que se devuelve el texto del mensaje o nulo si no se establece. Los valores posibles son:
                    Esto se aplica solo a los siguientes campos:
                        * Mensaje
                        * Mensaje con datos de reemplazo
                        * Mensaje de ayuda
                        * Mensaje de ayuda con datos de reemplazo
                        * Mensaje de ayuda con datos de reemplazo y formateo caracteres
                        * Mensaje de ayuda con caracteres de formato
                    Nota:   este valor de CCSID no se aplica a los datos de sustitución que se han sustituido en el texto.
                                Consulte el identificador de juego de caracteres codificados para obtener esta información.

            retorna integer

        """

        return self.queuedmessage.getCcsidCodedCharacterSetIdentifierForText()

    # Devuelve el indicador de estado de conversión CCSID para datos.
    def getQMCcsidconversionStatusIndicatorForData(self):

        """
                Devoluciones:
                El indicador de estado de conversión de CCSID para datos o nulo si no se establece. Los valores posibles son:
                    0: no se necesitó ninguna conversión porque el CCSID de los datos coincidía con el CCSID al que deseaba convertir los datos.
                    1 - No se produjo ninguna conversión porque los datos eran 65535 o el CCSID al que deseaba convertir los datos era 65535.
                    2 - No se produjo ninguna conversión porque no solicitó que se devolvieran los datos del mensaje o los datos no contenían ningún tipo de datos *CCHAR.
                    3 - Los datos se convirtieron al CCSID especificado utilizando las tablas de conversión de mejor ajuste.
                    4: se produjo un error de conversión al usar las tablas de conversión de mejor ajuste, por lo que se intentó una conversión predeterminada. Esto completó sin error.
                    -1: se produjo un error en las conversiones de mejor ajuste y predeterminadas. Los datos no se convirtieron.

               retorna integer

        """
        return self.queuedmessage.getCcsidconversionStatusIndicatorForData()

    # Devuelve el indicador de estado de conversión de CCSID para texto.
    def getQMCcsidConversionStatusIndicatorForText(self):

        """
            Devoluciones:
            El indicador de estado de conversión de CCSID para texto o nulo si no se establece. Valores posibles_ son:
                0: no se necesitó ninguna conversión porque el CCSID del texto coincidía con el CCSID al que deseaba convertir el texto.
                1 - No se produjo ninguna conversión porque el texto era 65535 o el CCSID al que deseaba convertir el texto era 65535.
                2 - No se produjo ninguna conversión porque no solicitó que se devolviera ningún texto.
                3 - El texto se convirtió al CCSID especificado utilizando las tablas de conversión de mejor ajuste.
                4: se produjo un error de conversión al usar las tablas de conversión de mejor ajuste, por lo que se intentó una conversión predeterminada. Esto completó sin error.
                -1: se produjo un error en las conversiones de mejor ajuste y predeterminadas. Los datos no se convirtieron.

            retorna integer

        """
        return self.queuedmessage.getCcsidConversionStatusIndicatorForText()

    # Devuelve el usuario del trabajo del remitente.
    def getQMCurrentUser(self):

        """
            Para obtener el usuario actual del mensaje, llame getCurrentUser()al acceder a un sistema que ejecuta V5R3 o superior.
            return string (El usuario del trabajo del remitente, o "" si no está configurado.)

        """
        return self.queuedmessage.getCurrentUser()

    # Devuelve el nombre del trabajo del remitente.
    def getQMFromJobName(self):

        """

            return  El nombre del trabajo del remitente, o "" si no está configurado.

        """
        return self.queuedmessage.getFromJobName()


    # Devuelve el número de trabajo del remitente.
    def getQMFromJobNumber(self):
        """

            return El número de trabajo del remitente, o "" si no está configurado.

        """
        return self.queuedmessage.getFromJobNumber()


    # Devuelve el nombre del programa de envío.
    def getQMFromProgram(self):

        """

            return  El nombre del programa de envío, o "" si no está configurado.

        """

        return self.queuedmessage.getFromProgram()



    # Devuelve la clave de mensaje de 4 bytes.
    def  getQMKey(self):

        """

            return  La clave del mensaje, o nula si no está configurada.
            bytearray
        """
        return bytearray(self.queuedmessage.getKey())

    # Devuelve el texto de un mensaje predefinido sin la opción de sustitución de datos de reemplazo.
    def getQMMessage(self):
        """
            Si aparece un mensaje improvisado, este campo contiene el texto del mensaje improvisado.

            return El mensaje sin datos de reemplazo o una cadena vacía si no se establece.
            string

        """
        return str(self.queuedmessage.getMessage())


    # Devuelve la ayuda del mensaje para el mensaje enumerado sin formatear los caracteres
    def getQMMessageHelp(self):

        """
            Devuelve la ayuda del mensaje para el mensaje enumerado sin formatear los caracteres
            y sin reemplazar los datos. Si aparece un mensaje improvisado, este campo contiene el texto del mensaje improvisado.

            return  La ayuda del mensaje para el mensaje enumerado sin formatear caracteres y sin reemplazo de datos o una cadena vacía si no se establece.
            string

        """
        return self.queuedmessage.getMessageHelp()

    # Devuelve la ayuda del mensaje para el mensaje enumerado,
    def getQMMessageHelpFormat(self):

        """
            Devuelve la ayuda del mensaje para el mensaje enumerado,
            incluidos los datos de reemplazo pero sin los caracteres de formato.
            Si aparece un mensaje improvisado, este campo contiene el texto del mensaje improvisado.

            return  La ayuda del mensaje para el mensaje enumerado, incluidos los datos de reemplazo y los caracteres de formato o una cadena vacía si no se establece.
            string

        """
        return self.queuedmessage.getMessageHelpFormat()



    # Devuelve la ayuda del mensaje para el mensaje enumerado, incluidos los datos de reemplazo.
    # Si aparece un mensaje improvisado, este campo contiene el texto del mensaje improvisado.
    def getQMMessageHelpReplacement(self):

        """
            Devuelve la ayuda del mensaje para el mensaje enumerado, incluidos los datos de reemplazo.
            Si aparece un mensaje improvisado, este campo contiene el texto del mensaje improvisado.

            return La ayuda del mensaje para el mensaje enumerado, incluidos los datos de reemplazo o una cadena vacía si no se establece.
            string
        """
        return self.queuedmessage.getMessageHelpReplacement()



    # Devuelve la ayuda del mensaje para el mensaje enumerado,
    def getQMMessageHelpReplacementandFormat(self):

        """
               Devuelve la ayuda del mensaje para el mensaje enumerado,
               incluidos los datos de reemplazo y los caracteres de formato.
               Si aparece un mensaje improvisado, este campo contiene el texto del mensaje improvisado.

         return La ayuda del mensaje para el mensaje enumerado, incluidos los datos de reemplazo y los caracteres de formato o una cadena vacía si no se establece.
         string
        """
        self.queuedmessage.getMessageHelpReplacementandFormat()

    # Devuelve la cola de mensajes.
    def getQMQueue(self):

        """

            return La cola de mensajes, o nula si no está configurada.
        """
        return self.queuedmessage.getQueue()

    # Devuelve el número de números de instrucción o números de instrucciones disponibles para el programa o procedimiento receptor.
    def getQMReceiverStatementNumbers(self):

        """
            Devuelve el número de números de instrucción o números de instrucciones disponibles para el programa o procedimiento receptor.
            Para los programas del modelo de programa original (OPM) y los procedimientos no optimizados,
            este recuento es 1. Para los procedimientos optimizados, este recuento puede ser superior a 1.
            En este caso, cada número de declaración representa un punto potencial en el que se podría haber recibido el mensaje.
            Si la información de la tabla de asignación se eliminó del programa, este campo devuelve un recuento de 0 y no hay números de declaración disponibles.
            La matriz de números de declaración de recepción o números de instrucción sigue inmediatamente a este campo en los datos devueltos. return
            El número de números de instrucción o números de instrucciones disponibles para el programa o
            procedimiento receptor o una matriz de cadenas nulas si no se establece nada.

            returrn  lista string
        """
        return self.queuedmessage.getReceiverStatementNumbers()



    # Devuelve el nombre del procedimiento que recibe el mensaje.
    def getQMReceivingModuleName(self):

        """
                Devuelve el nombre del procedimiento que recibe el mensaje.
                Si el mensaje no se envió a un procedimiento dentro de un programa ILE, este campo no se establece
                y la longitud del campo de datos es 0. Un nombre de procedimiento anidado tiene cada nombre
                de procedimiento separado por dos puntos. El nombre del procedimiento más externo se identifica primero,
                seguido de los procedimientos que contiene. El procedimiento más interno se identifica en último lugar en la cadena.

                return El nombre del procedimiento que recibe el mensaje o una cadena vacía si no se establece.

        """
        return self.queuedmessage.getReceivingModuleName()



    # Devuelve el nombre del procedimiento que recibe el mensaje.
    def getQMReceiveProcedureName(self):

        """
            Devuelve el nombre del procedimiento que recibe el mensaje.
            Si el mensaje no se envió a un procedimiento dentro de un programa ILE,
            este campo no se establece y la longitud del campo de datos es 0.
            Un nombre de procedimiento anidado tiene cada nombre de procedimiento separado por dos puntos.
            El nombre del procedimiento más externo se identifica primero, seguido de los procedimientos que contiene.
            El procedimiento más interno se identifica en último lugar en la cadena.

            return El nombre del procedimiento que recibe el mensaje o una cadena vacía si no se establece.
            string
        """

        return self.queuedmessage.getReceiveProcedureName()



    # Devuelve el nombre del programa, o el nombre del programa ILE que contiene el procedimiento al que se envió el mensaje.
    def getQMReceiveProgramName(self):

        """

            return El nombre del programa o el nombre del programa ILE o una cadena vacía si no se ha establecido.


        """
        return self.queuedmessage.getReceiveProgramName()


    # Devuelve el tipo de receptor (ya sea un programa o un procedimiento).
    def getQMReceivingType(self):

        """
            El tipo del receptor o una cadena vacía si no se establece. Los valores posibles son:
                0 - El receptor es un programa de modelo de programa original (OPM)
                1 - El receptor es un procedimiento dentro de un programa ILE y el nombre del procedimiento tiene una longitud máxima de 256 caracteres inclusive
                2 - El receptor es un procedimiento dentro de un programa ILE y el nombre del procedimiento tiene 257 o más caracteres de longitud.

        """

        return self.queuedmessage.getReceivingType()



    # Devuelve el estado de respuesta.
    def getQMReplyStatus(self):

        """
            return El estado de respuesta, "" si no está establecido, o nulo si no es aplicable.
            string

        """
        return self.queuedmessage.getReplyStatus()


    # Devuelve el nivel del programa de procesamiento de solicitudes que recibió el mensaje de solicitud.
    def getQMRequestLevel(self):

        """
            Devuelve el nivel del programa de procesamiento de solicitudes que recibió el mensaje de solicitud.
            Si el mensaje que se enumera no es una solicitud, este campo se establece en 0.


            retunr El nivel del programa de procesamiento de solicitudes que recibió el mensaje de solicitud o una cadena vacía si no se establece.
            integer:
        """
        return self.queuedmessage.getRequestLevel()


    # Devuelve información sobre el estado de procesamiento del mensaje de solicitud.
    def getQMRequestStatus(self):

        """

            return string
            formación sobre el estado de procesamiento del mensaje de solicitud o una cadena vacía si no se establece. Los valores posibles son:
                O - Este mensaje de solicitud ha sido recibido y procesado.
                C: este mensaje de solicitud se está procesando actualmente.
                N: este mensaje de solicitud aún no se ha procesado.

        """
        return self.queuedmessage.getRequestStatus()


    # Devuelve el tipo del remitente (si es un programa o un procedimiento).
    def getQMSenderType(self):

        """
            return string
            El tipo del remitente o una cadena vacía si no se establece. Los valores posibles son:
                0: el remitente es un OPM o un programa de código interno con licencia del sistema (SLIC) con un nombre de 12 caracteres o menos.
                1 - El remitente es un procedimiento dentro de un programa ILE y el nombre del procedimiento tiene una longitud máxima de 256 caracteres.
                2 - Sender es un procedimiento dentro de un programa ILE y el nombre del procedimiento tiene una longitud de 257 caracteres hasta 4096 caracteres inclusive.
                3 - Sender es un programa SLIC con un nombre de 13 caracteres hasta 256 caracteres inclusive.

        """
        return self.queuedmessage.getSenderType()




    # Devuelve el nombre del módulo que contiene el procedimiento que envía el mensaje.
    def getQMSendingModuleName(self):

        """
                Devuelve el nombre del módulo que contiene el procedimiento que envía el mensaje.
                Si el mensaje no fue enviado por un procedimiento dentro de un programa ILE,
                este campo no se establece y la longitud del campo de datos es 0.

                retrun  string
                El nombre del módulo que contiene el procedimiento que envía el mensaje o una cadena vacía si no se establece.

        """
        return self.queuedmessage.getSendingModuleName()



    # Devuelve el nombre del procedimiento que envía el mensaje.
    def getQMSendingProcedureName(self):

        """
                Devuelve el nombre del procedimiento que envía el mensaje.
                Si el mensaje no lo envió un procedimiento dentro de un programa ILE,
                este campo no se establece y la longitud del campo de datos es 0.
                Un nombre de procedimiento anidado tiene cada nombre de procedimiento separado por dos puntos.
                El nombre del procedimiento más externo se identifica primero, seguido de los procedimientos que contiene.
                El procedimiento más interno se identifica en último lugar en la cadena.

                return string
                El nombre del procedimiento que envía el mensaje o una cadena vacía si no se establece.

        """
        return self.queuedmessage.getSendingProcedureName()


    # Devuelve el número de números de declaración de envío o números de instrucción
    def getQMSendingStatementNumbers(self):

        """
                Devuelve el número de números de declaración de envío o números de instrucción
                disponibles seguidos de una matriz de números de declaración de envío o números de instrucción.
                El número de números de instrucciones o números de instrucciones disponibles
                para el programa o procedimiento de envío.
                Para programas OPM y procedimientos no optimizados, este recuento es 1.
                Para procedimientos optimizados, este recuento puede ser superior a 1.
                En este caso, cada número de declaración representa un punto potencial
                en el que se podría haber enviado el mensaje. Si la información de la
                tabla de asignación se eliminó del programa, este campo devuelve un recuento
                de 0 y no hay números de declaración disponibles.
                La matriz de envío de números de instrucciones o números de instrucciones
                sigue inmediatamente a este campo en los datos devueltos.

                return lista string
                No se establece el número de números de instrucción de envío o números de instrucción
                disponibles seguidos de una matriz de números de instrucción de envío o números de instrucción o una matriz de cadena nula.

        """
        return self.queuedmessage.getSendingStatementNumbers()


    # Devuelve el nombre del perfil de usuario con el que se estaba ejecutando el subproceso cuando se envió el mensaje.
    def getQMSendingUserProfile(self):

        """
            return string
            El nombre del perfil de usuario bajo el que se estaba ejecutando el subproceso o una cadena vacía si no se ha establecido.

        """
        return self.queuedmessage.getSendingUserProfile()


    # Devuelve la representación de cadena de este objeto QueuedMessage.
    def toQMString(self):

        """

            return string
            toString en la clase AS400Message

        """
        return self.queuedmessage.toString()

