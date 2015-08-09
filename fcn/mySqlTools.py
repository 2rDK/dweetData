import _mysql
import configparser
config = configparser.ConfigParser()
config.read('fcn/settings.ini')



def mySqlSenderAnalog(myKeys, unit):
    
    db=_mysql.connect(host=config['MySQL']['Host'],user=config['MySQL']['User'],passwd=config['MySQL']['Pass'],db=config['MySQL']['db'])

    for key, value in myKeys.items():
        db.query("INSERT INTO `Analog` (`device_id`, `tag`, `value`, `unit`) VALUES ('"+str(config['Device']['ID'])+"', '"+str(key)+"', '"+str(value)+"', '"+str(unit)+"')")
 
    db.close()

