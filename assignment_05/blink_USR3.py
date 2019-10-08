# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
LED blink program / blink_USR3.py
--------------------------------------------------------------------------
Authors: Rebecca Liu (rpl2 [at] rice [dot] edu)
  
Copyright 2019 Rebecca Liu
Reference credits:
BeagleBone IO Python library
Ben Croston, MIT Licensed RPi.GPIO library.
Justin Cooper, Adafruit Industries. BeagleBone IO Python library is released under the MIT License

License: 

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Program that blinks the USR3 LED at 5 Hz

--------------------------------------------------------------------------

import Adafruit_BBIO.GPIO as GPIO
import time

for i in range(4):
    GPIO.setup("USR%d" % i, GPIO.OUT)
    GPIO.output("USR%d" % i, GPIO.LOW) 
    #turns all LEDs off (reset from any previous uses)

while True:
    i=3 #LED 3
    GPIO.output("USR%d" % i, GPIO.HIGH) #turn LED on
    time.sleep(0.1) #time on
    #5 Hz is 5 cycles per second. 
    #If time(1) = 1 second, then each on/off cycle should be 1/5 = 0.2 seconds.
    #The time was split evenly between on and off, so 0.1 seconds for each.
    GPIO.output("USR%d" % i, GPIO.LOW) #turn LED off
    time.sleep(0.1) #time off






