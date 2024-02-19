from drivers.I2C.I2C_Read import readI2C
import random

#Leitura do sensor de luminosidade
"""
- Leitura 0 é ausência de luz e 100 luz intensa;
- Leitura ordenada de forma crescente;  
"""
def lightSensorRead():
    id = 0
    
    messages = []
    message = readI2C(id)
    messages.append(message)
    
    return sorted(messages, key=lambda x: x["VALOR_LIDO"])


#Acionamento do iluminador
"""
- Acionamento do iluminador em caso de leitura inferior a 40; 
"""
def activateIlluminator(value_read):
    if value_read < 40:
        print("Leitura:", value_read, "Iluminador ATIVADO")
    else:
        print("Leitura:", value_read, "Iluminador DESATIVADO")

