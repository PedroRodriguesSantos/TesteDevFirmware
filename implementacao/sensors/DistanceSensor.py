from drivers.I2C.I2C_Read import readI2C

#Leitura do sensor de distancia
"""
- Leitura 0 a 100 metros
- Leitura ordenada de forma crescente;
"""
def distanceSensorRead():
    id = 1
    
    messages = []
    message = readI2C(id)
    messages.append(message)
    
    return sorted(messages, key=lambda x: x["VALOR_LIDO"])


#Demonstrando Distancia
"""
- Demonstrando distancia. 
"""
def distancePrint(value_read):
    print('Distancia: ', value_read, ' Metros')

