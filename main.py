from machine import Pin
import time


try:
    tx_pin = Pin(13, Pin.OUT)
    print("aqui 1")
except Exception as e:
    print("Erro ao configurar o pino GPIO:", e)
    

def send_signal():
    try:
        if tx_pin is not None:  # Garante que tx_pin foi configurado corretamente
            for _ in range(10):  # Envia um pulso 10 vezes
                tx_pin.value(1)
                time.sleep(0.001)  # Pequeno delay (1ms)
                tx_pin.value(0)
                time.sleep(0.001)
                print("aqui 3")
        else:
            print("Pino não foi inicializado corretamente. Ignorando envio de sinal.")
    except Exception as e:
        print("Erro ao enviar sinal:", e)

while True:
    try:
        send_signal()
        time.sleep(2)  # Espera 2 segundos antes de enviar novamente
        print("aqui 3")
    except Exception as e:
        print("Erro no loop principal:", e)