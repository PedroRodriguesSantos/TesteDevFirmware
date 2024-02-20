from drivers.I2C.I2C_Read import readI2C
from counterTimer.CounterTimer import counterTimerProcess, max_timer_sensors
import random
import time

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



def routineLightSensor():

    timer_routine_light_sensor = counterTimerProcess(0)
    if timer_routine_light_sensor > max_timer_sensors:  # A cada 5 segundos    
        array_messages_light = lightSensorRead()
        for message in array_messages_light:
            activateIlluminator(message["VALOR_LIDO"])
        timer_routine_light_sensor = 0
        
    