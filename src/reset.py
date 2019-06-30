import serial
from time import sleep

sleep(10)
 
ser = serial.Serial("/dev/serial/by-id/usb-Lord_Microstrain_Lord_Inertial_Sensor_0000__6233.40581-if00", 115200, 8)
cmd = bytearray([0x75,0x65,0x01,0x02,0x02,0x7E,0x5D,0x43])

ser.write(cmd)
ser.close()