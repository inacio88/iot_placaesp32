import machine
import network
#import wifi_credentials
import time
import urequests


# ----------------------------- CONEXAO WIFI -------------------------------------------------
wlan = network.WLAN(network.STA_IF)

#reiniciar wifi
wlan.active(False)
time.sleep(0.5)
wlan.active(True)


networks = wlan.scan()
print(networks)

ssid = 'nome'
password = 'senha'
wlan.connect(ssid, password)

timeout = 0

# Esperar a conexão
if not wlan.isconnected():
    print('Conectando...')
    while (not wlan.isconnected() and timeout < 30):
        print(30 - timeout)
        timeout = timeout + 1
        time.sleep(1)
    
    
if wlan.isconnected():
    print('conectado')
    print(wlan.ifconfig())
    
else:
    print('Timeout')


if wlan.isconnected():
    print('conectado')
    print(wlan.ifconfig())
    req = urequests.get('http://jsonplaceholder.typicode.com/albums/1')
    print(req.status_code)
    print(req.text)
else:
    print('Timeout')


