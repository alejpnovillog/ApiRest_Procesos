# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os

        from com_ibm_as400_accees.objectLockListEntry import ObjectLockListEntry

except Exception as e:
    print(f'Falta algun modulo {e}')


class ObjectDescription():

    # Atributos de la clase
    ALLOW_CHANGE_BY_PROGRAM = 308
    APAR = 413
    ASP_NAME_ALL =  "*"
    ASP_NAME_ALLAVL = "*ALLAVL"
    ASP_NAME_CURASPGRP = "*CURASPGRP"
    ASP_NAME_SYSBAS = "*SYSBAS"
    ASP_NAME_UNKNOWN = "*N"
    ASP_SEARCH_TYPE_ASP = "*ASP"
    ASP_SEARCH_TYPE_ASPGRP = "*ASPGRP"
    AUDITING = 310
    AUDITING_ALL = "*ALL"
    AUDITING_CHANGE = "*CHANGE"
    AUDITING_NONE = "*NONE"
    AUDITING_USER_PROFILE = "*USRPRF"
    CHANGE_DATE = 305
    CHANGED_BY_PROGRAM = 309
    COMPILER = 408
    COMPRESSION = 307
    COMPRESSION_INELIGIBLE = "X"
    COMPRESSION_NO = "N"
    COMPRESSION_STORAGE_FREED = "F"
    COMPRESSION_TEMPORARY = "T"
    COMPRESSION_YES = "Y"
    CREATION_DATE = 304
    CREATOR_SYSTEM = 406
    CREATOR_USER_PROFILE = 405
    CURRENT_LIBRARY = "*CURLIB"
    DAYS_USED = 603
    DIGITALLY_SIGNED = 311
    DIGITALLY_SIGNED_MULTIPLE = 313
    DIGITALLY_SIGNED_TRUSTED = 312
    DOMAIN = 303
    DOMAIN_SYSTEM = "*S"
    DOMAIN_USER = "*U"
    EXTENDED_ATTRIBUTE = 202
    JOURNAL = 514
    JOURNAL_IMAGES = 516
    JOURNAL_OMITTED_ENTRIES = 517
    JOURNAL_START_DATE = 518
    JOURNAL_STATUS = 513
    LAST_USED_DATE = 601
    LIBRARY = 10001
    LIBRARY_ASP_DEVICE_NAME = 606
    LIBRARY_ASP_NUMBER = 314
    LIBRARY_LIST = "*LIBL"
    LICENSED_PROGRAM = 411
    NAME = 10000
    OBJECT_ASP_DEVICE_NAME = 605
    OBJECT_ASP_NUMBER = 301
    OBJECT_LEVEL = 409
    OBJECT_SIZE = 701
    ORDER_IN_LIBRARY_LIST = 205
    OVERFLOWED_ASP = 703
    OWNER = 302
    PRIMARY_GROUP = 414
    PRIMARY_GROUP_NONE = "*NONE"
    PTF = 412
    RESET_DATE = 602
    RESTORE_DATE = 502
    SAVE_ACTIVE_DATE = 512
    SAVE_COMMAND = 506
    SAVE_DATE = 501
    SAVE_DEVICE = 508
    SAVE_DEVICE_DISKETTE = "*DKT"
    SAVE_DEVICE_NOT_SAVED = ""
    SAVE_DEVICE_OPTICAL = "*OPT"
    SAVE_DEVICE_SAVE_FILE = "*SAVF"
    SAVE_DEVICE_TAPE = "*TAP"
    SAVE_FILE = 509
    SAVE_LABEL = 511
    SAVE_SEQUENCE_NUMBER = 505
    SAVE_SIZE = 503
    SAVE_VOLUME_ID = 507
    SOURCE_FILE = 401
    SOURCE_FILE_UPDATED_DATE = 404
    STATUS_DAMAGED  = - 60
    STATUS_LOCKED  = - 45
    STATUS_NO_AUTHORITY = - 63
    STATUS_NO_ERRORS = 64
    STATUS_PARTIALLY_DAMAGED = 41
    STATUS_UNKNOWN = 0
    STORAGE_STATUS = 306
    STORAGE_STATUS_FREE = "*FREE"
    STORAGE_STATUS_KEEP = "*KEEP"
    SYSTEM_LEVEL = 407
    SYSTEM_OR_BASIC_ASP = "*SYSBAS"
    TEXT_DESCRIPTION = 203
    TYPE = 10002
    USAGE_INFO_UPDATED = 604
    USER_CHANGED = 410
    USER_DEFINED_ATTRIBUTE = 204


    # Constructor
    def __init__(self, system, qsysobjpathname):


        """
        parametros:
            system = Es la conexion a la Iseries
            qsysobjpathname = Es el string con el path del objeto

        Metodos:
        
                boolean =  equals( obj)
                    Indica si algún otro objeto es "igual a" este.
                
                boolean =	exists()
                    Comprueba si este objeto existe actualmente en el sistema.
                
                String = getAspDeviceName()
                    Devuelve el nombre de un dispositivo de grupo de almacenamiento auxiliar (ASP) 
                    en el que se asigna almacenamiento para la biblioteca que contiene el objeto.
                
                String = getAspSearchType()
                    Devuelve el tipo de búsqueda que se utilizará cuando se especifica un 
                    nombre de dispositivo de grupo de almacenamiento auxiliar específico.
                
                String = getLibrary()
                    Devuelve la biblioteca de este objeto.
                
                String = getName()
                    Devuelve el nombre de este objeto.
                    
                ObjectLockListEntry = 	getObjectLockList()
                    Devuelve una lista de todos los objetos ObjectLockListEntry que representan 
                    posibles bloqueos de objetos en esta ObjectDescription.
                    
                String = getPath()
                    Devuelve el nombre de vía de acceso completo del sistema de 
                    archivos integrado de este objeto.
                    
                byte = getStatus()
                    Devuelve el estado de la información devuelta en este objeto 
                    si fue generada por un ObjectList.
                    
                String = getType()
                    Devuelve el tipo de este objeto.
                    
                objeto = getValue(int attribute)
                    Devuelve el valor del atributo dado de este ObjectDescription.
                    
                String = getValueAsString(int attribute)
                    Devuelve el valor del atributo dado de este ObjectDescription, como una cadena.
                    
                integer = hashCode()
                    Devuelve un valor de código hash para el objeto.
                    
                refresh()
                    Recupera todos los atributos posibles de este objeto del sistema.
                    
                String = toString()
                    Devuelve una representación de cadena de este ObjectDescription.
        
        """
        self.objeto = jpype.JClass('com.ibm.as400.access.ObjectDescription')

