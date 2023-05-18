import machine
from machine import Pin, ADC
import network
#import wifi_credentials
import time
import urequests


#------------------------------ DEFINICAO DOS PINOS NO SENSOR --------------------------------
# 36 == vp liga no S (perto do 3v3)
# + liga no 3v3
# - liga gnd
adc = ADC(Pin(36))

# ----------------------------- CONEXAO WIFI -------------------------------------------------
wlan = network.WLAN(network.STA_IF)

#reiniciar wifi
wlan.active(False)
time.sleep(0.5)
wlan.active(True)


networks = wlan.scan()
print(networks)

ssid = ''
password = ''
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


#----------------------------------- CONSTANTES E VARIAVEIS ------------------------------------------
HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = '' 
UPDATE_TIME_INTERVAL = 2500  # in ms 
last_update = time.ticks_ms()

# --------------------------------------------------------------------------------------------
def fazer_request(leituraSensor, campo2, campo3):
    sensor_readings = {"field1":leituraSensor, "field2":campo2, "field3":campo3} 
    print(sensor_readings)
    request = urequests.get( 
        'http://api.thingspeak.com/update?api_key=' +
          THINGSPEAK_WRITE_API_KEY, 
          json = sensor_readings, 
          headers = HTTP_HEADERS)
    time.sleep(2)
    request = urequests.get( 
        'http://api.thingspeak.com/update?api_key=' +
          THINGSPEAK_WRITE_API_KEY, 
          json = sensor_readings, 
          headers = HTTP_HEADERS)
    print(request.status_code)
    
    request.close()
        

# Main loop:
campo1 = 0
campo2 = 0
campo3 = 0

leituraSensorControle = 404

while True: 
    if time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL: 
        #time.sleep(10)
        leituraSensor = adc.read()
        print(leituraSensor)
        campo2 = campo2 + 1
        
        if leituraSensor != leituraSensorControle:
            leituraSensorControle = leituraSensor
            fazer_request(leituraSensor, campo2, campo3)
        
        
        last_update = time.ticks_ms()



