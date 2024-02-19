from sensors.LightSensor import lightSensorRead, activateIlluminator
from sensors.BatterySensor import batterySensorRead, operationalBatteryLevel
from sensors.DistanceSensor import distanceSensorRead
from sensors.GPSPositionSensor import gpsPositionRead

import threading
import time

def main():
    
    #Leitura do sensor de luminosidade e gerenciamento da ativação do iluminador;
    array_messages_light = lightSensorRead()
    for message in array_messages_light:
        activateIlluminator(message["VALOR_LIDO"])

    #Leitura do sensor de distancia
    array_messages_distance = distanceSensorRead()
    for message in array_messages_distance:
        print('Distancia: ', message["VALOR_LIDO"], ' Metros')

    #Leitura do nível da bateria e gerenciamento do nível de sistema operacional;
    array_messages_battery = batterySensorRead()
    for mensagem in array_messages_battery:
        if operationalBatteryLevel(mensagem["VALOR_LIDO"]):
            break

    gpsPositionRead()


if __name__ == "__main__":
    main()
