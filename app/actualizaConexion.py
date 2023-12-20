# ------------------LIBRERIA PARA OBTENER LOS DATOS DE CONEXION
from app_Config.configurarConexion import ConfigHost

#con = ConfigHost(host='Automotor_Prod',  accion='add', serverhost='sqlite3', databasehost='Automotor')
con = ConfigHost()

"""

con.host = 'IseriesGxProd_postgres'
con.serverhost = 'postgres'
con.iphost = 'localhost'
con.usuariohost = 'postgres'
con.passhost = 'macs6259'
con.schemahost = None
con.databasehost = 'Kuvasz'
con.accion = 'add'
con.add_host()


con.host = 'Pub400'
con.serverhost = 'db2'
con.iphost = 'PUB400.COM'
con.usuariohost = 'anovillo'
con.passhost = 'macs6259'
con.schemahost = 'anovillo1'
con.databasehost = 'PUB400'
con.accion = 'add'
con.add_host()



con.chg_host()
con.accion = 'list'
con.host = '*all'
con.accion = 'list'
con.list_host()


con.host = 'IseriesGxProd_postgres'
con.accion = 'chg'
con.schemahost = 'public'
con.chg_host()
"""
con.host = '*all'
con.accion = 'list'
con.list_host()












