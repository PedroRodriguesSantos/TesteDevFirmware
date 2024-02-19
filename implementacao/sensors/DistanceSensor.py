from drivers.I2C.I2C_Read import readI2C

#Leitura do sensor de distancia
"""
- Leitura 0 a 100 metros
- Leitura ordenada de forma crescente;
"""
def distanceSensorRead():
    id = 2
    value_read = 0
    
    messages = []
    message = readI2C(id, value_read)
    messages.append(message)
    
    return sorted(messages, key=lambda x: x["VALOR_LIDO"])




