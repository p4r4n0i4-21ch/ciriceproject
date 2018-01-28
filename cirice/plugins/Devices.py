import paho.mqtt.client as mqtt
import time


def on_log(client, userdata, level, buf):
    print("log: "+buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Usted esta conectado!")
    else:
        print("No se pudo hacer la conexión codigo=",rc)

def on_disconnect(client, userdata, flags, rc=0):
    print("Codigo de resultado de desconexión "+ str(rc))
broker="192.168.43.51"

def on_message(client, userdata, msg):
    topic= msg.topic
    print(topic)
    m_decode=str(msg.payload.decode("utf-8","ignore"))
    print("dato recibido", m_decode)
    if (float(m_decode) < 50):
        client.publish("/itq/koudabit/invernadero/actuacion/led","1")
    else:
        client.publish("/itq/koudabit/invernadero/actuacion/led", "0")

client = mqtt.Client("python1")
client.on_connect=on_connect
client.on_disconnect=on_disconnect
#client.on_log=on_log
client.on_message=on_message
print("Conectando al servidor MQTT = ", broker)

client.connect(broker)
client.subscribe("/itq/koudabit/invernadero/sensado/#")
run = True
while run:
    client.loop()



client.disconnect()