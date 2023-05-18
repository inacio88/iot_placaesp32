from machine import Pin
import time

# Configurar o pino do sensor magnético embutido
hall_sensor_pin = 34
hall_sensor = Pin(hall_sensor_pin, Pin.IN)

while True:
    # Ler o valor do sensor
    valor = hall_sensor.value()

    # Imprimir o valor lido
    print("Valor do sensor:", valor)

    # Aguardar 1 segundo antes de ler novamente
    time.sleep(1)
