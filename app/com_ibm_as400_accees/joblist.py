# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')


class JobList():


    ALL	 = "*ALL"
    SELECTION_ACTIVE_JOB_STATUS = 8
    SELECTION_INITIAL_USER = 13
    SELECTION_JOB_NAME  = 1
    SELECTION_JOB_NAME_ALL = "*ALL"
    SELECTION_JOB_NAME_CURRENT = "*CURRENT"
    SELECTION_JOB_NAME_ONLY = "*"
    SELECTION_JOB_NUMBER = 3
    SELECTION_JOB_NUMBER_ALL = "*ALL"
    SELECTION_JOB_QUEUE = 12
    SELECTION_JOB_QUEUE_STATUS_HELD = 10
    SELECTION_JOB_QUEUE_STATUS_READY = 11
    SELECTION_JOB_QUEUE_STATUS_SCHEDULE = 9
    SELECTION_JOB_TYPE = 4
    SELECTION_JOB_TYPE_ALL = "*"
    SELECTION_JOB_TYPE_ENHANCED = 17
    SELECTION_PRIMARY_JOB_STATUS_ACTIVE = 5
    SELECTION_PRIMARY_JOB_STATUS_JOBQ = 6
    SELECTION_PRIMARY_JOB_STATUS_OUTQ	 = 7
    SELECTION_SERVER_TYPE = 14
    SELECTION_SERVER_TYPE_ALL = "*ALL"
    SELECTION_SERVER_TYPE_BLANK = "*BLANK"
    SELECTION_USER_NAME = 2
    SELECTION_USER_NAME_ALL = "*ALL"
    SELECTION_USER_NAME_CURRENT = "*CURRENT"


    def __int__(self):

        """
        Constructores
        JobList()
        Construye un objeto JobList.
        JobList(AS400 system)
        Construye un objeto JobList.

        Job[]	getJobs(int listOffset, int number)
        Devuelve un subconjunto de la lista de trabajos en la lista de trabajos.

        """

        self.joblist = jpype.JClass('com.ibm.as400.access.JobList')


    # ***
    # Agrega un atributo de trabajo que se recuperará para cada trabajo en esta lista de trabajos.
    def addJLISTJobAttributeToRetrieve(self, atributo):

        """
        Agrega un atributo de trabajo que se recuperará para cada trabajo en esta lista de trabajos.

         void	addJobAttributeToRetrieve(int attribute)

         param:
            int attribute


        """
        self.joblist.addJobAttributeToRetrieve(atributo)



    # ***
    # Agrega un atributo de trabajo utilizado para ordenar la lista.
    def addJLISTJobAttributeToSortOn(self, atributo, orderby):

        """
        Agrega un atributo de trabajo utilizado para ordenar la lista.


        void	addJobAttributeToSortOn(int attribute, boolean sortOrder)

        param:
            int attribute
            boolean sortOrder


        """
        self.joblist.addJobAttributeToSortOn(atributo, orderby)


    #  ***
    # Agrega un tipo de selección y un valor que se utilizará para filtrar la lista de trabajos.
    def addJLISTJobSelectionCriteria(self, tiposeleccion, valorobjetoseleccion):

        """
        Agrega un tipo de selección y un valor que se utilizará para filtrar la lista de trabajos.

         void	addJobSelectionCriteria(int selectionType, java.lang.Object selectionValue)

         param:
            int selectionType
            java.lang.Object selectionValue


        """
        self.joblist.addJobSelectionCriteria(tiposeleccion, valorobjetoseleccion)


    # ***
    # Agrega un PropertyChangeListener.
    def addJLISTPropertyChangeListener(self, oyente):

        """
        Agrega un PropertyChangeListener.
        PropertyChangeListener especificado cada vez que se cambie el valor de cualquier propiedad enlazada.

         void	addPropertyChangeListener(java.beans.PropertyChangeListener listener)

         param:
            java.beans.PropertyChangeListener listener

        """
        self.joblist.addPropertyChangeListener(oyente)



    # ***
    # Agrega un VetoableChangeListener.
    def addJLISTVetoableChangeListener(self, oyente):

        """
        Agrega un VetoableChangeListener.
        VetoableChangeListener especificado cada vez que se cambie el valor de cualquier propiedad restringida.

        void	addVetoableChangeListener(java.beans.VetoableChangeListener listener)

        param:
            java.beans.VetoableChangeListener listener


        """
        self.joblist.addVetoableChangeListener(oyente)



    # ***
    # Borra los atributos del trabajo que se van a recuperar.
    def clearJLISTJobAttributesToRetrieve(self):

        """
        Borra los atributos del trabajo que se van a recuperar.
        void	clearJobAttributesToRetrieve()

        """
        self.joblist.clearJobAttributesToRetrieve()



    # ***
    # Borra los atributos de trabajo utilizados para ordenar la lista.
    def clearJLISTJobAttributesToSortOn(self):

        """
        Borra los atributos de trabajo utilizados para ordenar la lista.
         void	clearJobAttributesToSortOn()

        """
        self.joblist.clearJobAttributesToSortOn()


    # ***
    # Borra los tipos y valores de selección utilizados para filtrar la lista de trabajos.
    def clearJLISTJobSelectionCriteria(self):

        """
        Borra los tipos y valores de selección utilizados para filtrar la lista de trabajos.
        void	clearJobSelectionCriteria()

        """
        self.joblist.clearJobSelectionCriteria()


    # ***
    # Cierra la lista de trabajos en el sistema.
    def closeJLIST(self):

        """
        Cierra la lista de trabajos en el sistema.
        void	close()

        """
        self.joblist.close()


    # ***
    # Cierra la lista en el sistema cuando este objeto se recolecta como basura.
    def finalizeJLIST(self):

        """
        Cierra la lista en el sistema cuando este objeto se recolecta como basura.
        protected void	finalize()

        """
        self.joblist.finalize()


    # ***
    # Devuelve una enumeración que envuelve la lista de trabajos en el sistema.
    def getJLISTJobs(self):

        """
        Devuelve una enumeración que envuelve la lista de trabajos en el sistema.
        java.util.Enumeration = getJobs()

        """
        return list(self.joblist.getJobs())


    # ***
    # Devuelve el número de trabajos en la lista.
    def getJLISTLength(self):

        """
        Devuelve el número de trabajos en la lista.
        int = getLength()

        """
        return self.joblist.getLength()


    # ***
    # Devuelve el nombre del trabajo que describe qué trabajos se devuelven.
    def getJLISTName(self):

        """
        Devuelve el nombre del trabajo que describe qué trabajos se devuelven.
        java.lang.String = getName()

        """
        return self.joblist.getName()



    # ***
    # Devuelve el número de trabajo que describe qué trabajos se devuelven.
    def getJLISTNumber(self):

        """
        Devuelve el número de trabajo que describe qué trabajos se devuelven.
        java.lang.String = getNumber()

        """
        return self.joblist.getNumber()


    # ***
    # Devuelve el nombre de usuario que describe qué trabajos se devuelven.
    def getJLISTUser(self):

        """
        Devuelve el nombre de usuario que describe qué trabajos se devuelven.
        java.lang.String = getUser()

        """
        return self.joblist.getUser()


    # ***
    # Carga la lista de trabajos en el sistema.
    def loadJLIST(self):

        """
        Carga la lista de trabajos en el sistema.
        void	load()

        """
        self.joblist.load()


    #
    #  Elimina PropertyChangeListener.
    def removeJLISTPropertyChangeListener(self, oyente):

        """
        Elimina PropertyChangeListener.
        void	removePropertyChangeListener(java.beans.PropertyChangeListener listener)

        param:
            java.beans.PropertyChangeListener listener

        """
        self.joblist.removePropertyChangeListener(oyente)



    # ***
    # Elimina VetoableChangeListener.
    def removeJLISTVetoableChangeListener(self, oyente):

        """
        Elimina VetoableChangeListener.
        void	removeVetoableChangeListener(java.beans.VetoableChangeListener listener)

        param:
            java.beans.VetoableChangeListener listener


        """
        self.joblist.removeVetoableChangeListener()



    # ***
    # Establece el nombre del trabajo que describe qué trabajos se devuelven.
    def setJLISTName(self, nombre):

        """
        Establece el nombre del trabajo que describe qué trabajos se devuelven.
        void	setName(java.lang.String name)

        param:
            java.lang.String name

        """
        self.joblist.setName(nombre)



    # ***
    # Establece el número de trabajo que describe qué trabajos se devuelven.
    def setJLISTNumber(self, numero):

        """
        Establece el número de trabajo que describe qué trabajos se devuelven.
        void	setNumber(java.lang.String number)

        param:
            java.lang.String number

        """
        self.joblist.setNumber(numero)


    #  ***
    # Establece el objeto del sistema que representa el sistema en el que existen los trabajos.
    def setJLISTSystem(self, sistema):

        """
        Establece el objeto del sistema que representa el sistema en el que existen los trabajos.
        void	setSystem(AS400 system)

        param:
            AS400 system

        """
        self.joblist.setSystem(sistema)



    # ***
    # Establece el valor del nombre de usuario que describe qué trabajos se devuelven.
    def setJLISTUser(self, usuario):

        """
        Establece el valor del nombre de usuario que describe qué trabajos se devuelven.
        void	setUser(java.lang.String user)
        param:
            java.lang.String user

        """
        self.joblist.setUser(usuario)



    # ***
    # Devuelve el objeto del sistema que representa el sistema en el que existen los trabajos.
    def getJLISTSystem(self):

        """
        Devuelve el objeto del sistema que representa el sistema en el que existen los trabajos.
        AS400 = getSystem()

        """
        return self.joblist.getSystem()


