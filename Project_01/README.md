# Multi-Fandom Fan Light Display with Music
This repository contains the code and documentation for this project. This project uses push buttons to play playlists of MP3 files while displaying a corresponding LED design. The device is controlled by a panel of push buttons and runs on boot. The code and build instructions are intended for implementation on a PocketBeagle and assumes that user has already setup the PocketBeagle for use.

## Build Instructions

### Audio and Control Hardware
Parts Needed:
1. USB External Stereo Sound Adapter
2. Female USB Types A Adapter
3. Push Buttons (x 6)
4. 1.5 kOhm resistors (x 6; brown, green, red)
5. Speaker of choice

Steps:
1. Solder V_BUS and V_IN pins (P1.5 and P1.7) together.
2. Solder ID and GND pins (P1.13 and P1.15) together. 
3. Insert pins of female to USB type A adapter into PocketBeagle header. The pin alignment is as follows:

    |    Adapter    |  PocketBeagle |
    | ------------- | ------------- |
    | V_cc | V_BUS/V_IN (P1.7) |
    | D- | DN (P1.9)  |
    | D+ | DP (P1.11) |
    | ID | ID (P1.13) |
    | GND | GND (P1.15) |

4. Plug USB External Stereo Sound Adapter into USB hub that is plugged into the USB end of female to USB type A adapter.
5. Plug speaker of choice into green output port of the stereo sound adapter.
6. Wire push button with the lower right leg connected to ground and the upper left leg connected to a 1.5 kOhm resistor connected to 3.3 V power supply. The upper left leg should also be connected to a GPIO pin on the PocketBeagle. The following GPIO pins were used (NOTE: If user uses different GPIO pins, code constants must be changed to reflect the difference).

    |    Button     |      Pin      |
    | ------------- | ------------- |
    | Control | P2.24 |
    | Black | P2.22 |
    | Yellow | P2.20 |
    | Green | P2.18 |
    | Red | P2.19 |
    | Blue | P2.17 |    

### Audio and Control Code
1. Ensure that the package for mpg123 (command line mp3 player) is installed. If the player is not installed use both commands in sequential order:

sudo apt-get install mpg123
sudo apt-get install pulseaudio

2. If GPIO pins were wired differently, the constants in the code must be changed to reflect this difference.

3. Lists of desired MP3 tracks must be loaded onto the PocketBeagle prior to use. Ensure that the pathway to these lists in the code under the task function are complete and correct.

4. The code for just the audio can also be run through the terminal using python3 audiotest.py (make sure pathway includes LEDscape).

### LED String Light Hardware
Parts Needed:
1. HKBAYI 240 pixel RGB light string
2. Cardboard
3. Clear tape
4. USB male to 5 pin female adapter

Steps:
1. Create a 25x9 LED matrix by snaking the LED light string along the cardboard and secure using tape. There should be one column of LED lights on either side of the matrix that will not be used in the display because it is the turning point of the light string. 
2. Connect the LED light string to the PocketBeagle and USB hub (for power) using the following pinout

    |    Wire     |      Pin      |
    | ------------- | ------------- |
    | Red (Vout) | Positive pin of USB |
    | Green (Input) | P1.8 |
    | White (GND) | Negative pin of USB |  
    
### LED Strings Light Code

1. First edit user boot file to use UIO:

cd /boot
grep pru uEnv.txt
sudo nano uEnv.txt

2. The file should be edited to look like this:

###pru_rproc (4.4.x-ti kernel)
#uboot_overlay_pru=/lib/firmware/AM335X-PRU-RPROC-4-4-TI-00A0.dtbo
###pru_rproc (4.14.x-ti kernel)
#uboot_overlay_pru=/lib/firmware/AM335X-PRU-RPROC-4-14-TI-00A0.dtbo
###pru_uio (4.4.x-ti, 4.14.x-ti & mainline/bone kernel)
uboot_overlay_pru=/lib/firmware/AM335X-PRU-UIO-00A0.dtbo

3. Prior to running script, ensure that LEDscape and open pixel control libraries are cloned into user repository. These library contains all scripts needed to drive the LEDs and can be accessed at the links below:
https://github.com/Yona-Appletree/LEDscape
https://github.com/zestyping/openpixelcontrol

4. Move all scripts that will be used to operate this device into the LEDscape folder. These include audiotest.py, lightstest.py, Composite.py, and opc.py (from the open pixel control library).
Before running any code, be sure to configure the input pin.
config-pin P1_8 out

5. Next begin the server by running: sudo ./opc-server --config my-config.json
The code for just the LED display can be run through the terminal using python3 lightstest.py (make sure path includes LEDscape).

## Operation Instructions

User should have one terminal open that is used to run config-pin P1_8 out and sudo ./opc-server --config my-config.json. The user should then open another terminal (without exiting the first) that is used to run python3 Composite.py (make sure path includes LEDscape). The user can then interact with the display using the panel of buttons. When switching between groups, the user should press the control button to clear the LED display. Use for continuous music and light displays!

# Find out more about this project on Hackster: 
https://www.hackster.io/rebecca-liu/light-up-multi-kpop-group-fan-display-with-music-3c68dd
