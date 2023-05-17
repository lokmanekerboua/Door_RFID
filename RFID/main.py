import cayenne.client  # Cayenne MQTT Client
import serial

# Configure the serial connection
ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the appropriate port name
ser.timeout = 1  # Set a timeout value for reading from the serial port
# Cayenne authentication details
MQTT_USERNAME = "YOUR_CAYENNE_MQTT_USERNAME"
MQTT_PASSWORD = "YOUR_CAYENNE_MQTT_PASSWORD"
MQTT_CLIENT_ID = "YOUR_CAYENNE_MQTT_CLIENT_ID"

client = cayenne.client.CayenneMQTTClient()

client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)


def SendData(msg):
    client.virtualWrite(3, msg)  # Publish msg to Cayenne MQTT Broker Channel 3
    print("send success")


# while True:
#     client.loop()


try:
    while True:
        # Read data from the serial port
        line = ser.readline().decode().strip()
        client.loop()

        # Process and display the received data
        if line:
            print(line)
            if line=="Authorized":
                SendData(1)
            else:
                SendData(0)

except KeyboardInterrupt:
    pass

# Close the serial port
ser.close()