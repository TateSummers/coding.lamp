# Write your code here :-)
import time
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull
import touchio

touch_pad = board.A0 # the ~1 pin
touch = touchio.TouchIn(touch_pad)

pixel_pin = board.D2
num_pixels = 12
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)
 
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255,255,255)
OFF = (0,0,0)
ORANGE = (180,20,0)

now = 0

while True:
    if touch.value:
        now=now+1
        print(now)
        if (now == 0):
            pixels.fill(OFF)
            pixels.show()
        if (now == 1):
            COLOR = BLUE
            for i in range(0,12,1):
                pixels[i] = COLOR
                pixels.show()
                time.sleep(0.1)
            if touch.value:
                now = now+1
                break
        if (now == 2):
            COLOR = PURPLE
            for i in range(0,12,1):
                pixels[i] = COLOR
                pixels.show()
                time.sleep(0.1)
            if touch.value:
                now = now+1
                break
        if (now == 3):
            COLOR = RED
            for i in range(0,12,1):
                pixels[i] = COLOR
                pixels.show()
                time.sleep(0.1)
            if touch.value:
                now = now+1
                break
        if (now == 4):
            COLOR = ORANGE
            for i in range(0,12,1):
                pixels[i] = COLOR
                pixels.show()
                time.sleep(0.1)
            if touch.value:
                now = now+1
                break
        if (now == 5):
            COLOR = YELLOW
            for i in range(0,12,1):
                pixels[i] = COLOR
                pixels.show()
                time.sleep(0.1)
            if touch.value:
                now = now+1
                break
        if (now == 6):
            COLOR = WHITE
            for i in range(0,12,1):
                pixels[i] = COLOR
                pixels.show()
                time.sleep(0.1)
            if touc.value:
                now = now+1
                break
    if(now>6):
        now = 0
