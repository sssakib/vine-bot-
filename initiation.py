import RPi.GPIO as gpio
import time

#pin diff
ir_pin=23
 


#setups
gpio.setmode(gpio.BCM)
gpio.setup(ir_pin,gpio.IN)



#function
def ir_code(TRUE):
    if  gpio.input(ir_pin):
        print('there is a fire')
    else:
        print('error no input deteccted')
#main
a=input('press true')
ir_code(a)