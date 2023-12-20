cadena_con_acentos = 'CIUDAD DEL LIB. GRAL. JOSÉ DE SAN MARTÍN'

import unidecode
cadena_sin_acentos = unidecode.unidecode(cadena_con_acentos)
print(len(cadena_con_acentos.encode("utf-8").hex()))
print(cadena_sin_acentos)
print(len(cadena_sin_acentos.encode("utf-8").hex()))

