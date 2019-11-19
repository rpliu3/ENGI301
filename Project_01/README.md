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

4. Plug USB External Stereo Sound Adapter into USB end of female to USB type A adapter.
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

### LED String Light Hardware
Parts Needed:
1. HKBAYI 240 pixel RGB light string
2. Cardboard
3. Clear tape

Steps:
1. Create a 25x9 LED matrix by snaking the LED light string along the cardboard and secure using tape. There should be one column of LED lights on either side of the matrix that will not be used in the display because it is the turning point of the light string. 
2. Connecte the LED light string to the PocketBeagle using the following pinout

    |    Wire     |      Pin      |
    | ------------- | ------------- |
    | Red (Vout) | P1.24 |
    | Green (Input) | P1.8 |
    | White (GND) | P1.22 |  

## Operation Instructions

Once PocketBeagle boots, user operates the device by simply pressing a button that corresponds to the kpop group that they want to listen to and display. The program can be stopped at any time using the control button. The group can also be changed at any time by pressing a different button. Songs in the playlist will be shuffled through continuously.
