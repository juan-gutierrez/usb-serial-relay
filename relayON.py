#!/usr/bin/python

import serial
port = '/dev/ttyUSB0'
ser = serial.Serial(port, 9600, timeout=1)
# To close relay (ON)
code = 'A00101A2'
ser.write(code.decode('HEX'))
ser.close()
