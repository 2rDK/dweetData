#!/usr/bin/python
from fcn.readSensors import readRPiCPUTemp
from fcn.readCPULoad import readCPULoad
from fcn.dweetTools import dweetSender

myKeys = {
          'CPU_temp': readRPiCPUTemp(), 
          'CPU_load': readCPULoad()
          }
myName = "HusetIO_RPi"

print(dweetSender(myName,myKeys))

#print(rqs.status_code)
