import serial
import time

# Abrir conexão serial com o modem GPRS
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)

# Lista de comandos AT para estabelecer a conexão GPRS
commands = [
    'ATE1\r\n',
    'AT+COPS=2\r\n',
    'AT+COPS=0\r\n',
    'AT+CGDCONT=1,"IP","tim.com.br","",0,0\r\n'
]

def send_at_command(command):
    ser.write(command.encode())
    time.sleep(1)  # Aguarda a resposta
    response = ser.read(ser.inWaiting()).decode()  # Lê a resposta
    return response

# Envia os comandos e verifica as respostas
for cmd in commands:
    response = send_at_command(cmd)
    if "OK" in response:
        print(f"Comando {cmd.strip()} executado com sucesso.")
    else:
        print(f"Erro ao executar o comando {cmd.strip()}. Resposta: {response}")
        break  # Interrompe o processo se um comando falhar

ser.close()  # Fecha a conexão serial
