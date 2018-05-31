#!/usr/bin/python

import serial
port = '/dev/ttyUSB0'
ser = serial.Serial(port, 9600, timeout=1)
# To open relay (OFF)
code = 'A00100A1'
ser.write(code.decode('HEX'))
ser.close()
