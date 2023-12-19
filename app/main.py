# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# controlamos las librerias que importamos
# DOCUMENTACION LINK https://fastapi.tiangolo.com/tutorial/bigger-applications/
try:

    #  Uvicorn es un servidor web ASGI (interfaz de puerta de enlace de servidor asíncrono)
    import uvicorn

    from fastapi import FastAPI

   
    # recuperamos todas las rutas posibles
    from api.routers import router as main_router

except Exception as e:
    print(f'Falta algun modulo en main --> {e}')


try:
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # creamos una instancia de la clase  FastAPI donde antes de usar la operacion de ruta ejecuta la dependencia
    app = FastAPI()
    
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # incluimos rutas previamente definidas en creamos una instancia de la clase  FastAPI
    # incluimos las rutas que  utilizan para obtener informacion para las PROVINCIAS
    app.include_router(router=main_router)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # En esta operacion de ruta 
    @app.get("/")
    async def root():
        """
    
        Returns:
            _type_:     Retornamos un diccionario 
            
        """    """"""
        return {"message": "Esta es la solicitud para la raiz de la aplicacion!"}



except Exception as e:
    print(f'Falta algun modulo en main --> {e}')



# Llamamos al servidor para que inicie
if __name__ ==  "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
