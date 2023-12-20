# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')


class CallStackEntry():

    def __int__(self, stack):

        """
        stack = la pila recibida

        """

        # genero una instancia de la clase com.ibm.as400.access.CallStackEntry
        self.callstackentry = jpype.JClass('com.ibm.as400.access.CallStackEntry')

        # asigno a la instancia el objeto stack
        self.callstackentry = stack



    # ***
    # Devuelve el nombre del grupo de activación dentro del cual se ejecuta el programa o procedimiento.
    def getSENTRYActivationGroupName(self):

        """
        Devuelve el nombre del grupo de activación dentro del cual se ejecuta el programa o procedimiento.
        java.lang.String = getActivationGroupName()

        """
        return self.callstackentry.getActivationGroupName()


    # ***
    # Devuelve el número del grupo de activación dentro del cual se está ejecutando el programa o procedimiento.
    def getSENTRYActivationGroupNumber(self):

        """
        Devuelve el número del grupo de activación dentro del cual se está ejecutando el programa o procedimiento.
        long = getActivationGroupNumber()

        """
        return self.callstackentry.getActivationGroupNumber()


    # ***
    # Devuelve el objeto Trabajo que generó esta entrada de la pila de llamadas.
    def getSENTRYJob(self):

        """
        Devuelve el objeto Trabajo que generó esta entrada de la pila de llamadas.
         Job = getJob()

        """
        return self.callstackentry.getJob()


    # ***
    # Devuelve el número de instrucción de máquina actual en el programa.
    def getSENTRYMIInstructionNumber(self):

        """
        Devuelve el número de instrucción de máquina actual en el programa.
        int = getMIInstructionNumber()


        """
        return self.callstackentry.getMIInstructionNumber()

    # ***
    # Devuelve la biblioteca en la que se encuentra el módulo.
    def getSENTRYModuleLibrary(self):

        """
        Devuelve la biblioteca en la que se encuentra el módulo.
        java.lang.String = getModuleLibrary()

        """
        return self.callstackentry.getModuleLibrary()

    # ***
    # Devuelve el módulo que contiene el procedimiento del entorno de lenguaje integrado (ILE).
    def getSENTRYModuleName(self):

        """
        Devuelve el módulo que contiene el procedimiento del entorno de lenguaje integrado (ILE).
         java.lang.String	 = getModuleName()

        """
        return self.callstackentry.getModuleName()


    # ***
    # Devuelve el nombre del procedimiento en este nivel de la pila de llamadas.
    def getSENTRYProcedureName(self):
        """
        Devuelve el nombre del procedimiento en este nivel de la pila de llamadas.
        java.lang.String = getProcedureName()

        """
        return self.callstackentry.getProcedureName()


    #  ***
    # Devuelve el nombre del dispositivo de agrupación de almacenamiento
    # auxiliar (ASP) en el que se encuentra el programa.
    def getSENTRYProgramASPName(self):

        """
            Devuelve el nombre del dispositivo de agrupación de almacenamiento
            auxiliar (ASP) en el que se encuentra el programa.

            java.lang.String = getProgramASPName()

        """
        return self.callstackentry.getProgramASPName()


    #  ***
    # Devuelve el identificador numérico del dispositivo de agrupación de
    # almacenamiento auxiliar (ASP) que contiene el programa.
    def getSENTRYProgramASPNumber(self):

        """
            Devuelve el identificador numérico del dispositivo de agrupación de
            almacenamiento auxiliar (ASP) que contiene el programa.

            int = getProgramASPNumber()

        """
        return self.callstackentry.getProgramASPNumber()


    # ***
    # Devuelve la biblioteca en la que se encuentra el programa.
    def getSENTRYProgramLibrary(self):

        """
        Devuelve la biblioteca en la que se encuentra el programa.
        java.lang.String = getProgramLibrary()

        """
        return self.callstackentry.getProgramLibrary()


    # ***
    # Devuelve el nombre del dispositivo de agrupación de almacenamiento
    # auxiliar (ASP) en el que se encuentra la biblioteca de programas.
    def getSENTRYProgramLibraryASPName(self):

        """
            Devuelve el nombre del dispositivo de agrupación de almacenamiento
            auxiliar (ASP) en el que se encuentra la biblioteca de programas.
            java.lang.String = getProgramLibraryASPName()

        """
        return self.callstackentry.getProgramLibraryASPName()


    # ***
    # Devuelve el identificador numérico del dispositivo de agrupación
    # de almacenamiento auxiliar (ASP) que contiene la biblioteca de programas.
    def getSENTRYProgramLibraryASPNumber(self):

        """
            Devuelve el identificador numérico del dispositivo de agrupación
            de almacenamiento auxiliar (ASP) que contiene la biblioteca de programas.
            int = getProgramLibraryASPNumber()

        """
        return self.callstackentry.getProgramLibraryASPNumber()

    # ***
    # Devuelve el nombre del procedimiento en este nivel de la pila de llamadas.
    def getSENTRYProgramName(self):

        """
        Devuelve el nombre del procedimiento en este nivel de la pila de llamadas.
        java.lang.String	getProgramName()

        """
        return self.callstackentry.getProgramName()


    # ***
    # Devuelve el nivel del programa o procedimiento de procesamiento de solicitudes.
    def getSENTRYRequestLevel(self ):

        """
        Devuelve el nivel del programa o procedimiento de procesamiento de solicitudes.
        int = getRequestLevel()

        """
        return self.callstackentry.getRequestLevel()


    #  ***
    # Devuelve el identificador de declaración de idioma de alto nivel.
    def getSENTRYStatementIdentifier(self):

        """
        Devuelve el identificador de declaración de idioma de alto nivel.
        java.lang.String[] = getStatementIdentifier()

        """
        return self.callstackentry.getStatementIdentifier()

    # ***
    # Devuelve el identificador del subproceso a cuya pila
    # de llamadas pertenece esta entrada.
    def getSENTRYThreadID(self):

        """
            Devuelve el identificador del subproceso a cuya pila
            de llamadas pertenece esta entrada.
            long	getThreadID()

        """
        return self.callstackentry.getThreadID()


    # ***
    # Indica si un límite de control está activo para un programa
    # o procedimiento en particular.
    def isSENTRYControlBoundaryActive(self):

        """
            Indica si un límite de control está activo para un programa
            o procedimiento en particular.
            boolean = isControlBoundaryActive()

        """
        return self.callstackentry.isControlBoundaryActive()


    #         java.lang.String	toString()
    # Devuelve una representación de cadena de esta entrada de la pila de llamadas.
    def toSENTRYString(self):

        """
        Devuelve una representación de cadena de esta entrada de la pila de llamadas.
        java.lang.String = toString()

        """
        return self.callstackentry.toString()
