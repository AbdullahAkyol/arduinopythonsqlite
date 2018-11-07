import serial
import time
import sqlite3

con = sqlite3.connect("arduino1.db")
cursor = con.cursor()

ser = serial.Serial('COM5', 9600, timeout = 1)
time.sleep(3)

numpoints = 3
dataList = [0]*numpoints

def gelenVeri():
    ser.write(b'y')
    arduinoData = ser.readline().decode('ascii')
    print("Arduino Data: "+arduinoData)
    return arduinoData
for i in range(0,10):
    time.sleep(.100)
    for i in range(0, numpoints):
        data = gelenVeri()
        dataList[i] = data
    cursor.execute("CREATE TABLE IF NOT EXISTS degerler(deger1 TEXT, deger2 TEXT, deger3 TEXT)")
    cursor.execute("INSERT INTO degerler VALUES (?, ?, ?)", dataList)
    con.commit()
con.close()

