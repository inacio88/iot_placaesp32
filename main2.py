from machine import Pin
import time

# Configuração dos pinos
try:
    tx_pin = Pin(13, Pin.OUT)  # Pino do transmissor (TX)
    rx_pin = Pin(15, Pin.IN)   # Pino do receptor (RX)
    print("Pinos configurados corretamente.")
except Exception as e:
    print("Erro ao configurar os pinos GPIO:", e)

# Função para enviar o sinal RF
def send_signal():
    try:
        if tx_pin is not None:
            print("Enviando sinal...")
            for _ in range(10):  # Envia um pulso 10 vezes
                tx_pin.value(1)
                time.sleep(0.001)  # Pequeno delay (1ms)
                tx_pin.value(0)
                time.sleep(0.001)
            print("Sinal enviado!")
        else:
            print("Erro: Pino TX não inicializado.")
    except Exception as e:
        print("Erro ao enviar sinal:", e)

# Função para receber sinal RF
def receive_signal():
    try:
        if rx_pin is not None:
            if rx_pin.value() == 1:
                print("🚀 Sinal recebido no RX!")
    except Exception as e:
        print("Erro ao receber sinal:", e)

# Loop principal
while True:
    try:
        send_signal()     # Transmite sinal
        time.sleep(2)     # Aguarda 2 segundos
        receive_signal()  # Verifica se recebeu o sinal
    except Exception as e:
        print("Erro no loop principal:", e)
