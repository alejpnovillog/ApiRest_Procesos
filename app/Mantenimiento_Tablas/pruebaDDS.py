try:

    import pyodbc
    from pydal.adapters.db2 import DB2Pyodbc
    from pydal import DAL
    from pydal import Field
except Exception as e:
    print(f'Falta algun modulo {e}')

c2 = 'db2:pyodbc://driver={iSeries Access ODBC Driver}; system=172.16.5.19; uid=gxusr; pwd=genexus; dbq=Epagos'
db = DAL(c2, pool_size=10, db_codec='UTF-8')
lista = list()
primary = list()



lista = [
    Field('INFVE00003', type='integer'),
    Field('TIPOC00001', type='integer'),
    Field('TIPOS00001', type='integer'),
    Field('TIPOD00001', type='integer'),
    Field('NUMER00001', type='integer'),
    Field('CUITC00001', type='integer'),
    Field('APELL00001', type='string', length=150),
    Field('PORCE00001', type='integer'),
    Field('CALLE00001', type='string', length=40),
    Field('NUMER00002', type='string', length=10),
    Field('PISO_00001', type='string', length=10),
    Field('DEPAR00001', type='string', length=10),
    Field('BARRI00001', type='string', length=40),
    Field('LOCAL00001', type='string', length=40),
    Field('CODIG00001', type='string', length=8),
    Field('PROVI00001', type='integer'),
    Field('RESER00001', type='string', length=256),
    Field('INFVE00002', type='integer'),
    Field('KTIME00001', type='detetime')

]

primary = ['INFVE00003']

parm = {
    'name': 'INFOR00002',
    'fields': tuple(lista), 'arg': {'primarykey': primary,
                                    'migrate': False}
}


# ----- JSON LOG TEMP
tmpinformacionVehiculoTitular_Dal = db.define_table(parm['name'], *parm['fields'], **parm['arg'])



"""
Field('INFVE00003', type='integer'),
Field('TIPOC00001', type='integer'),
Field('TIPOS00001', type='integer'),
Field('TIPOD00001', type='integer'),
Field('NUMER00001', type='integer'),
Field('CUITC00001', type='integer'),
Field('APELL00001', type='string', length=150),
Field('PORCE00001', type='integer'),
Field('CALLE00001', type='string', length=40),
Field('NUMER00002', type='string', length=10),
Field('PISO_00001', type='string', length=10),
Field('DEPAR00001', type='string', length=10),
Field('BARRI00001', type='string', length=40),
Field('LOCAL00001', type='string', length=40),  
Field('CODIG00001', type='string', length=8),  
Field('PROVI00001', type='integer'),  
Field('RESER00001', type='string', length=256),  
Field('INFVE00002', type='integer'),
Field('KTIME00001', type='detetime')
                                                primarykey = ['INFVE00001'],
                                                migrate = False
                                            )
"""
print(tmpinformacionVehiculoTitular_Dal)
print('hola')

