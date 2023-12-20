
# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os

except Exception as e:
    print(f'Falta algun modulo {e}')



# Definimos la clase para manejar la iseries
class ObjectList():

    # Atributos
    ALL = "*ALL"
    ALL_USER = "*ALLUSR"
    ASP_NAME_ALL = "*"
    ASP_NAME_ALLAVL = "*ALLAVL"
    ASP_NAME_CURASPGRP = "*CURASPGRP"
    ASP_NAME_SYSBAS = "*SYSBAS"
    ASP_SEARCH_TYPE_ASP = "*ASP"
    ASP_SEARCH_TYPE_ASPGRP = "*ASPGRP"
    AUTH_ALL = "*ALL"
    AUTH_ANY = "*ANY"
    AUTH_CHANGE = "*CHANGE"
    AUTH_DATA_ADD = "*ADD"
    AUTH_DATA_DELETE = "*DLT"
    AUTH_DATA_EXECUTE = "*EXECUTE"
    AUTH_DATA_READ = "*READ"
    AUTH_DATA_UPDATE = "*UPD"
    AUTH_LIST_MANAGEMENT = "*AUTLMGT"
    AUTH_OBJECT_ALTER = "*OBJALTER"
    AUTH_OBJECT_EXISTENCE = "*OBJEXIST"
    AUTH_OBJECT_MANAGEMENT = "*OBJMGT"
    AUTH_OBJECT_OPERATIONAL = "*OBJOPR"
    AUTH_OBJECT_REFERENCE = "*OBJREF"
    AUTH_USE = "*USE"
    CURRENT_LIBRARY = "*CURLIB"
    IBM = "*IBM"
    LIBRARY_LIST = "*LIBL"
    STATUS_ANY = 92
    USER_LIBRARY_LIST = "*USRLIBL"

    # Constructor
    def __init__(self, system):

        """
        parametro
            system  = The system.

        addLibraryAuthorityCriteria(String authority= Atributo)
            Agrega una autoridad de biblioteca como parte de los
            criterios de selección para generar la lista de objetos.

        addObjectAttributeToRetrieve(int attribute)
            Agrega un atributo de objeto para recuperar cuando se crea esta lista.

        addObjectAttributeToSortOn(int attribute, boolean(True, False) sortOrder)
            Agrega un atributo de objeto utilizado para ordenar la lista.

        addObjectAuthorityCriteria(String authority =  authority)
            Agrega una autoridad de objeto como parte de los criterios de selección para generar la lista de objetos

        addObjectSelectionCriteria(byte status)
            Agrega un atributo de objeto utilizado para filtrar la lista.

        clearLibraryAuthorityCriteria()
            Borra los criterios de autoridad de la biblioteca utilizados para filtrar la lista.

        clearObjectAttributesToRetrieve()
            Borra los atributos del objeto para recuperar como parte de esta lista.

        clearObjectAttributesToSortOn()
            Borra los atributos de objeto utilizados para ordenar la lista.

        clearObjectAuthorityCriteria()
            Borra los criterios de autorización de objeto utilizados para filtrar la lista.

        clearObjectSelectionCriteria()
            Borra los estados de los objetos utilizados para filtrar la lista y
            restablece la selección de objetos para incluir objetos en la lista (verdadero).

        close()
        Cierra la lista de objetos en el sistema.

        finalize()
            Cierra la lista en el sistema cuando este objeto se recolecta como basura.

        String	getAspDeviceName()
            Devuelve el nombre de un dispositivo de grupo de almacenamiento auxiliar (ASP)
            en el que se asigna almacenamiento para la biblioteca que contiene el objeto.

        String	getAspSearchType()
            Devuelve el tipo de búsqueda que se utilizará cuando se especifica un
            nombre de dispositivo de grupo de almacenamiento auxiliar específico.

        int getLength()
            Devuelve el número de objetos en la lista de objetos.

        String	getLibrary()
            Devuelve la biblioteca utilizada para filtrar esta lista.

        String	getName()
            Devuelve el nombre del objeto utilizado para filtrar esta lista.

        Enumeration	getObjects()
            Devuelve la lista de objetos en la lista de objetos.

        ObjectDescription[]	getObjects(int listOffset, int number)
            Devuelve un subconjunto de la lista de objetos.

        AS400	getSystem()
            Devuelve el sistema.

        String	getType()
            Devuelve el tipo de objeto utilizado para filtrar esta lista.

        load()
            Carga la lista de objetos en el sistema.

        setAspSearchType(jString aspSearchType)
            Especifica el tipo de búsqueda cuando se especifica un nombre de dispositivo
            de grupo de almacenamiento auxiliar específico para el nombre de dispositivo ASP.

        setObjectSelection(boolean select)
            Establece si los criterios de selección de objetos se utilizan o
            no para incluir objetos en la lista o para omitirlos de la lista.

        documentacion
        https://www.ibm.com/docs/api/v1/content/ssw_ibm_i_72/rzahh/javadoc/com/ibm/as400/access/ObjectList.html#clearLibraryAuthorityCriteria()

        """

        self.objetoList = jpype.JClass('com.ibm.as400.access.ObjectList')

