from machine import Pin
import time

# Configuração dos pinos
try:
    tx_pin = Pin(13, Pin.OUT)  # Pino do transmissor (TX)
    rx_pin = Pin(15, Pin.IN, Pin.PULL_DOWN)  # Pino do receptor (RX) com pull-up
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
                time.sleep(0.001)
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
            print("Lendo sinal RX por 1 segundo...")
            for _ in range(100):  # Lê várias vezes por 1 segundo
                if rx_pin.value() == 1:
                    print("🚀 Sinal recebido!")
                    return
                time.sleep(0.01)  # Pequeno atraso para capturar mudanças no sinal
            print("Nenhum sinal detectado.")
        else:
            print("rx_pin é None")
    except Exception as e:
        print("Erro ao receber sinal:", e)

# Loop principal
while True:
    try:
        send_signal()      # Transmite sinal
        time.sleep(0.1)    # Aguarda um tempo antes de ler RX
        receive_signal()   # Verifica se recebeu o sinal
    except Exception as e:
        print("Erro no loop principal:", e)
