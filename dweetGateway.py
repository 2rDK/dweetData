#!/usr/bin/python
import requests
import random
from time import sleep
from readSensors import readSensors
from readCPULoad import readCPULoad

myKey1 = "CPU_temp"
myKey2 = "CPU_load"
myName = "HusetIO"
dweetIO = "https://dweet.io/dweet/for/"

temp = readSensors()
loadCPU = readCPULoad()
rqsString = dweetIO + myName + '?' + myKey1 + '=' + str(temp) + '&' + myKey2 + $

print(rqsString)

rqs = requests.get(rqsString)

print(rqs.status_code)
