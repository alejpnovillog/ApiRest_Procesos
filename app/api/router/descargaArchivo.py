# invocacion http://tu-api-rest/descargar_archivo 

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/descargar_archivo")
def descargar_archivo():
    # Lógica para leer el archivo
    ruta_archivo = "ruta/del/archivo/archivo.txt"

    # Utiliza FileResponse para devolver el archivo como respuesta
    return FileResponse(ruta_archivo, filename="archivo_descargado.txt")
