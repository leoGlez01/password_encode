import random


def encode(cadena):
    # Here is a map with the keys and values that you want to determine
    nueva_cadena = ""
    for caracter in cadena:
        if caracter in mapping:
            nueva_cadena += mapping[caracter]
        else:
            nueva_cadena += caracter

    secret_key = (
        random.choice("df")
        + random.choice("hj")
        + random.choice("$^")
        + random.choice("%")
        + random.choice("#@")
        + random.choice("!?")
        + random.choice("-_")
        + random.choice("&f")
        + random.choice("vb")
        + "."
        + "L0123"
    )
    encrypted = nueva_cadena + "." + secret_key
    return encrypted


def decode(cadena):
    # Here is a map with the keys and values that you want to determine
    map_inv = {v: k for k, v in map.items()}
    nueva_cadena = ""
    for caracter in cadena:
        if caracter in map_inv:
            nueva_cadena += map_inv[caracter]
        elif caracter == ".":
            break
        else:
            nueva_cadena += caracter

    return nueva_cadena
