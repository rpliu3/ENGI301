#!/usr/bin/env python

"""
--------------------------------------------------------------------------
Lights test for Multi-fandom Kpop light display with music
--------------------------------------------------------------------------
License:   
Copyright 2019 Rebecca Liu

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------
Software API:

  * opc.client ensures that server is running so that LED string can be displayed
  
--------------------------------------------------------------------------
Background Information: 
 
   * Base code for LED functions came from the following repositories:
        https://markayoder.github.io/PRUCookbook/01case/case.html#_neopixels_5050_rgb_leds_with_integrated_drivers_ledscape
        https://markayoder.github.io/PRUCookbook/06io/io.html#io_uio
        https://github.com/Yona-Appletree/LEDscape.git
        https://github.com/zestyping/openpixelcontrol

"""

import time
import opc
import Adafruit_BBIO.GPIO as GPIO

BUTTONC                      = "P2_24" #blue stop button
BUTTONK                      = "P2_22" #black button
BUTTONY                      = "P2_20" #yellow button
BUTTONG                      = "P2_18" #green button
BUTTONR                      = "P2_19" #red button
BUTTONB                      = "P2_17" #blue button

ADDRESS = 'localhost:7890'

# Create a client object
client = opc.Client(ADDRESS)

# Test if it can connect
if client.can_connect():
    print ('connected to %s' % ADDRESS)
else:
    # We could exit here, but instead let's just print a warning
    # and then keep trying to send pixels in case the server
    # appears later
    print ('WARNING: could not connect to %s' % ADDRESS)
    
def setup():
    """Setup the hardware components."""

    # Initialize Buttons
    GPIO.setup(BUTTONK,GPIO.IN)
    GPIO.setup(BUTTONY,GPIO.IN)
    GPIO.setup(BUTTONG,GPIO.IN)
    GPIO.setup(BUTTONR,GPIO.IN)
    GPIO.setup(BUTTONB,GPIO.IN)
    GPIO.setup(BUTTONC,GPIO.IN)

# Send pixels forever
STR_LEN=240
for i in range(STR_LEN):
    leds = [(0, 0, 0)] * STR_LEN

#uses each light's address to set display to a design
def task():
    while True:

        if(GPIO.input(BUTTONB) == 0):
            for i in range(7,31):
                leds[i] = (0,128,255)
            for i in range(215,239):
                leds[i] = (0,128,255)
            for i in [7,31,33,57,59,83,85,109,111,135,137,161,163,187,189,213,215,239]:
                leds[i] = (0,128,255)
            for i in [145,180,181,142,130,90,77,76,93,178,146,126,94,74,125,176,148,124,96,72,175,149,123,97,71,174,173,122,70,69,172,152,120,100,68,153,118,103,64,104,116,156,168]:
                leds[i] = (0,128,255)
        
            if client.put_pixels(leds, channel=0):
                pass
                #print ('sent')
            else:
                print ('not connected')
            time.sleep(0.1)
            
        elif(GPIO.input(BUTTONR) == 0):
            for i in range(7,31):
                leds[i] = (255,0,0)
            for i in range(215,239):
                leds[i] = (255,0,0)
            for i in [7,31,33,57,59,83,85,109,111,135,137,161,163,187,189,213,215,239]:
                leds[i] = (255,0,0)
            for i in [185,139,133,87,81,184,141,132,89,80,182,142,130,90,78,179,180,143,129,91,76,75,93,127,128,178,146,126,94,74,177,148,125,96,73,149,123,97,71,174,151,121,99,69,122,172,152,120,100,68,153,102,65,103,117,155,169,166,167,156,116,104,63,62,106,114,115]:
                leds[i] = (255,0,0)
                
            if client.put_pixels(leds, channel=0):
                pass
                #print ('sent')
            else:
                print ('not connected')
            time.sleep(0.1)
        
        elif(GPIO.input(BUTTONG) == 0):
            for i in range(7,31):
                leds[i] = (0,255,0)
            for i in range(215,239):
                leds[i] = (0,255,0)
            for i in [7,31,33,57,59,83,85,109,111,135,137,161,163,187,189,213,215,239]:
                leds[i] = (0,255,0)
            for i in [182,142,130,90,78,143,128,93,74,94,126,146,178,150,175,176,147,125,95,72,71,98,173,172,171,170,169,153,119,101,67]:
                leds[i] = (0,255,0)
                
            if client.put_pixels(leds, channel=0):
                pass
                #print ('sent')
            else:
                print ('not connected')
            time.sleep(0.1)
            
        elif(GPIO.input(BUTTONY) == 0):
            for i in range(7,31):
                leds[i] = (255,255,0)
            for i in range(215,239):
                leds[i] = (255,255,0)
            for i in [7,31,33,57,59,83,85,109,111,135,137,161,163,187,189,213,215,239]:
                leds[i] = (255,255,0)
            for i in [185,139,133,87,81,184,140,132,88,80,141,90,77,91,129,143,181,180,144,128,92,76,179,178,127,177,147,125,95,73,176,148,124,96,72,149,98,69,99,121,151,173,172,152,120,100,68,171,170,169,154,118,102,66,168,156,116,104,64,167,166,115,63,62]:
                leds[i] = (255,255,0)
                
            if client.put_pixels(leds, channel=0):
                pass
                #print ('sent')
            else:
                print ('not connected')
            time.sleep(0.1)
        
        elif(GPIO.input(BUTTONK) == 0):
            for i in range(7,31):
                leds[i] = (255,255,255)
            for i in range(215,239):
                leds[i] = (255,255,255)
            for i in [7,31,33,57,59,83,85,109,111,135,137,161,163,187,189,213,215,239]:
                leds[i] = (255,255,255)
            for i in [182,142,130,90,78,181,180,179,129,128,77,76,75,177,148,123,98,69,73,96,150,173,171,170,169,168,156,116,104,64,65,66,67,101,119,153]:
                leds[i] = (255,255,255)
                
            if client.put_pixels(leds, channel=0):
                pass
                #print ('sent')
            else:
                print ('not connected')
            time.sleep(0.1)
                
        elif(GPIO.input(BUTTONC) == 0):
            for i in range(0,240):
                leds[i] = (0,0,0)
          
            if client.put_pixels(leds, channel=0):
                pass
                #print ('sent')
            else:
                print ('not connected')
            time.sleep(0.1)
            
        
if __name__ == '__main__':
    setup()
    
    try:
        task()
    except KeyboardInterrupt:
        pass

    print("Program Complete.")        