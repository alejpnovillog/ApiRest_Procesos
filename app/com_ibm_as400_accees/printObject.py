# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os

except Exception as e:
    print(f'Falta algun modulo {e}')

# Es la definicion de una clase abstracta
class PrintObject():


    ATTR_3812SCS = 287
    ATTR_ACCOUNT_CODE	 = 265
    ATTR_AFP = 10
    ATTR_AFP_RESOURCE = -12
    ATTR_AFPRESOURCE	 = 282
    ATTR_ALIGN = 11
    ATTR_ALIGNFORMS = 190
    ATTR_ALWDRTPRT = 12
    ATTR_ASCIITRANS	 = 296
    ATTR_ASPDEVICE = 266
    ATTR_AUTHCHCK = 14
    ATTR_AUTHORITY	 = 13
    ATTR_AUTOEND = 16
    ATTR_AUX_POOL = 252
    ATTR_BACK_OVERLAY = -1
    ATTR_BARCODE	 = 283
    ATTR_BKMGN_ACR = 17
    ATTR_BKMGN_DWN = 18
    ATTR_BKOVL_ACR = 22
    ATTR_BKOVL_DWN	 = 21
    ATTR_BTWNCPYSTS = 206
    ATTR_BTWNFILESTS = 207
    ATTR_CHANGES = 191
    ATTR_CHAR_ID = 55
    ATTR_CHARID = 300
    ATTR_CHR_RTT_CMDS = 316
    ATTR_CHRSET = 308
    ATTR_CHRSET_LIB = 307
    ATTR_CHRSET_SIZE = 312
    ATTR_CODEDFNT = 26
    ATTR_CODEDFNTLIB = 24
    ATTR_CODEDFONT_SIZE	 = 281
    ATTR_CODEPAGE = 25
    ATTR_CODEPAGE_NAME = 280
    ATTR_CODEPAGE_NAME_LIB = 279
    ATTR_CODFNT_ARRAY = 306
    ATTR_COLOR = 284
    ATTR_CONSTBCK_OVL = 270
    ATTR_CONTROLCHAR = 196
    ATTR_CONVERT_LINEDATA = 247
    ATTR_COPIES = 28
    ATTR_COPIESLEFT = 29
    ATTR_CORNER_STAPLE = 248
    ATTR_CPI = 23
    ATTR_CPI_CHANGES = 301
    ATTR_CURPAGE = 30
    ATTR_DATA_QUEUE = -2
    ATTR_DATAFORMAT = 31
    ATTR_DATE = 34
    ATTR_DATE_END = 253
    ATTR_DATE_USED = 269
    ATTR_DATE_WTR_BEGAN_FILE = 234
    ATTR_DATE_WTR_CMPL_FILE = 235
    ATTR_DAYS_UNTIL_EXPIRE	 = 320
    ATTR_DBCS_FNT = 275
    ATTR_DBCS_FNT_LIB = 274
    ATTR_DBCS_FNT_SIZE = 276
    ATTR_DBCSCPI = 156
    ATTR_DBCSDATA = 153
    ATTR_DBCSEXTENSN = 154
    ATTR_DBCSROTATE = 155
    ATTR_DBCSSISO = 157
    ATTR_DDS = 285
    ATTR_DECIMAL_FMT = 268
    ATTR_DELETESPLF = 151
    ATTR_DESCRIPTION = 109
    ATTR_DESTINATION = 37
    ATTR_DESTOPTION = 152
    ATTR_DEVCLASS = 38
    ATTR_DEVMODEL = 	39
    ATTR_DEVSTATUS = 199
    ATTR_DEVTYPE = 40
    ATTR_DFR_WRITE = 35
    ATTR_DISPLAYANY = 41
    ATTR_DOUBLEWIDE = 286
    ATTR_DRAWERCHANGE = 302
    ATTR_DRWRSEP = 42
    ATTR_DUPLEX = 85
    ATTR_EDGESTITCH_NUMSTAPLES = 240
    ATTR_EDGESTITCH_REF = 238
    ATTR_EDGESTITCH_REFOFF = 239
    ATTR_ENDPAGE = 43
    ATTR_ENDPNDSTS = 204
    ATTR_ENVLP_SOURCE = 211
    ATTR_EXPIRATION_DATE = 321
    ATTR_FIDELITY = 	84
    ATTR_FIELD_OUTLIN = 288
    ATTR_FILESEP = 44
    ATTR_FOLDREC = 45
    ATTR_FONT_CHANGES = 	303
    ATTR_FONTID = 46
    ATTR_FONTRESFMT = 267
    ATTR_FORM_DEFINITION = -3
    ATTR_FORMFEED = 47
    ATTR_FORMTYPE = 48
    ATTR_FORMTYPEMSG = 67
    ATTR_FRONT_OVERLAY = -4
    ATTR_FTMGN_ACR = 49
    ATTR_FTMGN_DWN = 	50
    ATTR_FTOVL_ACR = 54
    ATTR_FTOVL_DWN = 53
    ATTR_GRAPHICS = 289
    ATTR_GRAPHICS_TOK = 290
    ATTR_GRPLVL_IDXTAG = 	291
    ATTR_HELDSTS = 	208
    ATTR_HIGHLIGHT =292
    ATTR_HOLD = 57
    ATTR_HOLDPNDSTS =209
    ATTR_HOLDTYPE = 158
    ATTR_IMGCFG = 256
    ATTR_INTERNETADDR = 148
    ATTR_IPDSPASSTHRU = 278
    ATTR_IPP_ATTR_CCSID = 225
    ATTR_IPP_ATTR_NL = 250
    ATTR_IPP_JOB_ID = 228
    ATTR_IPP_JOB_NAME = 230
    ATTR_IPP_JOB_NAME_NL = 231
    ATTR_IPP_JOB_ORIGUSER = 232
    ATTR_IPP_JOB_ORIGUSER_NL = 233
    ATTR_IPP_PRINTER_NAME = 229
    ATTR_JOBCCSID = 334
    ATTR_JOBNAME = 59
    ATTR_JOBNUMBER = 60
    ATTR_JOBSEPRATR = 61
    ATTR_JOBSYSTEM = 251
    ATTR_JOBUSER = 62
    ATTR_JUSTIFY = 56
    ATTR_LASTPAGE = 63
    ATTR_LIBRARY = 15
    ATTR_LINESPACING = 195
    ATTR_LPI = 64
    ATTR_LPI_CHANGES = 304
    ATTR_MAX_JOBS_PER_CLIENT = 222
    ATTR_MAXRCDS = 66
    ATTR_MEASMETHOD = 79
    ATTR_MESSAGE_QUEUE = -5
    ATTR_MFGTYPE = 65
    ATTR_MSGHELP = 129
    ATTR_MSGID = 147
    ATTR_MSGREPLY = 130
    ATTR_MSGSEV = 159
    ATTR_MSGTEXT = 128
    ATTR_MSGTYPE = 142
    ATTR_MULTI_ITEM_REPLY = 220
    ATTR_MULTIUP = 82
    ATTR_NETWORK = 189
    ATTR_NPSCCSID = 138
    ATTR_NPSLEVEL = 141
    ATTR_NUMBYTES = 125
    ATTR_NUMBYTES_SPLF = 217
    ATTR_NUMFILES = 69
    ATTR_NUMRSC_LIB_ENT = 313
    ATTR_NUMWRITERS = 145
    ATTR_OBJEXTATTR = 177
    ATTR_OFFICEVISION = 293
    ATTR_ONJOBQSTS = 205
    ATTR_OPCNTRL = 70
    ATTR_OPENCMDS = 160
    ATTR_ORDER = 71
    ATTR_OS4_CRT_AFP = 309
    ATTR_OUTPTY = 72
    ATTR_OUTPUT_QUEUE = -6
    ATTR_OUTPUTBIN = 192
    ATTR_OUTQSTS = 75
    ATTR_OVERALLSTS = 200
    ATTR_OVERFLOW = 76
    ATTR_PAGE_AT_A_TIME = 214
    ATTR_PAGE_DEFINITION = -13
    ATTR_PAGE_GROUPS = 294
    ATTR_PAGE_ROTATE = 298
    ATTR_PAGELEN = 78
    ATTR_PAGELVLIDXTAG = 295
    ATTR_PAGENUMBER = 215
    ATTR_PAGES = 111
    ATTR_PAGES_EST = 218
    ATTR_PAGEWIDTH = 81
    ATTR_PAGRTT = 36
    ATTR_PAPER_SOURCE_1 = 212
    ATTR_PAPER_SOURCE_2 = 213
    ATTR_PELDENSITY = 178
    ATTR_PGM_OPN_FILE =	272
    ATTR_PGM_OPN_LIB = 271
    ATTR_POINTSIZE = 83
    ATTR_PRINTER = 89
    ATTR_PRINTER_FILE = -7
    ATTR_PRTASSIGNED = 186
    ATTR_PRTDEVTYPE = 90
    ATTR_PRTQUALITY = 86
    ATTR_PRTSEQUENCE = 87
    ATTR_PRTTEXT = 88
    ATTR_PUBINF = 335
    ATTR_PUBINF_COLOR_SUP = 257
    ATTR_PUBINF_DS = 262
    ATTR_PUBINF_DUPLEX_SUP = 260
    ATTR_PUBINF_LOCATION	 = 261
    ATTR_PUBINF_PPM = 259
    ATTR_PUBINF_PPM_COLOR = 258
    ATTR_RCDFMT_DATA = 297
    ATTR_RECLENGTH = 95
    ATTR_REDUCE = 194
    ATTR_RESTART = 99
    ATTR_RMTLOCNAME = 255
    ATTR_RMTPRTQ = 93
    ATTR_RMTSYSTEM = 96
    ATTR_RPLCHAR = 98
    ATTR_RPLUNPRT = 97
    ATTR_RSC_LIB_LIST = 249
    ATTR_SADDLESTITCH_NUMSTAPLES = 243
    ATTR_SADDLESTITCH_REF = 242
    ATTR_SADDLESTITCH_STPL_OFFSEINFO = 244
    ATTR_SAVE = 100
    ATTR_SAVE_COMMAND = 322
    ATTR_SAVE_DEVICE = 323
    ATTR_SAVE_FILE = -14
    ATTR_SAVE_LABEL = 326
    ATTR_SAVE_SEQUENCE_NUMBER = 327
    ATTR_SAVE_VOLUME_FORMAT = 328
    ATTR_SAVE_VOLUME_ID =329
    ATTR_SCHEDULE = 107
    ATTR_SCS2ASCII = 113
    ATTR_SEEKOFF = 126
    ATTR_SEEKORG = 127
    ATTR_SENDPTY =	101
    ATTR_SEPPAGE	 = 161
    ATTR_SPLF_AUTH_METHOD = 227
    ATTR_SPLF_CREATOR = 314
    ATTR_SPLF_RESTORED_DATE = 330
    ATTR_SPLF_RESTORED_TIME	 = 331
    ATTR_SPLF_SAVED_DATE = 332
    ATTR_SPLF_SAVED_TIME = 333
    ATTR_SPLF_SECURITY_METHOD = 226
    ATTR_SPLF_SIZE = 310
    ATTR_SPLF_SIZE_MULT = 311
    ATTR_SPLFNUM = 105
    ATTR_SPLFSTATUS = 106
    ATTR_SPLSCS = 173
    ATTR_SPOOL = 103
    ATTR_SPOOLFILE = 104
    ATTR_SRC_CODEPAGE = 	263
    ATTR_SRCDRWR = 102
    ATTR_STARTEDBY = 197
    ATTR_STARTPAGE = 108
    ATTR_SYS_DRV_PGM = 305
    ATTR_SYSTEM = 188
    ATTR_TGT_CODEPAGE = 264
    ATTR_TIME = 110
    ATTR_TIME_END = 254
    ATTR_TIME_WTR_BEGAN_FILE = 236
    ATTR_TIME_WTR_CMPL_FILE = 237
    ATTR_TOADDRESS = 118
    ATTR_TOUSERID = 117
    ATTR_TRC1403 = 299
    ATTR_UNITOFMEAS = 114
    ATTR_USER_DEFINED_OBJECT = -9
    ATTR_USER_DFN_TXT = 277
    ATTR_USER_DRIVER_PROG = -11
    ATTR_USER_TRANSFORM_PROG = -10
    ATTR_USERCMT = 115
    ATTR_USERDATA = 116
    ATTR_USERGEN_DATA = 273
    ATTR_USRDEFDATA	 = 162
    ATTR_USRDEFFILE = 198
    ATTR_USRDEFOPT = 163
    ATTR_USRDRVDATA = 169
    ATTR_VIEWING_FIDELITY = 216
    ATTR_VMMVSCLASS = 119
    ATTR_WORKSTATION_CUST_OBJECT = -8
    ATTR_WRTNGSTS	 = 187
    ATTR_WTNGDATASTS = 203
    ATTR_WTNGDEVSTS	 = 201
    ATTR_WTNGMSGSTS = 202
    ATTR_WTRAUTOEND = 120
    ATTR_WTREND	 = 144
    ATTR_WTRINIT = 	172
    ATTR_WTRJOBNAME = 121
    ATTR_WTRJOBNUM = 122
    ATTR_WTRJOBSTS = 123
    ATTR_WTRJOBUSER = 124
    ATTR_WTRSTRPAGE = 143
    ATTR_WTRSTRTD = 193
    


    def __init__(self):

        """

        """
        self.printobject = jpype.JClass('com.ibm.as400.access.PrintObject')



    # ***
    # Adds the specified PropertyChange listener to receive PropertyChange events from this print object.
    def addPRNOBJPropertyChangeListener(self, oyente):

        """
            Adds the specified PropertyChange listener to receive PropertyChange events from this print object.
            void	addPropertyChangeListener(java.beans.PropertyChangeListener listener)

            param:
                java.beans.PropertyChangeListener listener

        """
        self.printobject.addPropertyChangeListener(oyente)



    # ***
    # Adds the specified VetoableChange listener to receive VetoableChange events from this print object.
    def addPRNOBJVetoableChangeListener(self, oyente):

        """
            Adds the specified VetoableChange listener to receive VetoableChange events from this print object.
            void	addVetoableChangeListener(java.beans.VetoableChangeListener listener)

            param:
                java.beans.VetoableChangeListener listener

        """
        self.printobject.addVetoableChangeListener(oyente)


    # ***
    # Returns an attribute of the object that is a Float type attribute.
    def getPRNOBJFloatAttribute(self, atributoid):

        """
            Returns an attribute of the object that is a Float type attribute.
             java.lang.Float = getFloatAttribute(int attributeID)

             param:
                int attributeID

        """
        return self.printobject.getFloatAttribute(atributoid)



    # ***
    # Returns an attribute of the object that is a Integer type attribute.
    def getPRNOBJIntegerAttribute(self, atributoid):

        """
            Returns an attribute of the object that is a Integer type attribute.
            java.lang.Integer = getIntegerAttribute(int attributeID)

            param:
                int attributeID

        """
        return self.printobject.getIntegerAttribute(atributoid)


    # ***
    # Returns an attribute of the object that is a Float type attribute.
    def getPRNOBJSingleFloatAttribute(self, atributoid):

        """
            Returns an attribute of the object that is a Float type attribute.
            java.lang.Float	getSingleFloatAttribute(int attributeID)

            param:
                int attributeID

        """
        return self.printobject.getSingleFloatAttribute(atributoid)


    # ***
    # Returns an attribute of the object that is a Integer type attribute.
    def getPRNOBJSingleIntegerAttribute(self, atributoid):

        """
            Returns an attribute of the object that is a Integer type attribute.
            java.lang.Integer = getSingleIntegerAttribute(int attributeID)

            param:
                int attributeID

        """
        return self.printobject.getSingleIntegerAttribute(atributoid)


    # ***
    # Returns an attribute of the object that is a String type attribute.
    def getPRNOBJSingleStringAttribute(self, atributoid):

        """
            Returns an attribute of the object that is a String type attribute.
            java.lang.String	getSingleStringAttribute(int attributeID)

            param:
                int attributeID

        """
        return self.printobject.getSingleStringAttribute(atributoid)


    # ***
    # Returns an attribute of the object that is a String type attribute.
    def getPRNOBJStringAttribute(self, atributoid):

        """
            Returns an attribute of the object that is a String type attribute.
            java.lang.String = getStringAttribute(int attributeID)

            param:
                int attributeID

        """
        return self.printobject.getStringAttribute(atributoid)


    # ***
    # Returns the system on which this object exists.
    def getPRNOBJSystem(self):

        """
            Returns the system on which this object exists.
            AS400 = getSystem()

        """
        return self.printobject.getSystem()


    #  ***
    # Removes the specified PropertyChange listener so that
    # it no longer receives PropertyChange events from this print object.
    def removePRNOBJPropertyChangeListener(self, oyente):

        """
            Removes the specified PropertyChange listener so that
            it no longer receives PropertyChange events from this print object.

            void	removePropertyChangeListener(java.beans.PropertyChangeListener listener)

            param:
                java.beans.PropertyChangeListener listener

        """
        self.printobject.removePropertyChangeListener(oyente)



    # ***
    # Removes the specified VetoableChange listener so that it no longer
    # receives VetoableChange events from this print object.
    def removePRNOBJVetoableChangeListener(self, oyenete):

        """
            Removes the specified VetoableChange listener so that it no longer
            receives VetoableChange events from this print object.

            void	removeVetoableChangeListener(java.beans.VetoableChangeListener listener)

            param:
                java.beans.VetoableChangeListener listener

        """
        self.printobject.removeVetoableChangeListener(oyenete)


    # ***
    # Sets the system on which this object exists.
    def setPRNOBJSystem(self, sistema):

        """
            Sets the system on which this object exists.
            void	setSystem(AS400 system)

            param:
                sistema

        """
        self.printobject.setSystem(sistema)


    # ***
    # Updates the attributes of this object by going to the system and
    # retrieving the latest attributes for the object.
    def updatePRNOBJ(self):

        """
            Updates the attributes of this object by going to the system and
            retrieving the latest attributes for the object.

        """
        self.printobject.update()
