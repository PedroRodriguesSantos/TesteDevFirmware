import random

# Array com mensagens NMEA
nmea_messages = [
    "$GPRMC,140602.00,A,2736.12493,S,04834.61709,W,0.234,,010920,,,A*7E",
    "$GPVTG,,,,,,,,,N*30",
    "$GPGGA,140601.00,,,,,0,00,99.99,,,,,,*64",
    "$GPGSV,3,1,10,05,34,266,,07,37,125,,08,14,133,18,09,34,049,33*79",
    "$GPGLL,,,,,140601.00,V,N*48"
]

def gpsPositionRead():
    # Escolhe uma mensagem NMEA aleatoriamente
    message = random.choice(nmea_messages)
    
    # Verifica se a mensagem é do tipo GPRMC
    if message.startswith("$GPRMC"):
        parts = message.split(',')
        latitude = parts[3] + parts[4]
        longitude = parts[5] + parts[6]
        print(f"Latitude: {latitude}, Longitude: {longitude}")

        # Aqui, você pode adicionar o código para enviar esses dados ao servidor

    else:
        print("A mensagem selecionada não contém dados de posição.")