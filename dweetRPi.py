#!/usr/bin/python3
import sys
sys.path.insert(0,"/home/pi/Documents/dweetData-master/fcn")
from fcn.readSensors import readRPiCPUTemp
from fcn.readCPULoad import readCPULoad
from fcn.dweetTools import dweetSender
from fcn.mySqlTools import mySqlSenderAnalog
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

myUnit = 1;

mySqlSenderAnalog(myKeys,myUnit)

#mySqlSender("CPU_temp",15,1)

    
