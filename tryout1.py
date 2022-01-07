import RPi.GPIO as gpio
import time

#pin diff
ir_pin=23
sonar_pin=24
trig =25 
echo=18


#variable diffine


#sonar varible
b=1


#setups
gpio.setmode(gpio.BCM)
gpio.setup(ir_pin,gpio.IN)
gpio.setup(sonar_pin,gpio.IN)
gpio.setup(trig,gpio.OUT)
gpio.setup(echo,gpio.IN)

#function for motor and pumps


#function of distance sensory unit
def sonar():
    gpio.output(trig,HIGH)
    delay(100)
    gpio.input(echo)
    print(echo)
    #if echo =100:
        



#function of flame sensory unit 
def ir_code(TRUE):
    if  gpio.input(ir_pin):
        print('there is a fire')
        b=1
        return(b)
    else:
        print('error no input deteccted')
        b=0
        return(b)
#main
a=input('press true')
ir_code(a)
if b==0:
    sonar()
