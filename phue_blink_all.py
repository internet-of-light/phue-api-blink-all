from phue import Bridge
from time import sleep
from rgb_xy import Converter
#import random
#remember to: pip3 install phues

#b = Bridge('10.0.1.16')    #Spieth Home
# For reference, the hubs are on the UW network at these IP addresses
# Lab Green	172.28.219.225
# Lab Blue	172.28.219.235
# Lab Red	172.28.219.189
# Sieg Master	172.28.219.179

b = Bridge('172.28.219.225') #Lab Green

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
#b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
#print(b.get_api())


lights = b.get_light_objects()



for light in lights:
    print(light)
    light.transitiontime = 10;



    
while True:
    for light in lights:
        light.on = True
        light.brightness = 255
        b.set_group(1, 'hue', 10000)
        light.xy = [.5,.2]
        print(light.xy)
        sleep(.1)
        light.on = False
        sleep(.1)

