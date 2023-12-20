# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        from com_ibm_as400_accees.printObject import PrintObject
        from com_ibm_as400_accees.printobjectinputstream import PrintObjectInputStream

except Exception as e:
    print(f'Falta algun modulo {e}')


class SpooledFile(PrintObject):

    HOLD_IMMED = '*IMMED'
    HOLD_PAGEEND = '*PAGEEND'


    def __int__(self, system = None, name = None, number = None, jobname = None, jobuser = None, jobnumber = None, jobsysname = None, createdate = None):

        """

            #         PrintObjectInputStream = getInputACIFMergedStream(boolean acifB)
            #         Obsoleto.
            #         Utilice getAFPInputStream() en su lugar.

            #         PrintObjectInputStream = getInputStream(PrintParameterList ppl)
            #         Devuelve un flujo de entrada que se puede utilizar para leer el contenido del archivo en spool.

            #         PrintObjectPageInputStream = getPageInputStream(PrintParameterList pageStreamOptions)
            #         Devuelve un flujo de entrada de página que se puede utilizar para leer el contenido del archivo en spool, una página a la vez.

            #         PrintObjectTransformedInputStream = getTransformedInputStream(PrintParameterList transformOptions)
            #         Devuelve un flujo de entrada transformado que se puede utilizar para leer el contenido del archivo en spool.

            #         void	sendNet(PrintParameterList sendOptions)
            #         Envía el archivo en cola a otro usuario en el mismo sistema o a un sistema remoto en la red.

            #         void	sendTCP(PrintParameterList sendOptions)
            #         Envía un archivo en cola para que se imprima en un sistema remoto.

            #         void	setAttributes(PrintParameterList attributes)
            #         Establece uno o más atributos del objeto.

        """


        # asigna la clase java de SpoolFile
        self.spoolFile = jpype.JClass('com.ibm.as400.access.SpooledFile')

        # determina que constructor usamos
        if  (jobsysname == None) and (createdate == None):
            self.spoolFile = self.spoolFile(system, name, number, jobname, jobuser, jobnumber)
        else :
            self.spoolFile = self.spoolFile(system, name, number, jobname, jobuser, jobnumber, jobsysname, createdate)





    # ***
    # Responde al mensaje que provocó la espera del archivo en spool.
    def answerSPLFILEMessage(self, reply):

        """
            Responde al mensaje que provocó la espera del archivo en spool.
            void	answerMessage(java.lang.String reply)

            param:
                java.lang.String reply

        """
        self.spoolFile.answerMessage(reply)


    # ***
    # Crea una copia del archivo en spool que representa este objeto (SpooledFile).
    def copySPLFIL(self):

        """
            Crea una copia del archivo en spool que representa este objeto (SpooledFile).
            SpooledFile = copy()

        """
        return self.spoolFile.copy()


    # ***
    # Elimina el archivo en spool del sistema.
    def deleteSPLFIL(self):

        """
            Elimina el archivo en spool del sistema.
            void	delete()

        """
        self.spoolFile.delete()



    # ***
    # Devuelve la fecha de creación del archivo en spool.
    def getSPLFILCreateDate(self):

        """
            Devuelve la fecha de creación del archivo en spool.
            java.lang.String = 	getCreateDate()

        """
        return self.spoolFile.getCreateDate()


    # ***
    # Devuelve la hora de creación del archivo en spool.
    def getSPLFILCreateTime(self):

        """
            Devuelve la hora de creación del archivo en spool.
            java.lang.String = 	getCreateTime()

        """
        return self.spoolFile.getCreateTime()


    # ***
    # Devuelve el nombre del trabajo que creó el archivo en spool.
    def getSPLFILJobName(self):

        """
            Devuelve el nombre del trabajo que creó el archivo en spool.
            java.lang.String	 = getJobName()

        """
        return self.spoolFile.getJobName()


    # ***
    # Devuelve el número del trabajo que creó el archivo en spool.
    def getSPLFILJobNumber(self):

        """
            Devuelve el número del trabajo que creó el archivo en spool.
            java.lang.String =getJobNumber()

        """
        return self.spoolFile.getJobNumber()


    # ***
    # Devuelve el nombre del sistema donde se creó el archivo en spool.
    def getSPLFILJobSysName(self):

        """
            Devuelve el nombre del sistema donde se creó el archivo en spool.
            java.lang.String	 = getJobSysName()

        """
        return self.spoolFile.getJobSysName()


    # ***
    # Devuelve el ID del usuario que creó el archivo en spool.
    def getSPLFILJobUser(self):

        """
            Devuelve el ID del usuario que creó el archivo en spool.
            java.lang.String	 = getJobUser()

        """
        return self.spoolFile.getJobUser()


    # ***
    # Devuelve el nombre del archivo en spool.
    def getSPLFILName(self):

        """
            Devuelve el nombre del archivo en spool.
            java.lang.String = 	getName()

        """
        return self.spoolFile.getName()


    # ***
    # Devuelve el número del archivo en spool.
    def getSPLFILNumber(self):

        """
            Devuelve el número del archivo en spool.
            int = getNumber()


        """
        return self.spoolFile.getNumber()


    # ***
    # Mueve el archivo en spool a la primera posición en la cola de salida.
    def moveSPLFILToTop(self):

        """
            Mueve el archivo en spool a la primera posición en la cola de salida.
            void	moveToTop()

        """
        self.spoolFile.moveToTop()


    # ***
    # Libera un archivo en spool retenido en el sistema.
    def releaseSPLFIL(self):

        """
            Libera un archivo en spool retenido en el sistema.
            void	release()

        """
        self.spoolFile.release()


    # ***
    # Devuelve un flujo de entrada que se puede utilizar para leer el contenido del archivo en spool.
    def SPLFILInputStream(self):

        """
            Devuelve un flujo de entrada que se puede utilizar para leer el contenido del archivo en spool.
            PrintObjectInputStream = getInputStream()

        """
        return self.spoolFile.getInputStream()


    # ***
    # Contiene el archivo en spool.
    def holdSPLFIL(self, holdtype):

        """
            Contiene el archivo en spool.
            void	hold(java.lang.String holdType)

        """
        self.spoolFile.hold(holdtype)


    # ***
    # Devuelve el mensaje asociado con este archivo en spool.
    def getSPLFILMessage(self):

        """
        Devuelve el mensaje asociado con este archivo en spool.
         AS400Message = getMessage()

        """
        return self.spoolFile.getMessage()



    # ***
    # Mueve el archivo en spool a otra cola de salida oa otra posición en la misma cola de salida.
    def moveSPLFILspool(self, spooledfilefrom, spooledfileto):

        """
            Mueve el archivo en spool a otra cola de salida oa otra posición en la misma cola de salida.
            void	move(SpooledFile targetSpooledFile)

            param:
                spooledfilefrom
                spooledfileto

        """
        self.spoolFile.move(spooledfilefrom, spooledfileto)



    # ***
    # Mueve el archivo en spool a otra cola de salida.
    def moveSPLFILoutputqueue(self, outputqueuefrom, outputqueueto):

        """
            Mueve el archivo en spool a otra cola de salida.
            void	move(OutputQueue targetOutputQueue)

            param:
                outputqueuefrom
                outputqueueto


        """
        self.spoolFile.move(outputqueuefrom, outputqueueto)



    # ***
    # Crea una copia del archivo en spool que representa este objeto.
    def copySPLFILoutputqueue(self, outputqueuefrom, outputqueueto):

        """
            Crea una copia del archivo en spool que representa este objeto.
            SpooledFile = copy(OutputQueue outputQueue)

                param:
                    outputqueuefrom
                    outputqueueto


        """
        return self.spoolFile.copy(outputqueuefrom, outputqueueto)



