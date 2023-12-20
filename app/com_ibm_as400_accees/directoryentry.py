# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os


except Exception as e:
    print(f'Falta algun modulo {e}')


class DirectoryEntry():

    def __int__(self):

        """
        String = getAdministrationDomain()
                Devuelve el dominio de administración.

        String = getBuilding()
                Devuelve el edificio

        String = getCCMailAddress()
                Devuelve la dirección de cc:Mail.

        String = getCCMailComment()
                Devuelve el comentario de cc:Mail.

        String = getCompany()
                Devuelve la empresa

        String = getCountry()
                Devuelve el país o la región.

        String = getDepartment()
                Devuelve el departamento

        String = getDLOOwner()
                Devuelve a qué perfil se le asignará la propiedad de los objetos
                de biblioteca de documentos (DLO) para esta entrada de directorio.

        String = getDomainDefinedAttributeType1()
                Devuelve el tipo de atributo definido por el dominio 1.

        String = getDomainDefinedAttributeType2()
                Devuelve el tipo de atributo definido por el dominio 2.

        String = getDomainDefinedAttributeType3()
                Devuelve el tipo de atributo definido por el dominio 3.

        String = getDomainDefinedAttributeType4()
                Devuelve el tipo de atributo definido por el dominio 4.

        String = getDomainDefinedAttributeValue1()
                Devuelve el valor del atributo definido por el dominio 1.

        String = getDomainDefinedAttributeValue2()
                Devuelve el valor del atributo definido por el dominio 2.

        String = getDomainDefinedAttributeValue3()
                Devuelve el valor del atributo definido por el dominio 3.

        String = getDomainDefinedAttributeValue4()
                Devuelve el valor del atributo definido por el dominio 4.

        String = getFaxNumber()
                Devuelve el número de teléfono del fax.

        String = getFirstName()
                Devuelve el primer nombre.

        String = getFullName()
                Devuelve el nombre completo.

        String = getGenerationQualifier()
                Devuelve el calificador de generación.

        String = getGivenName()
                Devuelve el nombre dado.

        String = getInitials()
                Devuelve las iniciales.

        String = getJobTitle()
                Devuelve el título del trabajo.

        String = getLastName()
                Devuelve el apellido.

        String = getLocation()
                Devuelve la ubicación.

        String = getMailingAddress1()
                Devuelve la línea 1 de la dirección postal.

        String = getMailingAddress2()
                Devuelve la línea 2 de la dirección postal.

        String = getMailingAddress3()
                Devuelve la línea 3 de la dirección postal.

        String = getMailingAddress4()
                Devuelve la línea 4 de la dirección postal.

        String = getMailNotification()
                Devuelve el tipo de notificación de correo.

        String = getMailServiceLevel()
                Devuelve el valor del campo de nivel de servicio de
                correo y el ID del producto.

        String = getMailServiceName()
                Devuelve la parte del nombre del campo del nivel de servicio
                del marco del servidor de correo.

        String = getMailServiceProductID()
                Devuelve la parte del ID del producto del nivel de servicio
                del marco del servidor de correo.

        String = getMiddleName()
                Devuelve el segundo nombre.

        String = getNetworkUserID()
                Devuelve el ID de usuario de la red.

        String = getOffice()
                Devuelve la oficina.

        String = getOrganization()
                Devuelve la organización.

        String = getOrganizationUnit1()
                Devuelve la unidad organizativa 1.

        String = getOrganizationUnit2()
                Devuelve la unidad organizativa 1.

        String = getOrganizationUnit3()
                Devuelve la unidad organizativa 1.

        String = getOrganizationUnit4()
                Devuelve la unidad organizativa 1.

        String = getORName()
                Devuelve la representación en papel del nombre X.400 O/R, si existe.

        String = getPreferredAddressName()
                Devuelve la parte del nombre de campo de la dirección preferida.

        String = getPreferredAddressProductID()
                Devuelve la parte del ID del producto de la dirección preferida.

        String = getPreferredAddressTypeName()
                Devuelve el nombre del tipo de dirección de la dirección preferida.

        String = getPreferredAddressTypeValue()
                Devuelve el valor del tipo de dirección de la dirección preferida.

        String = getPreferredAddressValue()
                Devuelve el valor del campo de dirección preferida y el ID del producto.

        String = getPreferredName()
                Devuelve el nombre preferido.

        String = getPrivateManagementDomain()
                Devuelve el dominio de gestión privado.

        String = getSMTPDomain()
                Devuelve el dominio SMTP, si existe.

        String = getSMTPRoute()
                Devuelve la ruta SMTP, si existe.

        String = getSMTPUserID()
                Devuelve el ID de usuario de SMTP, si existe.

        String = getSurname()
                Devuelve el apellido.

        AS400 = getSystem()
                Devuelve el sistema.

        String = getSystemGroup()
                Devuelve el grupo del sistema de esta entrada de directorio.

        String = getSystemName()
                Devuelve el nombre del sistema de esta entrada de directorio.

        String = getTelephoneNumber1()
                Devuelve el primer número de teléfono.

        String = getTelephoneNumber2()
                Devuelve el segundo número de teléfono.

        String = getText()
                Devuelve el texto de esta entrada de directorio.

        String = getUserAddress()
                Devuelve la dirección de esta entrada de directorio.

        String = getUserDescription()
                Devuelve el campo de descripción de usuario para esta entrada de directorio.

        String = getUserID()
                Devuelve el ID de usuario de esta entrada de directorio.

        String = getUserProfile()
                Devuelve el nombre de perfil de usuario asociado con esta entrada.

        boolean = isIndirectUser()
                Indica si esta entrada representa un usuario indirecto.

        boolean = isLocal()
                Indica si esta entrada es una entrada local.

        boolean = isManager()
                Indica si esta entrada representa a un administrador.

        boolean = isMessageMailNotification()
                Indica un tipo de notificación de correo utilizado para esta entrada.

        boolean = isPrintCoverPage()
                Indica si se va a imprimir la portada.

        boolean = isPriorityMailNotification()
                Indica un tipo de notificación de correo utilizado para esta entrada.

        boolean = isSynchronized()
                Indica si esta entrada debe sincronizarse con directorios que no
                sean el directorio de distribución del sistema.

        """



        self.directoryentry = jpype.JClass('com.ibm.as400.access.DirectoryEntry')



