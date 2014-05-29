This is a python script to control vlc player using a apple remote.
To use the script enable the web interface on your vlc player.
Connect a arduino to your computer and burn the ino file onto the board. I am using the arduino ir remote library at: https://github.com/shirriff/Arduino-IRremote .
Connect a TSOP1838 or any other ir receiver to your arduino board on pin 2 and run the vlc script as python vlc.py &.