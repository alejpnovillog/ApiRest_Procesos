# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os

except Exception as e:
    print(f'Falta algun modulo {e}')


class QSYSObjectPathName():


    # Constructor
    def __int__(self):

        """
        asignar el path al atributo qsysobjectpathname

        addPropertyChangeListener(jPropertyChangeListener listener)
            Agrega un oyente para recibir una notificación cuando se cambia
            el valor de cualquier propiedad enlazada.

        addVetoableChangeListener(VetoableChangeListener listener)
            Agrega un oyente para recibir una notificación cuando se cambia
            el valor de cualquier propiedad restringida.

        String = getAspName()
            Devuelve la ASP en la que reside el objeto.

        String = getLibraryName()
            Devuelve la biblioteca en la que reside el objeto.

        String = getMemberName()
            Devuelve el nombre del miembro.

        String = getObjectName()
            Devuelve el nombre del objeto que representa este nombre de ruta.

        String = getObjectType()
            Devuelve el tipo de objeto que representa este nombre de ruta.

        String = getPath()
            Devuelve el nombre de vía de acceso del sistema de archivos integrado completo.

        removePropertyChangeListener(PropertyChangeListener listener)
            Elimina un oyente de la lista de cambios.

        removeVetoableChangeListener(VetoableChangeListener listener)
            Elimina un oyente de la lista de vetos.

        setAspName(String aspName)
            Establece la IASP en la que reside el objeto.

        setLibraryName(String libraryName)
            Establece la biblioteca en la que reside el objeto.

        setMemberName(String memberName)
            Establece el nombre del miembro.

        setObjectName(String objectName)
            Establece el nombre del objeto que representa este nombre de ruta.

        setObjectType(String objectType)
            Establece el tipo de objeto que representa este nombre de ruta.

        setPath(String path)
            Establece el nombre de vía de acceso del sistema de
            archivos integrado para este objeto.

        String = toPath(String libraryName, String objectName, String objectType)
            Crea un nombre de vía de acceso del sistema de archivos
            integrado para representar el objeto.

        String = toPath(String libraryName, String objectName, String memberName, String objectType)
            Crea un nombre de vía de acceso del sistema de archivos
            integrado para representar al miembro.

        String = toPath(String aspName, String libraryName, String objectName, String memberName, String objectType)
            Crea un nombre de vía de acceso del sistema de archivos
            integrado para representar al miembro.

        String = toQSYSName(String name)
            Método de utilidad para escribir en mayúsculas de forma selectiva l
            os caracteres de una cadena, para utilizar como un valor *NAME de IBM i.

        String = toQualifiedObjectName()
            Devuelve un nombre de objeto calificado, para usar en parámetros de API.


        """
        self.qsysobjectpathname = jpype.JClass('com.ibm.as400.access.QSYSObjectPathName')





