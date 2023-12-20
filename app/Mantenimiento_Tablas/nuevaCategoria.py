try:

    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion

except Exception as e:
    print(f'Falta algun modulo {e}')

api = ConfigurarAplicacion()

# Obtengo el conector a la base de datos
db = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_GX)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Lista de tablas a crear
lista_categorias = [

    'ACOPLADO',
    'AMBULANCIA',
    'ANTIGUO',
    'APLANADORA',
    'ARENERO',
    'AUTOELEVADORA',
    'BARREDORA',
    'BIPLAZA',
    'BLOCK',
    'BLOCK SEMI-ARMADO',
    'CAMION',
    'CAMION AUTOBOMBA',
    'CAMION GRUA',
    'CAMION HORMIGONERO',
    'CARGADORA',
    'CARRETON AUTOPROP.',
    'CASA RODANTE C/MOTOR',
    'CASA RODANTE S/MOTOR',
    'CHASIS C/CABINA',
    'CHASIS S/CABINA',
    'CICLOMOTOR',
    'COMPACTADORA',
    'CONVERTIBLE',
    'COSECHADORA',
    'COUPE',
    'CUATRICICLO',
    'CUATRICICLO C/DISP.',
    'CUATRICICLO C/DISP.ENG.',
    'DESCAPOTABLE',
    'ENFARDADORA',
    'EXCAVADORA',
    'FAMILIAR',
    'FERTILIZADORA',
    'FRESADORA',
    'FUMIGADORA',
    'FURGON',
    'FURGON CELULAR',
    'FURGONETA',
    'FURGONETA O UTILITARIO',
    'GRUA',
    'IRRIGADOR',
    'JEEP',
    'KARTING',
    'LIMOUSINE',
    'LOCOTRACTOR',
    'MINIBUS',
    'MONOPLAZA',
    'MOTOCICLETA',
    'MOTOCULTOR',
    'MOTONIVELADORA',
    'MOTOR',
    'NO INFORMADO',
    'OMNIBUS',
    'OTROS AUTOMOTORES',
    'OTROS AUTOMOTORES DE CARGA',
    'PAVIMENTADORA',
    'PERFORADORA',
    'PICADORA',
    'PICK-UP',
    'PICK-UP CABINA DOBLE',
    'PICK-UP CABINA SIMPLE',
    'PICK-UP CABINA Y MEDIA',
    'PULVERIZADORA',
    'RECUPERADORA ASFALTICA',
    'REMOLQUE',
    'RURAL 3 PUERTAS',
    'RURAL 4 PUERTAS',
    'RURAL 4/5 PUERTAS',
    'RURAL 5 PUERTAS',
    'SCOOTER',
    'SEDAN 2 PUERTAS',
    'SEDAN 3 PUERTAS',
    'SEDAN 4 PUERTAS',
    'SEDAN 5 PUERTAS',
    'SEGADORA',
    'SEMI-ACOPLADO',
    'SEMIRREMOLQUE',
    'SEÑALIZADORA ASFALTICA',
    'SIN ESPECIFICACION',
    'TALADOR',
    'TEXTURADOR/CURADO DE HORMIGON',
    'TODO TERRENO',
    'TOPADORA',
    'TRACTOR',
    'TRACTOR DE CARRETERA',
    'TRACTOR TRANSPORTADOR',
    'TRAILLA',
    'TRANSPORTE DE PASAJEROS',
    'TRICICLO',
    'TRICICLO DE CARGA',
    'UNIDAD DE TRACTOR-SEMIRREMOLQ.',
    'UTILITARIO',
    'UTILITARIO ELECTRICO',
    'VOLQUETE',
    'ZANJADORA',
    'TRACTOR C/CABINA DORMITORIO',
    'TRACTOR S/CABINA DORMITORIO',
    'TRITURADORA',
    'CHASIS C/CABINA DORMITORIO',
    'CARRETILLA GRUA',
    'CARGADORA RETROEXCAVADORA',
    'TRACTOR TERMINAL PORTUARIA',
    'PROCESADOR FORESTAL DE TRONCOS',
    'RECICLADORA',
    'PISA NIEVE',
    'CAMION C/CABINA DORMITORIO',
    'PERFILADORA DE CONCRETO',
    'MIDIBUS',
    'DESPAJONADORA',
    'PALA MECANICA',
    'CARRETON',
    'PILOTERA',
    'CAMION CISTERNA',
    'CAMION (S/E)',
    'TRAILER (S/E)',
    'UNIDAD DE BOMBEROS',
    'VEHICULO DE USO TACTICO',
    'CORTADORA DE ROCA',
    'TIENDE TUBOS',
    'ARRASTRA TRONCOS',
    'CARGADORA DE TRONCOS',
    'CUADRICICLO LIVIANO L6(B)',
    'CUADRICICLO PESADO PASAJ-L7B',

]


for nombre in lista_categorias:

    campos = dict()
    campos = {'desccategoria': nombre}

    retorno = db.add_Dal(db.__getattribute__(api.LISTA_TABLAS['TABLA_CATEGORIA']['objeto']), **campos)

    if not retorno:
        print(retorno)
