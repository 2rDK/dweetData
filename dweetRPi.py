#!/usr/bin/python
import requests
from fcn.readSensors import readRPiCPUTemp
from fcn.readCPULoad import readCPULoad

myKey1 = "RPi_CPU_temp"
myKey2 = "RPi_CPU_load"
myName = "HusetIO"
dweetIO = "https://dweet.io/dweet/for/"

temp = readRPiCPUTemp()
loadCPU = readCPULoad()
rqsString = dweetIO + myName + '?' + myKey1 + '=' + str(temp) + '&' + myKey2 + '=' + str(loadCPU)

print(rqsString)

rqs = requests.get(rqsString)

print(rqs.status_code)
