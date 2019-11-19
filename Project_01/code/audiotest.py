"""
--------------------------------------------------------------------------
Audio test for Multi-fandom Kpop light display with music
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

  * play_song(song)
      - Plays song(s) through USB audio connected speakers. Media format must be in mp3. Multiple songs must be in a list. 
  * mpg123 -() filename.mp3
      - command line audio player that can take in individual song files in mp3 format or multiple audio files at once in a list
  
--------------------------------------------------------------------------
Background Information: 
 
  * Uses USB audio adapter and push button controls. Plays stored mp3 files that are downloaded onto PocketBeagle.
    
    * Key functions used:
        - glob - returns an array of files by identifying a pattern that can be used to match multiple files 
          (i.e. * or ?, etc) in the specified path
        - subprocess - creates a new process and allows for running of terminal commands
        - mpg123 - command line audio player that is compatible with mp3 files. 
          Has several variable arguments which can be appended with the command for different effects and control
          https://linux.die.net/man/1/mpg123 provides all of the possible extensions that can be used with mpg123

"""

#!/usr/bin/env python
import time
from glob import glob
import subprocess
import Adafruit_BBIO.GPIO as GPIO

# ------------------------------------------------------------------------
# Constants: map buttons to their pins on PocketBeagle
# ------------------------------------------------------------------------

BUTTONC                      = "P2_24" #blue stop button
BUTTONK                      = "P2_22" #black button
BUTTONY                      = "P2_20" #yellow button
BUTTONG                      = "P2_18" #green button
BUTTONR                      = "P2_19" #red button
BUTTONB                      = "P2_17" #blue button

process                      = None    #set value for process variable

def play_song(song):
    """Play selected set of songs"""
    global process
    
    #if something is playing, kill the process (i.e. stop the music) so that new process (i.e. play new set of songs) can be started
    if not process == None:
        process.kill()
    
    #set slight delay to decrease sound distortion
    time.sleep(1)
    #define process: mpg123 -Z used to play songs in a playlist continuously at random, subprocess creates new process for mpg123
    process = subprocess.Popen(['/usr/bin/mpg123','-Z'] + glob(song))

#end def

def setup():
    """Setup the hardware components."""

    # Initialize Buttons
    GPIO.setup(BUTTONK,GPIO.IN)
    GPIO.setup(BUTTONY,GPIO.IN)
    GPIO.setup(BUTTONG,GPIO.IN)
    GPIO.setup(BUTTONR,GPIO.IN)
    GPIO.setup(BUTTONB,GPIO.IN)
    GPIO.setup(BUTTONC,GPIO.IN)
    
#end def

def task():
    """Execute the main program."""
    while(1):
        
        # Wait for button press
        if(GPIO.input(BUTTONK) == 0):
            #call function to play the songs in this playlist
            play_song('/var/lib/cloud9/ENGI301/Project1/EXO/*.mp3')
            #NOTE: the path for the playlist MUST be correct and complete otherwise program will not be able to find variable 'song' for function play_song

        # Wait for button press
        elif(GPIO.input(BUTTONY) == 0):
            #call function to play the songs in this playlist
            play_song('/var/lib/cloud9/ENGI301/Project1/Infinite/*.mp3')
            
         # Wait for button press
        elif(GPIO.input(BUTTONG) == 0):
            #call function to play the songs in this playlist
            play_song('/var/lib/cloud9/ENGI301/Project1/NCT/*.mp3')
            
         # Wait for button press
        elif(GPIO.input(BUTTONR) == 0):
            #call function to play the songs in this playlist
            play_song('/var/lib/cloud9/ENGI301/Project1/BigBang/*.mp3')
            
         # Wait for button press
        elif(GPIO.input(BUTTONB) == 0):
            #call function to play the songs in this playlist
            play_song('/var/lib/cloud9/ENGI301/Project1/Chen/*.mp3')
           
         #Wait for button press
        elif(GPIO.input(BUTTONC) == 0):
            #stop all processes when the control button is pressed
            process.kill()
            
#end def

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == '__main__':
    setup()
    
    try:
        task()
    except KeyboardInterrupt:
        pass

    print("Program Complete.")
