import subprocess
import sys
def readFitPCCPUTemp():
    try:
        proc = subprocess.Popen("sensors -u coretemp-isa-0000", stdout=subprocess.PIPE, shell=True)
        sensorsOutput = str(proc.stdout.read())
        needleLocation = sensorsOutput.find("temp2_input")
        cputemp = float(sensorsOutput[needleLocation+13:needleLocation+19])
    except:
        cputemp=-1
    
    return cputemp

def readRPiCPUTemp():
    try:
        proc = subprocess.Popen("/opt/vc/bin/vcgencmd measure_temp", stdout=subprocess.PIPE, shell=True)
        sensorsOutput = str(proc.stdout.read())
        cputemp = float(sensorsOutput[5:9])
    except:
        print("Unexpected error:", sys.exc_info()[0])
        cputemp=-1
    
    return cputemp