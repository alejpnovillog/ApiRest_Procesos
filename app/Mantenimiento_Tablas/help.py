from flask import Flask
from flask import jsonify

from app_Formularios.datos_Formularios import form0001
# Clases para menejar la aplicacion



# GENERO LA INSTANCIA
app = Flask('__name__')
#app = Flask('help')
app.config['JSON_AS_ASCII'] = False



#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN PROVINCIA
@app.route('/provinciaaddhlp/')
def provinciaaddhlp():

    consulta = form0001.provinciaaddhlp()
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE LA PROVINCIA
@app.route('/provinciaupdhlp/')
def provinciaupdhlp():

    consulta = {
        'update'  : {
            'PROVINCIAID'   : {'hidden':'on', 'name':'provinciaid', 'value':''},
            'PROVINCIA'     : {
                'placeholder': 'Codigo de la Provincia',
                'name' :'provincia',
                'value':''
                },
            'DESCPROVINCIA' : {
                'placeholder': 'Ingrese el Nombre de la Provincia',
                'name':'descprovincia',
                'type':'text',
                'length':'50',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            },
        'btn':[{'name':'Provincias', 'link':'http://localhost:5000/provinciawrkhlp/'}]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DE LA PROVINCIA
@app.route('/provinciawrkhlp/')
def provinciawrkhlp():

    consulta = {
        'lista': [
            {
                'PROVINCIAID'   : {'hidden':'on', 'value':''},
                'PROVINCIA'     : {
                    'placeholder': 'Codigo de la Provincia',
                    'name': 'provincia',
                    'value': ''
                    },
                'DESCPROVINCIA' : {
                    'placeholder': 'Nombre de la Provincia',
                    'name': 'descprovincia',
                    'value': '',
                    },
                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/provinciaupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/provinciaaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)

#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN TIPO CUERPO
@app.route('/tipocuerpoaddhlp/')
def tipocuerpoaddhlp():

    consulta = {
        'add': {
            'TIPOCUERPO'        :{
                'placeholder': 'Ingrese el Codigo del Tipo del Cuerpo',
                'name' :'tipocuerpo',
                'type' :'text',
                'length':'2',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 2 caracteres'
                },
            'DESCTIPOCUERPO'    : {
                'placeholder': 'Ingrese la descripcion del Tipo del Cuerpo',
                'name':'desctipocuerpo',
                'type':'text',
                'length':'50',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            'btn': [{'name': 'Tipos de Cuerpos', 'link': 'http://localhost:5000/tipocuerpowrkhlp/'}]
        }
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE TIPO CUERPO
@app.route('/tipocuerpoupdhlp/')
def tipocuerpoupdhlp():

    consulta = {
        'update': {
            'TIPOCUERPOID'      : {'hidden':'on', 'name':'tipocuerpoid', 'value':''},
            'TIPOCUERPO'        : {'name':'tipocuerpoid', 'value':''},
            'DESCTIPOCUERPO'    : {
                'placeholder': 'Ingrese la descripcion del Tipo del Cuerpo',
                'name': 'desctipocuerpo',
                'type': 'text',
                'length': '50',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            'btn': [{'name': 'Tipos de Cuerpos', 'link': 'http://localhost:5000/tipocuerpowrkhlp/'}]
        }
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL TIPO CUERPO
@app.route('/tipocuerpowrkhlp/')
def tipocuerpowrkhlp():

    consulta = {
        'lista': [
            {
                'TIPOCUERPOID'    : {'hidden':'on', 'name':'tipocuerpoid', 'value':''},
                'TIPOCUERPO'      : {
                    'placeholder': 'Codigo del Tipo del Cuerpo',
                    'name': 'tipocuerpo',
                    'value': ''
                    },
                'DESCTIPOCUERPO'  : {
                    'placeholder': 'Nombre del Tipo del Cuerpo',
                    'name': 'desctipocuerpo',
                    'value': '',
                },
                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/tipocuerpoupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/tipocuerpoaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN TIPO DE CUOTA
@app.route('/tipocuotaaddhlp/')
def tipocuotaaddhlp():

    consulta = {
        'add': {
            'TIPOCUOTA'     : {
                'placeholder': 'Ingrese el Tipo de Cuota',
                'name' :'tipocuota',
                'type' :'integer',
                'min':'1', 'max':'10',
                'value':'',
                'error':'Debe ingresarse un valor - El valor debe ser numerico'
            },
            'DESCTIPOCUOTA' : {
                'placeholder': 'Ingrese la Descripcion del Tipo de Cuota',
                'name':'desctipocuota',
                'type':'text',
                'length':'50',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 50 caracteres'
                }
            },
        'btn':[{'name':'TipoCuotas', 'link':'http://localhost:5000/tipocuotawrkhlp/'}]
    }

    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE TIPO DE CUOTA
@app.route('/tipocuotaupdhlp/')
def tipocuotaupdhlp():

    consulta = {
        'update': {
            'TIPOCUOTAID'      : {'hidden':'on', 'name':'tipocuotaid', 'value':''},
            'TIPOCUOTA'        : {'name':'tipocuota', 'value':''},
            'DESCTIPOCUOTA'    : {
                'placeholder': 'Ingrese la descripcion del Tipo de Cuota',
                'name': 'desctipocuota',
                'type': 'text',
                'length': '50',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            'btn':[{'name':'TipoCuotas', 'link':'http://localhost:5000/tipocuotawrkhlp/'}]
        }
    }
    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL TIPO DE CUOTA
@app.route('/tipocuotawrkhlp/')
def tipocuotawrkhlp():

    consulta = {
        'lista': [
            {
                'TIPOCUOTAID'    : {'hidden':'on', 'name':'tipocuotaid', 'value':''},
                'TIPOCUOTA'      : {
                    'placeholder': 'Codigo del Tipo de Cuota',
                    'name': 'tipocuota',
                    'value': ''
                    },
                'DESCTIPOCUOTA'  : {
                    'placeholder': 'Nombre del Tipo del Cuota',
                    'name': 'desctipocuota',
                    'value': '',
                },
                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/tipocuotaupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/tipocuotaaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)




#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN TIPO DE DOCUMENTO
@app.route('/tipodocumentoaddhlp/')
def tipodocumentoaddhlp():

    consulta = {
        'add': {
            'TIPODOCUMENTO'     : {
                'placeholder': 'Ingrese el Tipo de Documento',
                'name' :'tipodocumento',
                'type' :'integer',
                'min':'1', 'max':'10',
                'value':'',
                'error':'Debe ingresarse un valor - El valor debe ser numerico'
            },
            'DESCTIPODOCUMENTO' : {
                'placeholder': 'Ingrese la Descripcion del Tipo de Documento',
                'name':'desctipodocumento',
                'type':'text',
                'length':'50',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 50 caracteres'
                }
            },
        'btn':[{'name':'TipoDocumentos', 'link':'http://localhost:5000/tipodocumentowrkhlp/'}]
    }

    return jsonify(**consulta)




#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DEL TIPO DE DOCUMENTOS
@app.route('/tipodocumentoupdhlp/')
def tipodocumentoupdhlp():

    consulta = {
        'update': {
            'TIPODOCUMENTOID'      : {'hidden':'on', 'name':'tipodocumentoid', 'value':''},
            'TIPODOCUMENTO'        : {'name':'tipodocumento', 'value':''},
            'DESCTIPODOCUMENTO'    : {
                'placeholder': 'Ingrese la descripcion del Tipo de Documento',
                'name': 'desctipodocumento',
                'type': 'text',
                'length': '50',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            'btn':[{'name':'TipoDocumentos', 'link':'http://localhost:5000/tipodocumentowrkhlp/'}]
        }
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL TIPO DE DOCUMENTOS
@app.route('/tipodocumentowrkhlp/')
def tipodocumentowrkhlp():

    consulta = {
        'lista': [
            {
                'TIPODOCUMENTOID'    : {'hidden':'on', 'name':'tipodocumentoid', 'value':''},
                'TIPODOCUMENTO'      : {
                    'placeholder': 'Codigo del Tipo de Documento',
                    'name': 'tipodocumento',
                    'value': ''
                    },
                'DESCTIPODOCUMENTO'  : {
                    'placeholder': 'Nombre del Tipo de Documento',
                    'name': 'desctipodocumento',
                    'value': '',
                },
                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/tipodocumentoupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/tipodocumentoaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)




#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN TIPO ESTADO
@app.route('/tipoestadoaddhlp/')
def tipoestadoaddhlp():

    consulta = {
        'add': {
            'ESTADO'     : {
                'placeholder': 'Ingrese el Tipo de Estado',
                'name' :'estado',
                'type':'text',
                'length':'2',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 2 caracteres'
            },
            'DESCESTADO' : {
                'placeholder': 'Ingrese la Descripcion del Tipo de Estado',
                'name':'descestado',
                'type':'text',
                'length':'50',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 50 caracteres'
                }
            },
        'btn':[{'name':'TipoEstados', 'link':'http://localhost:5000/tipoestadowrkhlp/'}]
    }

    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE TIPO ESTADO
@app.route('/tipoestadoupdhlp/')
def tipoestadoupdhlp():


    consulta = {
        'update': {
            'ESTADOID'      : {'hidden':'on', 'name':'estadoid', 'value':''},
            'ESTADO'        : {'name':'estado', 'value':''},
            'DESCESTADO'    : {
                'placeholder': 'Ingrese la descripcion del Tipo de Estado',
                'name': 'desctipoestado',
                'type': 'text',
                'length': '50',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            'btn':[{'name':'TipoEstados', 'link':'http://localhost:5000/tipoestadowrkhlp/'}]
        }
    }
    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL TIPO ESTADO
@app.route('/tipoestadowrkhlp/')
def tipoestadowrkhlp():


    consulta = {
        'lista': [
            {
                'ESTADOID'    : {'hidden':'on', 'name':'estadoid', 'value':''},
                'ESTADO'      : {
                    'placeholder': 'Codigo del Tipo de Estado',
                    'name': 'tipoestado',
                    'value': ''
                    },
                'DESCESTADO'  : {
                    'placeholder': 'Nombre del Tipo de Estado',
                    'name': 'desctipoestado',
                    'value': '',
                },
                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/tipoestadoupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/tipoestadoaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)




#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN TIPO DE MONEDA
@app.route('/tipomonedaaddhlp/')
def tipomonedaaddhlp():

    consulta = {
        'add': {
            'CODIGOMONEDA'     : {
                'placeholder': 'Ingrese el Codigo de Moneda',
                'name' :'codigomoneda',
                'type' :'integer',
                'min':'1', 'max':'10',
                'value':'',
                'error':'Debe ingresarse un valor - El valor debe ser numerico'
            },
            'DESCTIPOMONEDA' : {
                'placeholder': 'Ingrese la Descripcion del Tipo de Moneda',
                'name':'desctipomoneda',
                'type':'text',
                'length':'50',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 50 caracteres'
                }
            },
        'btn':[{'name':'TipoMonedas', 'link':'http://localhost:5000/tipomonedawrkhlp/'}]
    }

    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE TIPO DE MONEDA
@app.route('/tipomonedaupdhlp/')
def tipomonedaupdhlp():

    consulta = {
        'update': {
            'CODIGOMONEDAID'      : {'hidden':'on', 'name':'codigomonedaid', 'value':''},
            'CODIGOMONEDA'        : {'name':'codigomoneda', 'value':''},
            'DESCTIPOMONEDA'    : {
                'placeholder': 'Ingrese la descripcion del Tipo de Moneda',
                'name': 'desctipomoneda',
                'type': 'text',
                'length': '50',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            'btn':[{'name':'TipoMonedas', 'link':'http://localhost:5000/tipomonedawrkhlp/'}]
        }
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL TIPO DE MONEDA
@app.route('/tipomonedawrkhlp/')
def tipomonedawrkhlp():

    consulta = {
        'lista': [
            {
                'CODIGOMONEDAID'    : {'hidden':'on', 'name':'codigomonedaid', 'value':''},
                'CODIGOMONEDA'      : {
                    'placeholder': 'Codigo del Tipo de Moneda',
                    'name': 'codigomoneda',
                    'value': ''
                    },
                'DESCTIPOMONEDA'  : {
                    'placeholder': 'Nombre del Tipo de Moneda',
                    'name': 'desctipomoneda',
                    'value': '',
                },
                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/tipomonedaupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/tipomonedaaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN TIPO DE MOVIMIENTO
@app.route('/tipomovimientoaddhlp/')
def tipomovimientoaddhlp():

    consulta = {
        'add': {
            'CODIGOTIPOMOVIMIENTO'     : {
                'placeholder': 'Ingrese el Tipo de Movimiento',
                'name' :'codigotipomovimiento',
                'type' :'integer',
                'min':'1', 'max':'10',
                'value':'',
                'error':'Debe ingresarse un valor - El valor debe ser numerico'
            },
            'DESCTIPOMOVIMIENTO' : {
                'placeholder': 'Ingrese la Descripcion del Tipo de Movimiento',
                'name':'desctipomovimiento',
                'type':'text',
                'length':'50',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 50 caracteres'
                }
            },
        'btn':[{'name':'TipoMovimientos', 'link':'http://localhost:5000/tipomovimientowrkhlp/'}]
    }

    return jsonify(**consulta)




#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE TIPO DE MOVIMIENTO
@app.route('/tipomovimientoupdhlp/')
def tipomovimientoupdhlp():

    consulta = {
        'update': {
            'CODIGOTIPOMOVIMIENTOID'      : {'hidden':'on', 'name':'codigotipomovimientoid', 'value':''},
            'CODIGOTIPOMOVIMIENTO'        : {'name':'codigotipomovimiento', 'value':''},
            'DESCTIPOMOVIMIENTO'    : {
                'placeholder': 'Ingrese la descripcion del Tipo de Movimiento',
                'name': 'desctipomovimiento',
                'type': 'text',
                'length': '50',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            'btn':[{'name':'TipoMonedas', 'link':'http://localhost:5000/tipomovimientowrkhlp/'}]
        }
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL TIPO DE MOVIMIENTO
@app.route('/tipomovimientowrkhlp/')
def tipomovimientowrkhlp():


    consulta = {
        'lista': [
            {
                'CODIGOTIPOMOVIMIENTOID'    : {'hidden':'on', 'name':'codigotipomovimientoid', 'value':''},
                'CODIGOTIPOMOVIMIENTO'      : {
                    'placeholder': 'Codigo del Tipo de Movimiento',
                    'name': 'codigotipomovimiento',
                    'value': ''
                    },
                'DESCTIPOMOVIMIENTO'  : {
                    'placeholder': 'Nombre del Tipo de Movimiento',
                    'name': 'desctipomovimiento',
                    'value': '',
                },
                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/tipomovimientoupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/tipomovimientoaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN TIPO ORIGEN
@app.route('/tipoorigenaddhlp/')
def tipoorigenaddhlp():

    consulta = {
        'add': {
            'TIPOORIGEN'     : {
                'placeholder': 'Ingrese el Tipo de Origen',
                'name' :'tipoorigen',
                'type':'text',
                'length':'1',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 1 caracteres'
            },
            'DESCORIGEN' : {
                'placeholder': 'Ingrese la Descripcion del Tipo de Origen',
                'name':'desctipoorigen',
                'type':'text',
                'length':'50',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 50 caracteres'
                }
            },
        'btn':[{'name':'TipoOrigen', 'link':'http://localhost:5000/tipoorigenwrkhlp/'}]
    }

    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE TIPO ORIGEN
@app.route('/tipoorigenupdhlp/')
def tipoorigenupdhlp():

    consulta = {
        'update': {
            'ORIGENID'      : {'hidden':'on', 'name':'origenid', 'value':''},
            'TIPOORIGEN'    : {'name':'tipoorigen', 'value':''},
            'DESCORIGEN'    : {
                'placeholder': 'Ingrese la descripcion del Tipo de Origen',
                'name': 'desctorigen',
                'type': 'text',
                'length': '50',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            'btn':[{'name':'TipoOrigen', 'link':'http://localhost:5000/tipoorigenwrkhlp/'}]
        }
    }
    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL TIPO ORIGEN
@app.route('/tipoorigenwrkhlp/')
def tipoorigenwrkhlp():

    consulta = {
        'lista': [
            {
                'ORIGENID'    : {'hidden':'on', 'name':'origenid', 'value':''},
                'TIPOORIGEN'  : {
                    'placeholder': 'Codigo del Tipo de Origen',
                    'name': 'tipoorigen',
                    'value': ''
                    },
                'DESCORIGEN'  : {
                    'placeholder': 'Nombre del Tipo de Origen',
                    'name': 'desctipoorigen',
                    'value': '',
                },
                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/tipoorigenupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/tipoorigenaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN TIPO PAGO
@app.route('/tipopagoaddhlp/')
def tipopagoaddhlp():

    consulta = {
        'add': {
            'CODIGOFORMAPAGO'     : {
                'placeholder': 'Ingrese el Codigo de Forma de Pago',
                'name' :'codigoformapago',
                'type' :'integer',
                'min':'1', 'max':'10',
                'value':'',
                'error':'Debe ingresarse un valor - El valor debe ser numerico'
            },
            'DESCTIPOPAGO' : {
                'placeholder': 'Ingrese la Descripcion del Tipo de Pago',
                'name':'desctipopago',
                'type':'text',
                'length':'50',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 50 caracteres'
                }
            },
        'btn':[{'name':'TipoPago', 'link':'http://localhost:5000/tipopagowrkhlp/'}]
    }

    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE TIPO PAGO
@app.route('/tipopagoupdhlp/')
def tipopagoupdhlp():


    consulta = {
        'update': {
            'CODIGOFORMAPAGOID'     : {'hidden':'on', 'name':'codigoformapagoid', 'value':''},
            'CODIGOFORMAPAGO'       : {'name':'codigoformapago', 'value':''},
            'DESCTIPOPAGO'          : {
                'placeholder': 'Ingrese la descripcion del Tipo de Pago',
                'name': 'desctipopago',
                'type': 'text',
                'length': '50',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            'btn':[{'name':'TipoPagos', 'link':'http://localhost:5000/tipopagowrkhlp/'}]
        }
    }
    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL TIPO PAGO
@app.route('/tipopagowrkhlp/')
def tipopagowrkhlp():

    consulta = {
        'lista': [
            {
                'CODIGOFORMAPAGOID'    : {'hidden':'on', 'name':'codigoformapagoid', 'value':''},
                'CODIGOFORMAPAGO'  : {
                    'placeholder': 'Codigo del Tipo de Forma de Pago',
                    'name': 'codigoformapago',
                    'value': ''
                    },
                'DESCTIPOPAGO'  : {
                    'placeholder': 'Nombre del Tipo de Forma de Pago',
                    'name': 'desctipoopago',
                    'value': '',
                },
                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/tipopagoupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/tipopagoaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN TIPO DE REGISTRO
@app.route('/tiporegistroaddhlp/')
def tiporegistroaddhlp():

    consulta = {
        'add': {
            'TIPOREGISTRO'     : {
                'placeholder': 'Ingrese el Tipo de Registro',
                'name' :'tiporegistro',
                'type':'text',
                'length':'2',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 2 caracteres'
            },
            'DESCTIPOREGISTRO' : {
                'placeholder': 'Ingrese la Descripcion del Tipo de Registro',
                'name':'desctiporegistro',
                'type':'text',
                'length':'50',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 50 caracteres'
                }
            },
        'btn':[{'name':'TipoRegistro', 'link':'http://localhost:5000/tiporegistrowrkhlp/'}]
    }

    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE TIPO DE REGISTRO
@app.route('/tiporegistroupdhlp/')
def tiporegistroupdhlp():


    consulta = {
        'update': {
            'TIPOREGISTROID'     : {'hidden':'on', 'name':'codigoformapagoid', 'value':''},
            'TIPOREGISTRO'       : {'name':'codigoformapago', 'value':''},
            'DESCTIPOREGISTRO'          : {
                'placeholder': 'Ingrese la descripcion del Tipo de Reggistro',
                'name': 'desctiporegistro',
                'type': 'text',
                'length': '50',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            'btn':[{'name':'TipoRegistros', 'link':'http://localhost:5000/tiporegistrowrkhlp/'}]
        }
    }
    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL TIPO DE REGISTRO
@app.route('/tiporegistrowrkhlp/')
def tiporegistrowrkhlp():

    consulta = {
        'lista': [
            {
                'TIPOREGISTROID'    : {'hidden':'on', 'name':'tiporegistroid', 'value':''},
                'TIPOREGISTRO'  : {
                    'placeholder': 'Codigo del Tipo de Registro',
                    'name': 'tiporegistro',
                    'value': ''
                    },
                'DESCTIPOREGISTRO'  : {
                    'placeholder': 'Nombre del Tipo de Registro',
                    'name': 'desctipooregistro',
                    'value': '',
                },
                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/tiporegistroupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/tiporegistroaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN TIPO DE SUB REGISTRO
@app.route('/tiposubregistroaddhlp/')
def tiposubregistroaddhlp():


    consulta = {
        'add': {
            'TIPOSUBREGISTRO'     : {
                'placeholder': 'Ingrese el Tipo de Registro',
                'name' :'tiposubregistro',
                'type':'text',
                'length':'1',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 1 caracteres'
            },
            'DESCTIPOSUBREGISTRO' : {
                'placeholder': 'Ingrese la Descripcion del Tipo de Sub Registro',
                'name':'desctiposubregistro',
                'type':'text',
                'length':'50',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 50 caracteres'
                }
            },
        'btn':[{'name':'TipoSubRegistro', 'link':'http://localhost:5000/tiposubregistrowrkhlp/'}]
    }

    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE TIPO DE SUB REGISTRO
@app.route('/tiposubregistroupdhlp/')
def tiposubregistroupdhlp():

    consulta = {
        'update': {
            'TIPOSUBREGISTROID'     : {'hidden':'on', 'name':'tiposubregistroid', 'value':''},
            'TIPOSUBREGISTRO'       : {'name':'tiposubregistro', 'value':''},
            'DESCTIPOSUBREGISTRO'          : {
                'placeholder': 'Ingrese la descripcion del Tipo de Sub Registro',
                'name': 'desctiposubregistro',
                'type': 'text',
                'length': '50',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            'btn':[{'name':'TipoSubRegistros', 'link':'http://localhost:5000/tiposubregistrowrkhlp/'}]
        }
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL TIPO DE SUB REGISTRO
@app.route('/tiposubregistrowrkhlp/')
def tiposubregistrowrkhlp():

    consulta = {
        'lista': [
            {
                'TIPOSUBREGISTROID'    : {'hidden':'on', 'name':'tiposubregistroid', 'value':''},
                'TIPOSUBREGISTRO'  : {
                    'placeholder': 'Codigo del Tipo de Sub Registro',
                    'name': 'tiposubregistro',
                    'value': ''
                    },
                'DESCTIPOSUBREGISTRO'  : {
                    'placeholder': 'Nombre del Tipo de Sub Registro',
                    'name': 'desctiposubregistro',
                    'value': '',
                },
                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/tiposubregistroupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/tiposubregistroaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN TIPO TITULAR
@app.route('/tipotitularaddhlp/')
def tipotitularaddhlp():

    consulta = {
        'add': {
            'TIPOTITULAR'     : {
                'placeholder': 'Ingrese el Tipo de Titular',
                'name' :'tipotitular',
                'type':'text',
                'length':'1',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 1 caracteres'
            },
            'DESCTIPOTITULAR' : {
                'placeholder': 'Ingrese la Descripcion del Tipo de Titular',
                'name':'desctipotitular',
                'type':'text',
                'length':'50',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 50 caracteres'
                }
            },
        'btn':[{'name':'TipoTitular', 'link':'http://localhost:5000/tipotitularwrkhlp/'}]
    }

    return jsonify(**consulta)




#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE TIPO TITULAR
@app.route('/tipotitularupdhlp/')
def tipotitularupdhlp():


    consulta = {
        'update': {
            'TIPOTITULARID'     : {'hidden':'on', 'name':'tipotitularid', 'value':''},
            'TIPOTITULAR'       : {'name':'tipotitular', 'value':''},
            'DESCTIPOTITULAR'   : {
                'placeholder': 'Ingrese la descripcion del Tipo de Titular',
                'name': 'desctipotitular',
                'type': 'text',
                'length': '50',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 50 caracteres'
                },
            'btn':[{'name':'TipoTitular', 'link':'http://localhost:5000/tipotitularwrkhlp/'}]
        }
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL TIPO TITULAR
@app.route('/tipotitularwrkhlp/')
def tipotitularwrkhlp():

    consulta = {
        'lista': [
            {
                'TIPOTITULARID'     : {'hidden':'on', 'name':'tipotitularid', 'value':''},
                'TIPOTITULAR'       : {
                    'placeholder': 'Codigo del Tipo de Titular',
                    'name': 'tipotitular',
                    'value': ''
                    },
                'DESCTIPOTITULAR'  : {
                    'placeholder': 'Nombre del Tipo de Titular',
                    'name': 'desctipotitular',
                    'value': '',
                },
                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/tipotitularupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/tipotitularaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN API ESTADOS
@app.route('/apiestadosaddhlp/')
def apiestadosaddhlp():

    consulta = {
        'add': {
            'APIESTADODESCRIPCION' : {
                'placeholder': 'Ingrese la Descripcion del Api de Estado',
                'name':'apiestadodescripcion',
                'type':'text',
                'length':'100',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 100 caracteres'
                }
            },
        'btn':[{'name':'ApiEstados', 'link':'http://localhost:5000/apiestadowrkhlp/'}]
    }

    return jsonify(**consulta)




#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE API ESTADOS
@app.route('/apiestadosupdhlp/')
def apiestadosupdhlp():

    consulta = {
        'update': {
            'APIESTADOSID'     : {'hidden':'on', 'name':'apiestadoid', 'value':''},
            'APIESTADODESCRIPCION'   : {
                'placeholder': 'Ingrese la descripcion del Api del Estado',
                'name': 'apiestadodescripcion',
                'type': 'text',
                'length': '100',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 100 caracteres'
                },
            'btn':[{'name':'ApiEstados', 'link':'http://localhost:5000/apiestadowrkhlp/'}]
        }
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DE API ESTADOS
@app.route('/apiestadoswrkhlp/')
def apiestadoswrkhlp():


    consulta = {
        'lista': [
            {
                'APIESTADOSID'     : {'hidden':'on', 'name':'apiestadoid', 'value':''},
                'APIESTADODESCRIPCION'       : {
                    'placeholder': 'Api Estado Descripcion',
                    'name': 'apiestadodescripcion',
                    'value': ''
                    },
                'APIUSERCRT'  : {
                    'placeholder': 'Usuario de Creacion del Registro',
                    'name': 'apiusercrt',
                    'value': '',
                },
                'TOKENUSERCRTTIMESTAMP': {
                    'placeholder': 'Fecha y Hora de Creacion del Registro',
                    'name': 'tokenusercrttimestamp',
                    'value': '',
                },

                'APIUSERDLT': {
                    'placeholder': 'Usuario de Eliminacion del Registro',
                    'name': 'apiuserdlt',
                    'value': '',
                },
                'TOKENUSERDLTTIMESTAMP': {
                    'placeholder': 'Fecha y Hora de Eliminacion del Registro',
                    'name': 'tokenuserdlttimestamp',
                    'value': '',
                },

                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/apiestadoupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/apiestadoaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN API TAREAS
@app.route('/apitareasaddhlp/')
def apitareasaddhlp():

    consulta = {
        'add': {
            'APITAREASDESCRIPCION' : {
                'placeholder': 'Ingrese la Descripcion del Api de Tarea',
                'name':'apiestadodescripcion',
                'type':'text',
                'length':'100',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 100 caracteres'
                }
            },
        'btn':[{'name':'ApiTareas', 'link':'http://localhost:5000/apitareawrkhlp/'}]
    }

    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE API TAREAS
@app.route('/apitareasupdhlp/')
def apitareasupdhlp():

    consulta = {
        'update': {
            'APITAREASID'           : {'hidden':'on', 'name':'apitareasid', 'value':''},
            'APITAREASDESCRIPCION'  : {
                'placeholder': 'Ingrese la descripcion del Api de Tareas',
                'name': 'apitareasdescripcion',
                'type': 'text',
                'length': '100',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 100 caracteres'
                },
            'btn':[{'name':'ApiTareas', 'link':'http://localhost:5000/apitareawrkhlp/'}]
        }
    }
    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DE API TAREAS
@app.route('/apitareaswrkhlp/')
def apitareaswrkhlp():

    consulta = {
        'lista': [
            {
                'APITAREASID'     : {'hidden':'on', 'name':'apitareasid', 'value':''},
                'APITAREASDESCRIPCION'       : {
                    'placeholder': 'Api Tareas Descripcion',
                    'name': 'apitareasdescripcion',
                    'value': ''
                    },
                'APIUSERCRT'  : {
                    'placeholder': 'Usuario de Creacion del Registro',
                    'name': 'apiusercrt',
                    'value': '',
                },
                'TOKENUSERCRTTIMESTAMP': {
                    'placeholder': 'Fecha y Hora de Creacion del Registro',
                    'name': 'tokenusercrttimestamp',
                    'value': '',
                },

                'APIUSERDLT': {
                    'placeholder': 'Usuario de Eliminacion del Registro',
                    'name': 'apiuserdlt',
                    'value': '',
                },
                'TOKENUSERDLTTIMESTAMP': {
                    'placeholder': 'Fecha y Hora de Eliminacion del Registro',
                    'name': 'tokenuserdlttimestamp',
                    'value': '',
                },

                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/apitareaupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/apitareasaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN API REGISTROS
@app.route('/apiregistrosaddhlp/')
def apiregistrosaddhlp():


    consulta = {
        'add': {
            'APIREGISTROSDESCRIPCION' : {
                'placeholder': 'Ingrese la Descripcion del Api del Registro',
                'name':'apiregistrodescripcion',
                'type':'text',
                'length':'100',
                'value':'',
                'error':'Debe ingresarse un valor - Hasta 100 caracteres'
                },
            'APIREGISTROSNUMERO': {
                'placeholder': 'Ingrese el Numero del Registro',
                'name': 'apiregistronumero',
                'type' :'integer',
                'min':'1', 'max':'10',
                'value': '',
                'error': 'Debe ingresarse un valor - El valor debe ser numerico'
            }

        },
        'btn':[{'name':'ApiRegistros', 'link':'http://localhost:5000/apiregistrowrkhlp/'}]
    }

    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE API REGISTROS
@app.route('/apiregistrosupdhlp/')
def apiregistrosupdhlp():


    consulta = {
        'update': {
            'APIREGISTROSID'           : {'hidden':'on', 'name':'apiregistroid', 'value':''},
            'APIREGISTROSDESCRIPCION'  : {
                'placeholder': 'Ingrese la descripcion del Api de Registro',
                'name': 'apiregistrodescripcion',
                'type': 'text',
                'length': '100',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 100 caracteres'
                },
            'APIREGISTROSNUMERO': {
                'placeholder': 'Ingrese el Numero del Registro',
                'name': 'apiregistronumero',
                'type' :'integer',
                'min':'1', 'max':'10',
                'value': '',
                'error': 'Debe ingresarse un valor - El valor debe ser numerico'
            },

            'btn':[{'name':'ApiRegistros', 'link':'http://localhost:5000/apiregistrowrkhlp/'}]
        }
    }
    return jsonify(**consulta)



#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DE API REGISTROS
@app.route('/apiregistroswrkhlp/')
def apiregistroswrkhlp():

    consulta = {
        'lista': [
            {
                'APIREGISTROSID'           : {'hidden':'on', 'name':'apiregistroid', 'value':''},
                'APIREGISTROSDESCRIPCION'       : {
                    'placeholder': 'Api Registro Descripcion',
                    'name': 'apiregistrodescripcion',
                    'value': ''
                    },
                'APIREGISTROSNUMERO': {
                    'placeholder': 'Api Registro Numero',
                    'name': 'apiregistronumero',
                    'value': ''
                },
                'APIUSERCRT'  : {
                    'placeholder': 'Usuario de Creacion del Registro',
                    'name': 'apiusercrt',
                    'value': '',
                },
                'TOKENUSERCRTTIMESTAMP': {
                    'placeholder': 'Fecha y Hora de Creacion del Registro',
                    'name': 'tokenusercrttimestamp',
                    'value': '',
                },

                'APIUSERDLT': {
                    'placeholder': 'Usuario de Eliminacion del Registro',
                    'name': 'apiuserdlt',
                    'value': '',
                },
                'TOKENUSERDLTTIMESTAMP': {
                    'placeholder': 'Fecha y Hora de Eliminacion del Registro',
                    'name': 'tokenuserdlttimestamp',
                    'value': '',
                },

                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/apiregiostroupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/apiregostrosaddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN TOKEN USER
@app.route('/tokenuseraddhlp/')
def tokenuseraddhlp():

    consulta = {
        'add': {
            'APIUSERNOMBRE'  : {
                'placeholder': 'Ingrese el Nombre del Usuario',
                'name': 'apiusernombre',
                'type': 'text',
                'length': '10',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 10 caracteres'
                },
            'APIUSERPASS'    : {
                'placeholder': 'Ingrese la password del Usuario',
                'name': 'apiuserpass',
                'type': 'password',
                'length': '10',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 10 caracteres'
                },
            'APELLIDONOMBRE'  : {
                'placeholder': 'Ingrese el Apellido y Nombre',
                'name': 'apellidonombre',
                'type': 'text',
                'length': '150',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 150 caracteres'
                },

            'APIUSEREMAIL'    : {
                'placeholder': 'Ingrese el enail del Usuario',
                'name': 'apiuseremail',
                'type': 'email',
                'length': '256',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 256 caracteres'
                },

            'APIUSERWHATSAPP'  : {
                'placeholder': 'Ingrese el whatsapp del Usuario',
                'name': 'apiuserwhatsapp',
                'type': 'tel',
                'length': '20',
                'value': '',
                'error': 'Debe ingresarse un valor - Hasta 20 caracteres'
                },

            'TIPODOCUMENTO': [
                    {
                        'TIPODOCUMENTO' : {
                            'placeholder': 'Tipo de Documento',
                            'name': 'tipodocumento',
                            'value': ''
                        },
                        'DESCTIPODOCUMENTO': {
                            'placeholder': 'Tipo de Documento Descripcion',
                            'name': 'desctipodocumento',
                            'value': ''
                        },
                        'TIPODOCUMENTOID': {'hidden':'on', 'name':'tipodocumentoid', 'value':''}
                    }
                ],
            'NUMERODOCUMENTO'  : {
                'placeholder': 'Ingrese el whatsapp del Usuario',
                'name': 'numerodocumento',
                'type': 'bigint',
                'min': '1', 'max': '18',
                'value': '',
                'error': 'Debe ingresarse un valor - El valor debe ser numerico'
                },
            'APIREGISTROS': [
                    {
                        'APIREGISTROSDESCRIPCION': {
                            'placeholder': 'Api Registro Descripcion',
                            'name': 'apiregistrosdescripcion',
                            'value': ''
                            },
                        'APIREGISTROSNUMERO': {
                            'placeholder': 'Api Registro Numero',
                            'name': 'apiregistrosnumero',
                            'value': ''
                            },
                        'APIREGISTROSID'    : {'hidden':'on', 'name':'apiregistroid', 'value':''}
                    }
                ],
        },
        'btn':[{'name':'TokenUser', 'link':'http://localhost:5000/tokenuserwrkhlp/'}]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE TOKEN USER
@app.route('/tokenuserupdhlp/')
def tokenuserupdhlp():

    consulta = {
        'update': {
                'APIUSERID'    : {'hidden':'on', 'name':'apiuserid', 'value':''},
                'APIUSERNOMBRE': {
                    'placeholder': 'Ingrese el Nombre del Usuario',
                    'name': 'apiusernombre',
                    'type': 'text',
                    'length': '10',
                    'value': '',
                    'error': 'Debe ingresarse un valor - Hasta 10 caracteres'
                },
                'APIUSERPASS': {
                    'placeholder': 'Ingrese la password del Usuario',
                    'name': 'apiuserpass',
                    'type': 'password',
                    'length': '10',
                    'value': '',
                    'error': 'Debe ingresarse un valor - Hasta 10 caracteres'
                },
                'APELLIDONOMBRE': {
                    'placeholder': 'Ingrese el Apellido y Nombre',
                    'name': 'apellidonombre',
                    'type': 'text',
                    'length': '150',
                    'value': '',
                    'error': 'Debe ingresarse un valor - Hasta 150 caracteres'
                },

                'APIUSEREMAIL': {
                    'placeholder': 'Ingrese el enail del Usuario',
                    'name': 'apiuseremail',
                    'type': 'email',
                    'length': '256',
                    'value': '',
                    'error': 'Debe ingresarse un valor - Hasta 256 caracteres'
                },

                'APIUSERWHATSAPP': {
                    'placeholder': 'Ingrese el whatsapp del Usuario',
                    'name': 'apiuserwhatsapp',
                    'type': 'tel',
                    'length': '20',
                    'value': '',
                    'error': 'Debe ingresarse un valor - Hasta 20 caracteres'
                },

                'TIPODOCUMENTO': [
                    {
                        'TIPODOCUMENTO' : {
                            'placeholder': 'Tipo de Documento',
                            'name': 'tipodocumento',
                            'value': ''
                        },
                        'DESCTIPODOCUMENTO': {
                            'placeholder': 'Tipo de Documento Descripcion',
                            'name': 'desctipodocumento',
                            'value': ''
                        },
                        'TIPODOCUMENTOID': {'hidden':'on', 'name':'tipodocumentoid', 'value':''}
                    }
                ],

                'NUMERODOCUMENTO': {
                    'placeholder': 'Ingrese el whatsapp del Usuario',
                    'name': 'numerodocumento',
                    'type': 'bigint',
                    'min': '1', 'max': '18',
                    'value': '',
                    'error': 'Debe ingresarse un valor - El valor debe ser numerico'
                },

                'APIREGISTROS': [
                    {
                        'APIREGISTROSDESCRIPCION': {
                            'placeholder': 'Api Registro Descripcion',
                            'name': 'apiregistrosdescripcion',
                            'value': ''
                            },
                        'APIREGISTROSNUMERO': {
                            'placeholder': 'Api Registro Numero',
                            'name': 'apiregistrosnumero',
                            'value': ''
                            },
                        'APIREGISTROSID'    : {'hidden':'on', 'name':'apiregistroid', 'value':''}
                    }
                ],

                'APIESTADO'       : {
                    'placeholder': 'Estado del Usuario',
                    'name': 'apiestado',
                    'value': ''
                }
        },
        'btn': [{'name': 'TokenUser', 'link': 'http://localhost:5000/tokenuserwrkhlp/'}]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL TOKEN USER
@app.route('/tokenuserwrkhlp/')
def tokenuserwrkhlp():

    consulta = {
        'lista': [
            {
                'APIUSERID'             : {'hidden':'on', 'name':'apiuserid', 'value':''},
                'APIUSERNOMBRE'         : {
                    'placeholder': 'Nombre del Usuario',
                    'name': 'apiusernombre',
                    'value': ''
                },

                'APELLIDONOMBRE'        : {
                    'placeholder': 'Apellido y Nombre del Usuario',
                    'name': 'apellidonombre',
                    'value': ''
                },

                'APIUSEREMAIL'          : {
                    'placeholder': 'Email del Usuario',
                    'name': 'apiuseremail',
                    'value': ''
                },

                'APIUSERWHATSAPP'       : {
                    'placeholder': 'Whatsapp del Usuario',
                    'name': 'apiuserwhatsapp',
                    'value': ''
                },

                'TIPODOCUMENTO'         : {
                    'TIPODOCUMENTO': {
                        'placeholder': 'Tipo de Documento',
                        'name': 'tipodocumento',
                        'value': ''
                    },
                    'DESCTIPODOCUMENTO': {
                        'placeholder': 'Tipo de Documento Descripcion',
                        'name': 'desctipodocumento',
                        'value': ''
                    },
                },
                'NUMERODOCUMENTO'       : {
                    'placeholder': 'Numero de Documento',
                    'name': 'numerodocumento',
                    'value': ''
                },
                    'APIREGISTROS'          :
                    {
                        'APIREGISTROSDESCRIPCION'   : 'varchar(100)',
                        'APIREGISTROSNUMERO'        : 'integer',
                    },

                'APIESTADO'             : {
                    'placeholder': 'Estado del Usuario',
                    'name': 'apiestado',
                    'value': ''
                },
                'APIUSERCRT': {
                    'placeholder': 'Usuario de Creacion del Registro',
                    'name': 'apiusercrt',
                    'value': '',
                },
                'TOKENUSERCRTTIMESTAMP': {
                    'placeholder': 'Fecha y Hora de Creacion del Registro',
                    'name': 'tokenusercrttimestamp',
                    'value': '',
                },

                'APIUSERDLT': {
                    'placeholder': 'Usuario de Eliminacion del Registro',
                    'name': 'apiuserdlt',
                    'value': '',
                },
                'TOKENUSERDLTTIMESTAMP': {
                    'placeholder': 'Fecha y Hora de Eliminacion del Registro',
                    'name': 'tokenuserdlttimestamp',
                    'value': '',
                },

                'btn':[
                    {'name':'modificar', 'link':'http://localhost:5000/tokenuserupdhlp/'},
                    {'name':'nuevo', 'link':'http://localhost:5000/tokenuseraddhlp/'}
                    ]
            }
        ]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA DAR DE ALTA UN API TOKEN
@app.route('/apitokenaddhlp/')
def apitokenaddhlp():

    consulta = {
        'add': {
            'APIUSER'       :[
                {
                    'APIUSERNOMBRE': {
                        'placeholder': 'Nombre del Usuario',
                        'name': 'apiusernombre',
                        'value': ''
                        },
                    'APIUSERID': {'hidden': 'on', 'name': 'apiuserid', 'value': ''}
                }

            ],
            'APIREGISTROS'  :[
                {

                    'APIREGISTROSDESCRIPCION'   : {
                        'placeholder': 'Descripcion del Registro',
                        'name': 'apiregistrosdescripcion',
                        'value': ''
                        },
                    'APIREGISTROSNUMERO'        : {
                        'placeholder': 'Numero del Registro',
                        'name': 'apiregistrosnumero',
                        'value': ''
                        },
                    'APIREGISTROID'             : {'hidden': 'on', 'name': 'apiregistroid', 'value': ''},


                }
            ],
        },
        'btn': [{'name': 'TokenUser', 'link': 'http://localhost:5000/apitokenwrkhlp/'}]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA CAMBIAR LOS DATOS DE API TOKEN
@app.route('/apitokenupdhlp/')
def apitokenupdhlp():

    consulta = {
        'update': {
            'TOKENAPIID'    : {'hidden': 'on', 'name': 'tokenapiid', 'value': ''},
            'APIUSER'       : {
                'APIUSERNOMBRE': {
                    'placeholder': 'Nombre del Usuario',
                    'name': 'apiusernombre',
                    'value': ''
                },
            },
            'APIREGISTROS'  :[
                {
                    'APIREGISTROSDESCRIPCION' : {
                        'placeholder': 'Descripcion del Registro',
                        'name': 'apiregistrosdescripcion',
                        'value': ''
                        },
                    'APIREGISTROSNUMERO'      : {
                        'placeholder': 'Numero del Registro',
                        'name': 'apiregistrosnumero',
                        'value': ''
                        },
                    'APIREGISTROID'           : {'hidden': 'on', 'name': 'apiregistroid', 'value': ''},
                }
            ],
        },
        'btn': [{'name': 'TokenUser', 'link': 'http://localhost:5000/apitokenwrkhlp/'}]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON DE LOS DATOS DEL API TOKEN
@app.route('/apitokenwrkhlp/')
def apitokenwrkhlp():

    consulta = {
        'lista': [
                {
                    'TOKENAPIID': {'hidden': 'on', 'name': 'tokenapiid', 'value': ''},
                    'APIUSERNOMBRE': {
                            'placeholder': 'Nombre del Usuario',
                            'name': 'apiusernombre',
                            'value': ''
                    },
                    'APIREGISTROSDESCRIPCION' : {
                            'placeholder': 'Descripcion del Registro',
                            'name': 'apiregistrosdescripcion',
                            'value': ''
                    },
                    'APIREGISTROSNUMERO'      : {
                            'placeholder': 'Numero del Registro',
                            'name': 'apiregistrosnumero',
                            'value': ''
                    },
                    'TOKENCONECTAR'         : {
                            'placeholder': 'Token utilizado al Conectar',
                            'name': 'tokenconectar',
                            'value': ''
                    },
                    'TOKENINICIOTRANSACCION': {
                            'placeholder': 'Inicio de la Transaccion',
                            'name': 'tokeniniciotransaccion',
                            'value': ''
                    },
                    'TOKENFINTRANSACCION'   : {
                            'placeholder': 'Finaliza la transaccion',
                            'name': 'tokenfintransaccion',
                            'value': ''
                    },
                    'btn':[
                            {'name':'modificar', 'link':'http://localhost:5000/apitokenupdhlp/'},
                            {'name':'nuevo', 'link':'http://localhost:5000/apitokenaddhlp/'}
                    ]
                }
        ]
    }
    return jsonify(**consulta)


#-------------------------------------------------------------------------
# ES LA RUTA PARA TRABAJAR CON EL MENU DE AYUDA
@app.route('/menuhlp/')
def menuhlp():

    consulta = {
        'menu_de_link': {
                    'ADD-PROVINCIA'             : 'http://localhost:5000/provinciaaddhlp/',
                    'UPD-PROVINCIA'             : 'http://localhost:5000/provinciaupdhlp/',
                    'WRK-PROVINCIA'             : 'http://localhost:5000/provinciawrkhlp/',
                    'ADD-TIPOCUERPO'            : 'http://localhost:5000/tipocuerpoaddhlp/',
                    'UPD-TIPOCUERPO'            : 'http://localhost:5000/tipocuerpoupdhlp/',
                    'WRK-TIPOCUERPO'            : 'http://localhost:5000/tipocuerpowrkhlp/',
                    'ADD-TIPOCUOTA'             : 'http://localhost:5000/tipocuotaaddhlp/',
                    'UPD-TIPOCUOTA'             : 'http://localhost:5000/tipocuotaupdhlp/',
                    'WRK-TIPOCUOTA'             : 'http://localhost:5000/tipocuotawrkhlp/',
                    'ADD-TIPODOCUMENTO'         : 'http://localhost:5000/tipodocumentoaddhlp/',
                    'UPD-TIPODOCUMENTO'         : 'http://localhost:5000/tipodocumentoupdhlp/',
                    'WRK-TIPODOCUMENTO'         : 'http://localhost:5000/tipodocumentowrkhlp/',
                    'ADD-TIPOESTADO'            : 'http://localhost:5000/tipoestadoaddhlp/',
                    'UPD-TIPOESTADO'            : 'http://localhost:5000/tipoestadoupdhlp/',
                    'WRK-TIPOESTADO'            : 'http://localhost:5000/tipoestadowrkhlp/',
                    'ADD-TIPOMONEDA'            : 'http://localhost:5000/tipomonedaaddhlp/',
                    'UPD-TIPOMONEDA'            : 'http://localhost:5000/tipomonedaupdhlp/',
                    'UPD-TIPOMONEDA'            : 'http://localhost:5000/tipomonedawrkhlp/',
                    'ADD-TIPOMOVIMIENTO'        : 'http://localhost:5000/tipomovimientoaddhlp/',
                    'UPD-TIPOMOVIMIENTO'        : 'http://localhost:5000/tipomovimientoupdhlp/',
                    'WRK-TIPOMOVIMIENTO'        : 'http://localhost:5000/tipomovimientowrkhlp/',
                    'ADD-TIPOORIGEN'            : 'http://localhost:5000/tipoorigenaddhlp/',
                    'UPD-TIPOORIGEN'            : 'http://localhost:5000/tipoorigenupdhlp/',
                    'WRK-TIPOORIGEN'            : 'http://localhost:5000/tipoorigenwrkhlp/',
                    'ADD-TIPOPAGO'              : 'http://localhost:5000/tipopagoaddhlp/',
                    'UPD-TIPOPAGO'              : 'http://localhost:5000/tipopagoupdhlp/',
                    'WRK-TIPOPAGO'              : 'http://localhost:5000/tipopagowrkhlp/',
                    'ADD-TIPOREGISTRO'          : 'http://localhost:5000/tiporegistroaddhlp/',
                    'UPD-TIPOREGISTRO'          : 'http://localhost:5000/tiporegistroupdhlp/',
                    'WRK-TIPOREGISTRO'          : 'http://localhost:5000/tiporegistrowrkhlp/',
                    'ADD-TIPOSUBREGISTRO'       : 'http://localhost:5000/tiposubregistroaddhlp/',
                    'UPD-TIPOSUBREGISTRO'       : 'http://localhost:5000/tiposubregistroupdhlp/',
                    'WRK-TIPOSUBREGISTRO'       : 'http://localhost:5000/tiposubregistrowrkhlp/',
                    'ADD-TIPOTITULARIDAD'       : 'http://localhost:5000/tipotitularaddhlp/',
                    'UPD-TIPOTITULARIDAD'       : 'http://localhost:5000/tipotitularupdhlp/',
                    'WRK-TIPOTITULARIDAD'       : 'http://localhost:5000/tipotitularwrkhlp/',
                    'ADD-APIESTADOS'            : 'http://localhost:5000/apiestadosaddhlp/',
                    'UPD-APIESTADOS'            : 'http://localhost:5000/apiestadosupdhlp/',
                    'WRK-APIESTADOS'            : 'http://localhost:5000/apiestadoswrkhlp/',
                    'ADD-APITAREAS'             : 'http://localhost:5000/apitareasaddhlp/',
                    'UPD-APITAREAS'             : 'http://localhost:5000/apitareasupdhlp/',
                    'WRK-APITAREAS'             : 'http://localhost:5000/apitareaswrkhlp/',
                    'ADD-APIREGISTROS'          : 'http://localhost:5000/apiregistrosaddhlp/',
                    'UPD-APIREGISTROS'          : 'http://localhost:5000/apiregistrosupdhlp/',
                    'WRK-APIREGISTROS'          : 'http://localhost:5000/apiregistroswrkhlp/',
                    'ADD-TOKENUSER'             : 'http://localhost:5000/tokenuseraddhlp/',
                    'UPD-TOKENUSER'             : 'http://localhost:5000/tokenuserupdhlp/',
                    'WRK-TOKENUSER'             : 'http://localhost:5000/tokenuserwrkhlp/',
                    'ADD-APITOKEN'              : 'http://localhost:5000/apitokenaddhlp/',
                    'UPD-APITOKEN'              : 'http://localhost:5000/apitokenupdhlp/',
                    'WRK-APITOKEN'              : 'http://localhost:5000/apitokenwrkhlp/',
        }
    }
    return jsonify(**consulta)













#-------------------------------------------------------------------------
# -- Esta sentencia me permite hacer un loop siempre escuchando
#-------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
