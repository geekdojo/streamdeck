# Copyright (c) 2018 Acroname Inc. - All Rights Reserved
#
# This file is part of the BrainStem development package.
# See file LICENSE or go to https://acroname.com/software/brainstem-development-kit for full license details.
import serial
import brainstem
#for easy access to error constants
from brainstem.result import Result
import time

# Create USBHub2x4 object and connecting to the first module found
print ('\nCreating USBHub3+ stem and connecting to first module found')
stem = brainstem.stem.USBHub3p()

#Locate and connect to the first object you find on USB
#Easy way: 1=USB, 2=TCPIP
result = stem.discoverAndConnect(brainstem.link.Spec.USB)
#Locate and connect to a specific module (replace you with Your Serial Number (hex))
#result = stem.discoverAndConnect(brainstem.link.Spec.USB, 0x66F4859B)

#Check error
if result == (Result.NO_ERROR):
    stem.usb.setUpstreamMode(1)
    print ('Set USB to work laptop.')
else:
    print ('Could not find a module.\n')



ser = serial.Serial('/dev/cu.usbserial-14340',timeout=1,baudrate=19200)
ser.write('sw i08\n')
ser.close()