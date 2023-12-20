try:
        import jpype
        import os
        from com_ibm_as400_accees.printObject import PrintObject

except Exception as e:
    print(f'Falta algun modulo {e}')


class PrintObjectInputStream():


    def __init__(self):

        """
            int	read(byte[] data)
            Lee hasta data.length bytes de datos de este flujo de entrada en data .
            int	read(byte[] data, int dataOffset, int length)
            Lee hasta bytes de longitud de datos de este flujo de entrada en data , comenzando en la compensación de matriz dataOffset .
            long	skip(long bytesToSkip)
            Salta los siguientes bytesToSkip bytes en la secuencia.

        """
        self.printobjectinputstream = jpype.JClass('com.ibm.as400.access.PrintObjectInputStream')


    # ***
    # Devuelve el número de bytes que se pueden leer sin bloquear.
    def availablePOINPSTR(self):

        """
            Devuelve el número de bytes que se pueden leer sin bloquear.
            int = available()

        """
        return self.printobjectinputstream.available()


    # ***
    # Cierra el flujo de entrada.
    def closePOINPSTR(self):

        """
            Cierra el flujo de entrada.
            void	close()

        """
        self.printobjectinputstream.close()


    # ***
    # Marca la posición actual en el flujo de entrada.
    def markPOINPSTR(self, readlimit):

        """
            Marca la posición actual en el flujo de entrada.
             void	mark(int readLimit)

        """
        self.printobjectinputstream.mark(readlimit)


    # ***
    # Devuelve un valor booleano que indica si este tipo de flujo admite marcar/restablecer.
    def markPOINPSTRSupported(self):

        """
        Devuelve un valor booleano que indica si este tipo de flujo admite marcar/restablecer.
         boolean = markSupported()

        """
        return self.printobjectinputstream.markSupported()



    # ***
    # Lee el siguiente byte de datos de este flujo de entrada.
    def readPOINPSTR(self):

        """
        Lee el siguiente byte de datos de este flujo de entrada.
        int = read()

        """
        return self.printobjectinputstream.read()



    #  ***
    #  Reposiciona la transmisión a la última posición marcada.
    def resetPOINPSTR(self):

        """
        Reposiciona la transmisión a la última posición marcada.
        void	reset()

        """
        self.printobjectinputstream.reset()


