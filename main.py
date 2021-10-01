from machine import Pin
import utime as time
import machine
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from dht import DHT11, InvalidChecksum

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

def executeLed():
    led.value(1)
    print("LEd")

i2c = I2C(id=1,scl=Pin(27),sda=Pin(26),freq=100000)
led = Pin(20, Pin.OUT)
led.value(0)

i2c2 = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c2, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
lcd.clear()

while True:
    time.sleep(1)
    
    pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))
    
    lcd.move_to(0,0)
    lcd.putstr("Temper. : {}".format(sensor.temperature)+ chr(223)+"C")
    lcd.move_to(0,1)
    lcd.putstr("Humidade: {}%".format(sensor.humidity))  
    
    
    if(t>30):
        executeLed()
    elif(h>80):
        executeLed()
    else:
        led.value(0)
    time.sleep(1)
   




