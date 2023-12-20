# Load las bibliotecas necesarias
try:
    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion
    from app_Conexion_Iseries_JtOpen.pythonJTOpen import JT400
    from com_ibm_as400_accees.objectDescription import  ObjectDescription
    #from com_ibm_as400_accees.objectList import ObjectList
    import os
    import datetime
    import unidecode
    import jpype

except Exception as e:
    print(f'Falta algun modulo {e}')



# definimos la conexion de datos solo para tablas SQL----------------------
data_Input = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_GX)

# obtenemos la estructura de conexion
con = data_Input.__getattribute__('instancia_Host_Input_Dict')



# definimos la conexion de la iseries para jecutar comandos
iprod = JT400(con['ip'], con['usuario'], con['password'])



print(f' Obtenemos la Version del OS400 = {iprod.getvrm()}')
print(f' Obtenemos la autenticacion del schema = {iprod.getauthenticationscheme()}')
print(f' Obtenemos el codigo CCSID del usuario = {iprod.getccsid()}')
print(f' Obtenemos el nombre de la base de datos en una conexion DDM = {iprod.getddmrdb()}')
print(f' Obtenemos el default time zone del Iseries = {iprod.getdefaulttimezone()}')
print(f' Obtenemos el ID del user de la Iseries = {iprod.getuserid()}')
print(f' Obtenemos la Version del OS Iseries = {iprod.getversion()}')
print(f' Obtenemos le Nombre del Sistema = {iprod.getsystemname()}')
print(f' Obtenemos el  port del servicio FILE del Sistema = {iprod.getserviceport(0)}')
print(f' Obtenemos el  port del servicio PRINT del Sistema = {iprod.getserviceport(1)}')
print(f' Obtenemos el  port del servicio COMMAND del Sistema = {iprod.getserviceport(2)}')
print(f' Obtenemos el  port del servicio DATAQUEUE del Sistema = {iprod.getserviceport(3)}')
print(f' Obtenemos el  port del servicio DATABASE del Sistema = {iprod.getserviceport(4)}')
print(f' Obtenemos el  port del servicio RECORDACCESS del Sistema = {iprod.getserviceport(5)}')
print(f' Obtenemos el  port del servicio CENTRAL del Sistema = {iprod.getserviceport(6)}')
print(f' Obtenemos el  port del servicio SIGNON del Sistema = {iprod.getserviceport(7)}')
print(f' Obtenemos el  Release del sistema OS 400 = {iprod.getrelease()}')
print(f' Obtenemos el  Proxy Server = {iprod.getproxyserver()}')
print(f' Obtenemos la cantidad de dias que faltan para que expire la password del usuario Warning = {iprod.getpasswordexpirationwarningdays()}')
print(f' Obtenemos la cantidad de dias que faltan para que expire la password del usuario = {iprod.getpasswordexpirationdays()}')
print(f' Obtenemos el Usuario por Default = {iprod.getdefaultuser()}')
print(f' Obtenemos el Nombre del GSS = {iprod.getgssname()}')
print(f' Obtenemos la Opcion del GSS = {iprod.getgssoption()}')
listaJob =  iprod.getjobs(iprod.iseries.COMMAND)
print(f' Obtenemos los job de un servicio = {listaJob}')

for job in listaJob:

    print(job.getName())
    print(f'Obtenemos el Job Accounting Code = {job.getJobAccountingCode()} ')
    print(job.getAuxiliaryIORequests())
    print(job.getJobActiveDate())






print('hola')




