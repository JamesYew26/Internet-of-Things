from time import *
from grovepi import *
from paho.mqtt import publish

MQTT_BROKER = "127.0.0.1"
MQTT_TOPIC = "test"

publish.single(MQTT_TOPIC, "Any question?", hostname=MQTT_BROKER)