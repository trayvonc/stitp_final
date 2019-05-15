#import pyodbc
#from program.logfile import logger
import pymysql

def get_Post():
    cnxn = pymysql.connect(host="localhost", user="root",password="123456", db="roll", port=3306)
    cur = cnxn.cursor()
    select = "Select fenci from roll"
    cur.execute(select)
    row=cur.fetchall()
    #row = cur.fetchone()
    if row:
        return row
    else:
        # raise Exception, "There seems no operator on sector:" + str(sectorNumber)
        print("There seems no Post")
    cnxn.close()

#for rows in get_Post():
    #print(rows)
