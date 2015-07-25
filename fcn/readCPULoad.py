import subprocess
def readCPULoad():
    try:
        proc = subprocess.Popen("cat /proc/loadavg", stdout=subprocess.PIPE, shell=True)
        loadAvg = str(proc.stdout.read())
        oneMinuteLoad = float(loadAvg[2:6])
    except:
        oneMinuteLoad = -1
    return oneMinuteLoad
