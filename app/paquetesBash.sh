#!/bin/bash

# Obtener la hora de inicio del script
start_time=$SECONDS

# Mostrar mensaje al iniciar
echo "Inicio del script: $(date)"

# Obtener la lista de paquetes instalados con dpkg --get-selections
dpkg --get-selections > paquetes.txt

# Inicializar el archivo terminal.txt
echo "Paquete | Estado | Información del Paquete" > terminal.txt

# Iterar sobre cada línea del archivo de paquetes
while IFS=$'\t' read -r package status; do
    # Obtener la información del paquete con apt show
    info=$(apt show "$package" 2>/dev/null | awk 'BEGIN { ORS=" | "} /Package|Version|Priority|Section/ {print}')

    # Imprimir la línea en el archivo terminal.txt
    echo "$package | $status | $info" >> terminal.txt
done < paquetes.txt

# Obtener la hora de finalización del script
end_time=$SECONDS

# Calcular la duración del script
duration=$((end_time - start_time))

# Mostrar mensaje al finalizar
echo "Fin del script: $(date)"

# Imprimir la duración del script
echo "El script se ejecutó durante $duration segundos."

echo "Archivo 'terminal.txt' creado con éxito."
