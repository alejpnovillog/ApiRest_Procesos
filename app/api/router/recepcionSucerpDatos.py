from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

async def procesar_archivos(ubicacion_carpeta: str):
    # Lógica para procesar los archivos en la ubicación de la carpeta
    # ...
    print(f"Proceso iniciado para la carpeta: {ubicacion_carpeta}")

@app.post("/procesar_archivos")
async def endpoint_procesar_archivos(ubicacion_carpeta: str, background_tasks: BackgroundTasks):
    # Agrega la tarea al fondo para ser ejecutada asincrónicamente
    background_tasks.add_task(procesar_archivos, ubicacion_carpeta)

    # Responde inmediatamente sin esperar a que termine el proceso
    return {"mensaje": "Proceso de archivos iniciado en segundo plano"}
