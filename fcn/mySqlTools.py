import _mysql
import configparser
config = configparser.ConfigParser()
config.read('fcn/settings.ini')



def mySqlSender(myTag, myValue, unit):
    
    db=_mysql.connect(host=config['MySQL']['Host'],user=config['MySQL']['User'],passwd=config['MySQL']['Pass'],db=config['MySQL']['db'])

    #Lav iteration her !

    db.query("INSERT INTO `Analog` (`device_id`, `tag`, `value`, `unit`) VALUES ('"+str(config['Device']['ID'])+"', '"+str(myTag)+"', '"+str(myValue)+"', '"+str(unit)+"')")
 
    db.close()

