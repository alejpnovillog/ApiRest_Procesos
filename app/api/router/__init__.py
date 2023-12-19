# api/routes/__init__.py
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
try:

    # importamos la libreria que maneja el sistema operativo
    import os

    # modulo para poder agrupar los scripts 
    from importlib import import_module

    # importamos la clase apirouter
    from fastapi import APIRouter

except Exception as e:
    print(f'Falta algun modulo en main --> {e}')

# asignamos una instancia de la clase
router = APIRouter()

# Lista todos los archivos en el directorio actual
files = os.listdir(os.path.dirname(__file__))

# Filtra los archivos que terminan con .py y no son __init__.py
# se incorpora a la lista el nombre del modulo sacandole los ultimos caracteres
modules = [filename[:-3] for filename in files if filename.endswith(".py") and filename != "__init__.py"]

# Importa y agrega cada router automáticamente
for module_name in modules:
    
    # se asigna a la variable el nombre del modulo definido como paquete
    # __package__ es la key para definir como modulo name sea definido como paquete
    module = import_module(f".{module_name}", package=__package__)
    
    # se include el modulo al router con el prefijo definido y asignandole un 
    # tags en el nombre del modulo
    router.include_router(module.router, prefix=f"/kuvasz", tags=[module_name])











