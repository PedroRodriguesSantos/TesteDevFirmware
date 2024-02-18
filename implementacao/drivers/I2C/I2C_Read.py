

def readI2C(id, value_read):
    checksum = (id + value_read) % 256
    return {"ID": id, "VALOR_LIDO": value_read, "CHECKSUM": checksum}

