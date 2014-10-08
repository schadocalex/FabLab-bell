# -*- coding: utf-8 -*-

from xbee import XBee
import serial
from time import sleep

PORT = '/dev/ttyUSB0'
BAUD_RATE = 57600

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

# Create API object

def message_received(data):
	print(int.from_bytes(data['rssi'], byteorder='little', signed=False))
xbee = XBee(ser, callback=message_received)

# Continuously read or print packets
while True:
	try:
		sleep(0.1)
	except KeyboardInterrupt:
		break

xbee.halt()
ser.close()
