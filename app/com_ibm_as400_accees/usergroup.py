# -------Lista de lisbrerias y Modulos
try:
        import jpype
        import os
        from com_ibm_as400_accees.user import User

except Exception as e:
    print(f'Falta algun modulo {e}')


class UserGroup(User):

    # Constructor
    def __init__(self):

        """
        Enumeration = getMembers()
            Devuelve un lista de usuarios de los miembreos del  grupo

        """

        self.usergroup = jpype.JClass('com.ibm.as400.access.UserGroup')
        User.__init__(self)

