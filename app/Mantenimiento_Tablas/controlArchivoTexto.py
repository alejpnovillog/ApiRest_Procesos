try:
    import os

except Exception as e:
    print(f'Falta algun modulo {e}')

# Establecemos la ruta donde esta el archivo
ruta = os.getcwd()
ruta = os.getcwd() + "\\Archivos_SinProcesar\\MigracionVehiculos"
os.chdir(ruta)

# Establecemos el archivo de texto
archivo_texto = "2481cfcc14ab493c51b9a4d02567bac1FIJO.txt"
total = 0
totalC = 0
totalT = 0
lectura = True
controlLogRecord = False

try:
    # Open el archivo archivo de texto
    with open(archivo_texto, mode='r', encoding='latin-1') as archivo:

        for linea in archivo:

            total += 1

            if linea[0:2] == 'E0':
                if len(linea) != 45:
                    controlLogRecord = True
                    print(f'Error registro {total} la longitud el tipo E0 DEBE SER 45. La longitud es {len(linea)}')

            if linea[0:2] == 'C5':
                if linea[2:3] == 'C':
                    if len(linea) != 860:
                        controlLogRecord = True
                        print(f'Error registro {total} la longitud el tipo C DEBE SER 860. La longitud es {len(linea)}')
                if linea[2:3] == 'T':
                    if len(linea) != 597:
                        print(f'Error registro {total} la longitud el tipo T DEBE SER 597. La longitud es {len(linea)}')

            if linea[0:2] == 'P0':
                if len(linea) != 42:
                    controlLogRecord = True
                    print(f'Error registro {total} la longitud el tipo P0 DEBE SER 42. La longitud es {len(linea)}')




    # proceso completado
    print(f'proceso completado....total C = {totalC}    total T = {totalT} total leidos {total}')







except Exception as e:
    print(f'total {total} - Error en el tronco del procedimiento {e}')
    x = input('hay error anote y pulse enter ................')

