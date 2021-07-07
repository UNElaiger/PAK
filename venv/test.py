import serial
ser = serial.Serial('COM6', baudrate = 115200, timeout=2) #настройка порта
class COMPORTREAD():
    while 1:
        arduinoData=ser.readline().decode('ascii')
        print(arduinoData.replace('\n',''))