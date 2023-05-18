import machine
from machine import Pin, ADC
import network
#import wifi_credentials
import time
import urequests
import utime
import ntptime


#------------------------------ DEFINICAO DOS PINOS NO SENSOR --------------------------------
# 36 == vp liga no S (perto do 3v3)
# + liga no 3v3
# - liga gnd
adc = ADC(Pin(36))

#----------------------------------- CONSTANTES E VARIAVEIS ------------------------------------------
HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = '' 
UPDATE_TIME_INTERVAL = 2000  # in ms 
last_update = time.ticks_ms()

# ----------------------------- CONEXAO WIFI -------------------------------------------------

def conectar_wifi():

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

# --------------------------------------------------------------------------------------------
def hora_local():
    ntptime.settime()

    # Obter a data e a hora atual
    timestamp = utime.time()
    data_hora = utime.localtime(timestamp)
    ano, mes, dia, hora, minuto, segundo, dia_da_semana, dia_do_ano = data_hora
    data_str = "{:02d}/{:02d}/{:04d}".format(dia, mes, ano)
    hora_str = "{:02d}:{:02d}:{:02d}".format(hora-3, minuto, segundo)
    data_hora = data_str + " " + hora_str
    
    return data_hora

# --------------------------------------------------------------------------------------------
def fazer_request(leituraSensor, campo2, campo3):
    campo2 = hora_local()
    sensor_readings = {"field1":leituraSensor, "field2":campo2, "field3":campo3} 
    print(sensor_readings)
    request = urequests.get( 
        'http://api.thingspeak.com/update?api_key=' +
          THINGSPEAK_WRITE_API_KEY, 
          json = sensor_readings, 
          headers = HTTP_HEADERS)
    print('primeiro')
    print(request.status_code)
    
    time.sleep(2)
    
    request = urequests.get( 
        'http://api.thingspeak.com/update?api_key=' +
          THINGSPEAK_WRITE_API_KEY, 
          json = sensor_readings, 
          headers = HTTP_HEADERS)
    print('segundo')
    print(request.status_code)
    
    request.close()
    
        

try:
    conectar_wifi()

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
            
            
            if leituraSensor != leituraSensorControle:
                leituraSensorControle = leituraSensor
                fazer_request(leituraSensor, campo2, campo3)
            
            
            last_update = time.ticks_ms()

except Exception as e:
    print("Ocorreu um erro:", e)
    print("Reiniciando...")
    fazer_request(0, 0, 505)
    machine.reset()
