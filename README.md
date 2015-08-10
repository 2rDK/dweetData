# dweetData
Send various data to Dweet.io and MySQL

#Install
## RPi
### Requirements
The Raspberry Pi must support Python 3.4. This means it must either be updated from Wheezy to Jessie or Python3.4 must be compiled from source.
If not, the MySQLdb module will fail due to incompability with Python3.2 (Wheezy standard)
### Procedure
1. First install PIP
```
apt-get install python3-pip
```
2. Install requests:
```
pip3 install requests
```
3. Install support for mysql:
```
apt-get install libmysqlclient-dev
apt-get install python-dev
pip3 install mysqlclient
```
4. Make suitable folder for the project, e.g.:
```
mkdir Documents/dweetData
```
5. Use **git** to initialize folder and download repository form GitHub
```
cd Documents/dweetData
git init
git pull <URL>
```
## Credits
i2c_base.py is shamelessly borrowed from https://github.com/raspberrypi/weather-station/