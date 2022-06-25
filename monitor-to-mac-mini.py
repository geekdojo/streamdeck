import serial
ser = serial.Serial('/dev/cu.usbserial-14340',timeout=1,baudrate=19200)
ser.write('sw i06\n')
ser.close()