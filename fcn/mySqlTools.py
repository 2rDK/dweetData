import MySQLdb
import configparser
config = configparser.ConfigParser()
config.read('/home/pi/Documents/dweetData/fcn/settings.ini')



def mySqlSenderAnalog(myKeys, unit):
    try:
        db=MySQLdb.connect(config['MySQL']['Host'],config['MySQL']['User'],config['MySQL']['Pass'],config['MySQL']['db'])
        c=db.cursor()
    
        for key, value in myKeys.items():
            c.execute("INSERT INTO `Analog` (`device_id`, `tag`, `value`, `unit`) VALUES ('"+str(config['Device']['ID'])+"', '"+str(key)+"', '"+str(value)+"', '"+str(unit)+"')")
        
        db.commit()
     
    except MySQLdb.Error as e:
  
        print("Error %d: %s" % (e.args[0],e.args[1]))

    
    finally:    
        
        if db:    
            db.close()