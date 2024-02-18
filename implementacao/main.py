from sensors.LightSensor import LightSensorRead, ActivateIlluminator
from sensors.BatterySensor import batterySensorRead, operationalBatteryLevel

import threading
import time

def main():
    
    #Leitura do sensor de luminosidade e gerenciamento da ativação do iluminador;
    array_messages_light = LightSensorRead()
    for message in array_messages_light:
        ActivateIlluminator(message["VALOR_LIDO"])

    #Leitura do nível da bateria e gerenciamento do nível de sistema operacional;
    array_messages_battery = batterySensorRead()
    for mensagem in array_messages_battery:
        if operationalBatteryLevel(mensagem["VALOR_LIDO"]):
            break




if __name__ == "__main__":
    main()
