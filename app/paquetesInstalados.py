'''

from datetime import datetime
import subprocess

try:
    
    inicio = datetime.now()
    print('Inicio del Proceso....', inicio)
    # Ejecutar el comando dpkg para obtener la lista de paquetes instalados
    result = subprocess.run(['dpkg', '--get-selections'], stdout=subprocess.PIPE, text=True)
    package_lines = result.stdout.strip().split('\n')

    # Crear una lista para almacenar las líneas que se escribirán en el archivo Markdown
    markdown_lines = []

    # Iterar sobre las líneas del comando dpkg
    for line in package_lines:
        last_updated = {}
        package, status = line.split('\t')[0], line.split('\t')[-1]

        try:
            # Ejecutar el comando apt show para obtener la fecha de la última actualización
            apt_show_result = subprocess.run(['apt', 'show', package], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
            ejemplo = apt_show_result.stdout.strip().split('\n')
        except subprocess.CalledProcessError as e:
            # Capturar y mostrar errores de apt
            print(f"Error al obtener información para {package}: {e.stderr}")

        # Actualizar el diccionario con la última fecha de actualización
        last_updated[package] = {'Estado': status, 'Detalle': ejemplo}

        # Filtrar los índices específicos de la lista de detalles
        filtered_detalle = [
            last_updated[package]['Detalle'][i] if i < len(last_updated[package]['Detalle']) else None for i in [0, 1]
        ]

        # Manejar el índice 3 por separado
        detalle_3 = last_updated[package]['Detalle'][3] if len(last_updated[package]['Detalle']) > 3 else None

        # Agregar una línea por paquete en forma horizontal
        markdown_lines.append(f"| {package} | {last_updated[package]['Estado']} | {' | '.join(filtered_detalle + [detalle_3]) if detalle_3 is not None else 'None'} |")

        print(package, status) 
        
except Exception as e:
    print(f'Hay errores --> {e}')
else:
    # Escribir las líneas en el archivo Markdown solucion.md
    with open('solucion.md', 'w') as markdown_file:
        for line in markdown_lines:
            markdown_file.write(line + '\n')

    print("Archivo 'solucion.md' creado con éxito.")
    print('Finalizacion del Proceso....', f'Inicio 'datetime.now())

'''

import subprocess
from tqdm import tqdm
from datetime import datetime

try:
    
    subprocess.run('clear', shell=True)
    
    print('PROCESAMIENTO DEL INFORME DE LOS PAQUETES QUE TIENE EL SISTEMA \n\n')
    
    # Obtener la lista de paquetes instalados con dpkg --get-selections
    result = subprocess.run(['dpkg', '--get-selections'], stdout=subprocess.PIPE, text=True)

    package_lines = result.stdout.strip().split('\n')

    # Crear un diccionario para almacenar la última fecha de actualización de cada paquete
    last_updated = {}

    # Inicializar la barra de progreso
    progress_bar = tqdm(package_lines, desc="Procesando paquetes", unit=" paquete")

    # Iterar sobre las líneas del comando dpkg
    for line in progress_bar:
        package, status = line.split('\t')[0], line.split('\t')[-1]

        try:
            # Ejecutar el comando apt show para obtener la fecha de la última actualización
            apt_show_result = subprocess.run(['apt', 'show', package], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
            info = apt_show_result.stdout.strip().split('\n')
        except subprocess.CalledProcessError as e:
            # Capturar y mostrar errores de apt
            print(f"Error al obtener información para {package}: {e.stderr}")
            info = []

        # Actualizar el diccionario con la última fecha de actualización
        last_updated[package] = {'Estado': status, 'Detalle': info}

    # Obtener la hora de finalización del script
    end_time = datetime.now()

    # Crear el archivo de salida terminal.txt
    with open('terminal.md', 'w') as output_file:
        
        
        output_line = f'# INFORME DE LOS PAQUETES DE LOC-OS AL {datetime.now()}\n'
        output_file.write(output_line)
        
        
        output_line = '| Paquete | Estado | Package | Version | Priority | Section | APT-Source |\n'
        output_file.write(output_line)

        output_line = '|---------|--------|---------|---------|----------|---------|------------|\n'
        output_file.write(output_line)

        
        # Imprimir detalles de la lista en el archivo
        for package, data in last_updated.items():
            output_line = f"{package} | {data['Estado']} | {' | '.join(data['Detalle'])}\n"
            output_file.write(output_line)

    # Imprimir la hora de finalización del script
    print("Fin del script:", end_time)

except Exception as e:
    print(f'Hay errores --> {e}')
