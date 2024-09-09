from machine import Pin, Timer, PWM
import time
stop = Pin(12,Pin.IN,Pin.PULL_UP)
led = Pin ("LED",Pin.OUT)
# pwm = PWM ( Pin ( 7 ) ) # GP9
# pwm. freq ( 1000 ) # 1kHz
pwm = Pin(8,Pin.OUT)
timer = Timer(-1)
def turnoff(t):
    led.off()
def turnon(t):
    led.on()
    timer.init(mode=Timer.ONE_SHOT,period=1000,callback=turnoff)
while True:
    print (stop.value())
#     pwm. duty_u16 (int(0) if stop.value()==0 else int(32000) ) # duty 50% (65535/2)
    if not stop.value():
        
        timer.init(mode=Timer.ONE_SHOT, period=100,callback=turnon)
    
