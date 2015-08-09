#!/usr/bin/python3
from fcn.readSensors import readRPiCPUTemp
from fcn.readCPULoad import readCPULoad
from fcn.dweetTools import dweetSender
#from fcn.mySqlTools import mySqlSender
from fcn.HTU21D import HTU21D

obj = HTU21D()
myKeys = {
          'CPU_temp': readRPiCPUTemp(), 
          'CPU_load': readCPULoad(),
          'Loft_temp': round(obj.read_temperature(),2),
          'Loft_hum': round(obj.read_humidity(),2)
          }

myName = "HusetIO_RPi"

print(dweetSender(myName,myKeys))

#mySqlSender("CPU_temp",15,1)

    
