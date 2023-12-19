# PROPUESTA DE RECEPCION DE DATOS DE RENDICIONES

- Recibir el pedido de procesamiento a un servicio de API-REST

- Una vez concluido el procesamiento enviar un email al usuario que lanzo el proceso

## SERVICIO API-REST

- El servicio es montado en el servidor MlmSrv o en otro indicado por INFRAESTRUCTURA

- El servicio es ejecutado desde un ejecutable para que infraestructura pueda levantar el servicio en caso de baja del servidor

- La invocacion del servicio puede ser: 

> - Mediante la terminal verde ( para seguir teniendo el kiosco)

> - La ejecucion de un link desde el navegador 

> - Mediante un menu de procesos en una pagina web de procesos

## RESPUESTA DE FIN DEL PROCESAMIENTO DEL API-REST

- La respuesta de la finalizacion del proceso es enviando un email al usuario de lanzamiento con copia 


## UBICACION DE LOS ARCHIVOS RECIBIDOS DE SUCERP

- Los archivos recibidos de sucerp deben ser incorporados en una carpeta fija en un servidor determinado

- La ruta de los archivos recibidos es configurable
