from sensors.LightSensor import lightSensorRead, activateIlluminator, routineLightSensor
from sensors.BatterySensor import batterySensorRead, operationalBatteryLevel
from sensors.DistanceSensor import distanceSensorRead, distancePrint
from sensors.GPSPositionSensor import gpsPositionRead
from counterTimer.CounterTimer import counterTimerProcess

import threading
import time

start_time = time.time()


def main():

    time.sleep(2)

    end_time = time.time() - start_time

    print(end_time)


    """
    teste = 100

    for _ in range(teste):

        counterTimerProcess();

        routineLightSensor();

        print('Teste')
        
        #Leitura do sensor de luminosidade e gerenciamento da ativação do iluminador;
        array_messages_light = lightSensorRead()
        for message in array_messages_light:
            activateIlluminator(message["VALOR_LIDO"])

        #Leitura do sensor de distancia
        array_messages_distance = distanceSensorRead()
        for message in array_messages_distance:
            distancePrint(message["VALOR_LIDO"])

        #Leitura do nível da bateria e gerenciamento do nível de sistema operacional;
        array_messages_battery = batterySensorRead()
        for message in array_messages_battery:
            operationalBatteryLevel(message["VALOR_LIDO"])
            #if operationalBatteryLevel(mensagem["VALOR_LIDO"]):
            #    break

        #Leitura do GPS
        gpsPositionRead()
    """

if __name__ == "__main__":
    main()
