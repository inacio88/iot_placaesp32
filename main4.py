import time
import _thread
from machine import Pin

# Configuração dos pinos
tx_pin = Pin(13, Pin.OUT)  # Pino do transmissor (TX)
rx_pin = Pin(15, Pin.IN)   # Pino do receptor (RX)

# Função para enviar o sinal RF
def send_signal():
    while True:
        print("📡 Enviando sinal...")
        for _ in range(10):  # Envia 10 pulsos rápidos
            tx_pin.value(1)
            time.sleep(0.001)  # 1ms ligado
            tx_pin.value(0)
            time.sleep(0.001)  # 1ms desligado
        print("✅ Sinal enviado!")
        time.sleep(2)  # Aguarda antes de enviar novamente

# Função para receber sinal RF
def receive_signal():
    while True:
        if rx_pin.value() == 1:
            print("🚀 Sinal RECEBIDO!")
        else:
            print("❌ Nenhum sinal recebido.")
        time.sleep(0.1)  # Aguarda 100ms antes de verificar novamente

# Criando threads para enviar e receber sinais em paralelo
_thread.start_new_thread(send_signal, ())  # Inicia a thread de envio
_thread.start_new_thread(receive_signal, ())  # Inicia a thread de recepção

# O loop principal não faz nada, pois as threads já estão rodando
while True:
    time.sleep(1)  # O loop principal apenas mantém o código em execução
