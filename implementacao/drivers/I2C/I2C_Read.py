import random

messages = []

idx_light = 0
array_messages_light = [-1, 0, 39, 40, 100, 101]

idx_distance = 0
array_messages_distance = [-1, 0, 35, 70, 100, 101]

idx_battery = 0
array_messages_battery = [50, 40, 30, 20, 10, 9]


def readI2C(id):
    
    # Simulação de leitura de sensores
    if id == 0:  # Sensor de Luminosidade
            global idx_light

            if idx_light < len(array_messages_light):
                value_read = array_messages_light[idx_light]
                message = {"ID": 0, "VALOR_LIDO": value_read, "CHECKSUM": (0 + value_read) % 256}
                idx_light += 1
            else:
                  idx_light = 0


    elif id == 1:  # Sensor de Distância
            global idx_distance

            if idx_distance < len(array_messages_distance):
                value_read = array_messages_distance[idx_distance]
                message = {"ID": 0, "VALOR_LIDO": value_read, "CHECKSUM": (0 + value_read) % 256}
                idx_distance += 1
            else:
                  idx_distance = 0


    elif id == 2:  # Sensor de Bateria
            global idx_battery

            if idx_battery < len(array_messages_battery):
                value_read = array_messages_battery[idx_battery]
                message = {"ID": 0, "VALOR_LIDO": value_read, "CHECKSUM": (0 + value_read) % 256}
                idx_battery += 1
            else:
                  idx_battery = 0

    else:
        # ID Desconhecido
        value_read = 0
        checksum = (id + value_read) % 256
        message = {"ID": id, "VALOR_LIDO": value_read, "CHECKSUM": checksum}
        #messages.append(message)


    return message

