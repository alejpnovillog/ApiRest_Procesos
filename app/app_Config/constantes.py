# Definimos las contantes para la administracion del modulo

# Conectores del MOTOR SQLITE
VALIDATOR               = "Validator"

# Conectores del MOTOR postgresql
POSTGRESQL_MATANZA           = "IseriesMatanza_postgres"
POSTGRESQL_GXPROD            = "IseriesGxProd_postgres"

# Conectores del MOTOR MYSQL
MYSQL_MATANZA           = "IseriesMatanza_mysql"
MYSQL_GXPROD            = "IseriesGxProd_mysql"

# Conectores del MOTOR ISERIES
TEST_MATANZA            = "Matanza_tst"
PROD_MATANZA            = "Matanza_prd"

TEST_ISERIES            = "Iseries_tst"
PROD_ISERIES            = "Iseries_prd"


# Ambientes
ENV_TARGET              = POSTGRESQL_GXPROD
ENV_MATANZA             = None
ENV_GX                  = PROD_ISERIES
ENV_SQ                  = VALIDATOR


# Cantidad de registros para un trabajar con
WRK_RECORDS = 200


# Tablas Id
TABLA_ESTADO                          = 1
TABLA_PROVINCIA                       = 2
TABLA_TIPO_CUERPO                     = 3
TABLA_TIPO_CUOTA                      = 4
TABLA_TIPO_DOCUMENTO                  = 5
TABLA_TIPO_MONEDA                     = 6
TABLA_TIPO_MOVIMIENTO                 = 7
TABLA_TIPO_ORIGEN                     = 8
TABLA_TIPO_PAGO                       = 9
TABLA_TIPO_REGISTRO                   = 10
TABLA_TIPO_SUB_REGISTRO               = 11
TABLA_TIPO_TITULAR                    = 12
TABLA_API_TOKEN_USER                  = 14
TABLA_API_ESTADOS                     = 15
TABLA_API_TOKEN                       = 18
TABLA_API_AUMOSO                      = 19
TABLA_API_REGISTROS                   = 20
TABLA_ALTAIMPOSITIVA                  = 21
TABLA_ALTAIMPOSITIVATITULAR           = 22
TABLA_ANULACIONTRAMITESSELLOS         = 23
TABLA_ANULACIONTRAMITESSELLOSDETALLE  = 24
TABLA_BAJAIMPOSITIVA                  = 25
TABLA_BAJAIMPOSITIVATITULAR           = 26
TABLA_CAMBIOTITULARIDAD               = 27
TABLA_CAMBIOTITULARIDADTITULAR        = 28
TABLA_ENCABEZADO                      = 29
TABLA_IMPUESTOAUTOMOTOR               = 34
TABLA_IMPUESTOSELLOS                  = 35
TABLA_IMPUESTOSELLOSPARTES            = 36
TABLA_IMPUESTOSELLOSPARTESTIPOTRAMITE = 37
TABLA_INFORMACIONVEHICULO             = 38
TABLA_INFORMACIONVEHICULOTITULAR      = 39
TABLA_INFORMACIORADICACION            = 40
TABLA_PIE                             = 41

# Switch Render Template
SWITCH_RENDER_TEMPLATE = False

# Render Paginas WRK
HTML_WRKESTADOS = 'estadowrk.html'

# Token
SECRET = '123'

# Directorio del Proyecto
DIR_PROYECTO = 'app'


PATH_EPAGOS_IMAGENES    = "C:\\Epagos\\archivos_Estaticos\\Imagenes\\"
URL_EPAGOS_MOSTRADOR    = "http://172.16.5.105:5000/epagos/mostrador"
HEADER_CONTENT_JSON     = "!'Content-type',!'application/json'"

