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

# helper function for fading - do not touch
def fade(c1, c2):
    diff = (c2[0]-c1[0], c2[1]-c1[1], c2[2]-c1[2])
    diffA = [1 if n==0 else abs(n) for n in diff]
    maxDiff = max(diffA)
    index = diffA.index(maxDiff)
    cFade = list(c1)
    increment = [int(diff[i]/diffA[i]) for i in range(3)]
    for i in range(0, maxDiff):
        for n in range(3):
            if(cFade[n] != c2[n]):
                cFade[n] += increment[n]
        pixels.fill(tuple(cFade))
        pixels.show()
        time.sleep(0.01)  # debounce delay
#end helper function
now = 0

while True:
    if touch.value:
        now=now+1
        if (now == 0):
            pixels.fill(OFF)
            pixels.show()
        if (now == 1):
            fade(OFF,RED)
            fade(RED,PURPLE)
            fade(PURPLE,BLUE)
            fade(BLUE,CYAN)
            fade(CYAN,GREEN)
            fade(GREEN,WHITE)
            fade(WHITE,OFF)
            time.sleep(0.5)
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
    if(now>3):
        now = 0
    time.sleep(0.2)
