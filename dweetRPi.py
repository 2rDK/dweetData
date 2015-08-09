#!/usr/bin/python
from fcn.readSensors import readRPiCPUTemp
from fcn.readCPULoad import readCPULoad
from fcn.dweetTools import dweetSender
#from fcn.mySqlTools import mySqlSender
import fcn.HTU21D


myKeys = {
          'CPU_temp': readRPiCPUTemp(), 
          'CPU_load': readCPULoad(),
          'Loft_temp': HTU21D.read_temperature()
          }

myName = "HusetIO_RPi"

print(dweetSender(myName,myKeys))

#mySqlSender("CPU_temp",15,1)

    
