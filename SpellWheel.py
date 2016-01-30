import cocos
from cocos.actions import *
import pyglet

import math

import Globals

class SpellWheel(cocos.layer.Layer):
    BACKGROUND_IMAGE = "Assets/spellwheel_slice.png"

    is_event_handler = True

    def __init__(self, joystick):
        super( SpellWheel, self).__init__()
        self.ingredients = []
        
        self.backgrounds = []
        #Visualisation stuff
        for i in range(0, Globals.INGREDIENTS_PER_TURN):
            self.backgrounds.append(cocos.sprite.Sprite(self.BACKGROUND_IMAGE))

            angle = i * 360 / Globals.INGREDIENTS_PER_TURN

            self.backgrounds[i].rotation = angle
            self.backgrounds[i].position = 320,240
            self.backgrounds[i].image_anchor = 0,0
            self.backgrounds[i].color = 255,255,255
            self.add(self.backgrounds[i])

        self.currentAngle = 0
        self.currentSector = 0

        
        self.joystick = joystick
        print(joystick.device)

        self.joystick.open()

        self.joystick.push_handlers(self)

        
    def on_joybutton_press(self, joystick, button):
        print(button)
    
    def on_joyaxis_motion(self, joystick, axis, value):
        #Calculate stick angle
        x = joystick.rx
        y = joystick.ry

        angle = math.atan2(y, x) * 360/(2*math.pi) + 90

        if(angle < 0): 
            angle += 360

        #Highlight the current sector
        sector = math.floor(angle / 360 * Globals.INGREDIENTS_PER_TURN)

        print(sector)

        #self.backgrounds[sector].color = 255,0,0


        
