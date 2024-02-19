import random

def readI2C(id, value_read):

    #Simulacao leitura sensores
    if id == 0:  #Sensor de Luminosidade
        value_read = random.randint(0, 100) # 0 é ausência de luz, 100 é luz intensa
    elif id == 1:  #Sensor de Bateria
        value_read = random.randint(0, 25)  # 0V a 25V
    elif id == 2:  #Sensor de Distancia
        value_read = random.randint(0, 100) # 0 a 100 metros 

    else:
        value_read = 0


    checksum = (id + value_read) % 256
    return {"ID": id, "VALOR_LIDO": value_read, "CHECKSUM": checksum}

