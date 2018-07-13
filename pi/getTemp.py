import os
import requests
import config

gpioContents = os.listdir("/sys/bus/w1/devices")

for content in gpioContents:
    if "28-" in content:
        file = open("/sys/bus/w1/devices/" + content + "/w1_slave", "r").read()
        tempInC = int(file.split("t=")[1].strip()) / 1000
        print(tempInC)
        response = requests.post(config.url + "/piTemperatureInput",
                                 data={
                                     "C": tempInC,
                                     "thermometer_id": content,
                                     "secret": config.secret})
        print(response)

