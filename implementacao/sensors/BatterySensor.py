from drivers.I2C.I2C_Read import readI2C

#Leitura do sensor de bateria
"""
- Leitura 0V a 25V;
- Leitura ordenada de forma crescente;
"""
def batterySensorRead():
    id = 1

    messages = []
    message = readI2C(id)
    messages.append(message)
    
    return sorted(messages, key=lambda x: x["VALOR_LIDO"])


#Segurança de operação com o nível de bateria
"""
- Desligamento do sistema, em caso de bateria com nível inferior a 10V;
"""
def operationalBatteryLevel(value_read):

    if value_read < 10:
        print(f"Leitura de bateria: {value_read}V - Sistema desligando")
        return True
    else:
        print(f"Leitura de bateria: {value_read}V - Sistema operacional")
        return False


