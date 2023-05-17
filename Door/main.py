import cayenne.client
import serial

MQTT_USERNAME = "YOUR_CAYENNE_MQTT_USERNAME"
MQTT_PASSWORD = "YOUR_CAYENNE_MQTT_PASSWORD"
MQTT_CLIENT_ID = "YOUR_CAYENNE_MQTT_CLIENT_ID"

ser = serial.Serial('COM3', 9600)

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)


def on_message(message):
    dic_message = vars(message).get('value')
    print("message received: " + str(dic_message))
    ser.write(dic_message.encode())


client.on_message = on_message

client.loop_forever()
