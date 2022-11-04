"""This module has components that are used for testing tuya's device control and Pulsar massage queue."""
from ast import Interactive
import logging
from tuya_connector import (
    TuyaOpenAPI,
    TuyaOpenPulsar,
    TuyaCloudPulsarTopic,
    TUYA_LOGGER,
)

print("File started!")

ACCESS_ID = "ep8pudh3yw3nsxhacxwn"
ACCESS_KEY = "957bbd2bd22f4284889d1e31a2c816c7"
API_ENDPOINT = "https://openapi.tuyaeu.com"
MQ_ENDPOINT = "wss://mqe.tuyaeu.com:8285/"

print("Running tuya logger")
# Enable debug log
TUYA_LOGGER.setLevel(logging.DEBUG)

print("setting openapi value")
# Init openapi and connect
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()


PLUG1 = "41750342b8f009020932"
# PLUG1 = "bf46f70e749d759f99gtu6"

print("saving device statue")
status = openapi.get("/v1.0/iot-03/devices/{}/status".format(PLUG1))

print("sending command")
commands = {'commands':[{'code': 'switch', 'value': False}]}
openapi.post('/v1.0/iot-03/devices/{}/commands'.format(PLUG1), commands)

# Call any API from Tuya
# device details information
information = openapi.get("/v1.0/iot-03/devices/{}".format(PLUG1))

# Get device functions
functions = openapi.get("/v1.0/iot-03/devices/{}/functions".format(PLUG1))

print("pulsar starts here")

# response = openapi.get("/v1.0/statistics-datas-survey", dict())

# # Init Message Queue
open_pulsar = TuyaOpenPulsar(
    ACCESS_ID, ACCESS_KEY, MQ_ENDPOINT, TuyaCloudPulsarTopic.PROD
)
# # Add Message Queue listener
open_pulsar.add_message_listener(lambda msg: print(f"---\nexample receive: {msg}"))

print("WE Are here now starting")
# # Start Message Queue
open_pulsar.start()

input()
# # Stop Message Queue
open_pulsar.stop()
