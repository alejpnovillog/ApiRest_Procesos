try:

    from jwt import encode, decode
    from jwt import exceptions
    from os import getenv
    from datetime import datetime, timedelta
    from flask import jsonify
    from app_Config import constantes

except Exception as e:
    print(f'Falta algun modulo {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Tiempo de  valides del token
def expire_date(days):
    try:

        now = datetime.now()
        new_date = now + timedelta(days)
        return new_date

    except Exception as e:
        print(f'Error - expire_date {e}')


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Generar un token
def write_token(**data):
    try:

        token = encode(payload={**data, "exp": expire_date(2)},
                       key=constantes.SECRET, algorithm="HS256")
        return token.encode("UTF-8")
    except Exception as e:
        print(f'Error - write_token {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Validacion del token
def validate_token(token, output=False):

    try:
        if output:
            error = dict()
            return decode(token, key=constantes.SECRET, algorithms=["HS256"]), error
        decode(token, key=getenv("SECRET"), algorithms=["HS256"])

    except exceptions.DecodeError:
        #response = jsonify({"message": "Invalid Token"})
        #response.status_code = 401
        #return response
        return False, {"error": "token invalido"}

    except exceptions.ExpiredSignatureError:
        #response = jsonify({"message": "Token Expired"})
        #response.status_code = 401
        #return response
        return False, {"error": "token ha expirado"}