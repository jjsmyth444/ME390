import RPi.GPIO as GPIO
import smbus
import time

address = 0x48
bus=smbus.SMBus(1)
cmd=0x40

def analogRead(chn):
    value = bus.read_byte_data(address,cmd+chn)
    return value
    
def analogWrite(value):
    bus.write_byte_data(address,cmd,value)  

def loop():
    while True:
        value = analogRead(0)
        print ('ADC Value : %d'%(value))
        time.sleep(0.1)

def destroy():
    bus.close()
    GPIO.cleanup()
    
if __name__ == '__main__':
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()