from app_Abstract.gestionRegistros import GestionRegistros
from app_Config import constantes

impr = GestionRegistros(ambiente=constantes.ENV_GX)

# tablaTipoRegistro
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.tipoRegistro_Dal)

# tablaTipoSubRegistro
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.tipoSubRegistro_Dal)

# tablaTipoCuerpo
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.tipoCuerpo_Dal)

# tablaTipoTitular
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.tipoTitular_Dal)

# tablaTipoOrigen
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.tipoOrigen_Dal)

# tablaTipoMovimiento
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.tipoMovimiento_Dal)

# tablaTipoPago
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.tipoPago_Dal)

# tablaTipoMoneda
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.tipoMoneda_Dal)

# tablaTipoDocumento
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.tipoDocumento_Dal)

# tablaProvincias
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.provincias_Dal)

# tablaEstado
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.estado_Dal)

# tablaTipoCuota
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.tipoCuota_Dal)

# tablaEncabezado
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.registroEncabezado_Dal)

# tablaAltaImpositiva
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.altaImpositiva_Dal)

# tablaAltaImpositivaTitular
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.altaImpositivaTitular_Dal)

# tablaBajaImpositiva
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.bajaImpositiva_Dal)

# tablaBajaImpositivaTitular
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.bajaImpositivaTitular_Dal)

# tablaImpuestosSellos
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.impuestoSellos_Dal)

# tablaImpuestosSellosPartes
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.impuestoSellosPartes_Dal)

# tablaImpuestosSellosPartesTipoTramite
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.impuestoSellosPartesTipoTramite_Dal)

# tablaImpuestosAutomotor
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.impuestoAutomotor_Dal)

# tablaInformacionVehiculo
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.informacionVehiculo_Dal)

# tablaInformacionVehiculoTitular
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.informacionVehiculoTitular_Dal)

# tablaCambioTitularidad
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.cambioTitularidad_Dal)

# tablaCambioTitularidadTitular
ojetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.cambioTitularidadTitular_Dal)

# tablaInformacionRadicacion
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.informacionRadicacion_Dal)

# tablaAnulacionTramitesSellos
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.anulacionTramitesSellos_Dal)

# tablaAnulacionTramitesSellosDetalle
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.anulacionTramitesSellosDetalle_Dal)

# tablaTramitesGenerales
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.tramitesGenerales_Dal)

# tablaTramitesGeneralesTitulares
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.tramitesGeneralesTitular_Dal)

# tablaPie
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.pie_Dal)

# tablaApiToken
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.apiToken_Dal)


# tablaApiAumoso
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.apiAumoso_Dal)

# tablaApiEstados
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.apiEstados_Dal)

# tablaApiTareas
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.apiTareas_Dal)

# tablaApiEstadosTareas
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.apiEstadosTareas_Dal)

# tablaApiRegistros
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.apiRegistros_Dal)

# tablaApiTokenUser
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.apiTokenUser_Dal)

# tablaApiToken
objetoTabla_Dal, campos, insert, update, delete = impr.get_Struct_Tabla(impr.apiToken_Dal)


print(objetoTabla_Dal)
print(campos)
print(insert)
print(update)
print(delete)


