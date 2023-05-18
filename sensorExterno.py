from machine import Pin, ADC
import time

# Configurar o pino ADC
adc = ADC(Pin(36))

while True:
    # Ler o valor do pino ADC
    valor = adc.read()

    # Imprimir o valor lido
    print("Valor do sensor:", valor)

    # Aguardar 1 segundo antes de ler novamente
    time.sleep(1)
