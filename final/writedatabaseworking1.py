#!/Program Files (x86)/Python37-32/python
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
import time
import datetime
import glob
from time import strftime
import pandas as pd
import numpy as np

cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print()
print("Hello World!")

"""import sys
print(sys.version)"""   


def ejecutaScript():
    
    print ('Ejecutando Script...')



    import pymysql
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='dataarduino')
    cur = conn.cursor()
    cur.execute("SELECT * FROM data")



    print(cur.description)
    print()





    #for row in cur:
    #    print(row)


     # Agregar una fruta en nuestra base de datos:
    #Date='2019-01-25'
    #Time='21:18:13'
    #Value='27'

    # Ejecutar sentencia:






    colnames = ['RSSI1','RSSI2']
    data = pd.read_csv('positions.csv', names=colnames)
    df=pd.DataFrame(data)

    i=df.shape[0] #Obtiene el número de filas,
    # si se cambia por 1 se obtiene el número de columnas

    #print(i)

    element=df.iloc[i-1] #obtiene propiedades de df
    #print(element)
    RSSI1final=element.RSSI1
    RSSI2final=element.RSSI2
    print(RSSI1final)
    print(RSSI2final)
    #import sys
    #print(sys.version)






    dateWrite = time.strftime('%Y-%m-%d')
    timeWrite = time.strftime('%H:%M:%S')





    print(RSSI1final)
    print(RSSI2final)



    print(type(float(RSSI1final)))
    print(type(float(RSSI2final)))
    print(type(timeWrite))

    RSSI1final=float(RSSI1final)
    RSSI2final=float(RSSI2final)


    cur.execute("INSERT INTO `data` (`Time`, `RSSI1`, `RSSI2`, `RSSI3`, `PULSOMELCHOR`, `PULSOCINTHIA`, `VELOCIDAD`, `ACELERACION`, `TEMPERATURA`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",('13',RSSI1final,RSSI2final,'13','13','13','13','13','13'))

    conn.commit()



    # Cerrar cursor
    cur.close()

    # Cerrar conexion
    conn.close()

    time.sleep(10)


while True:
    ejecutaScript()
