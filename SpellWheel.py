import cocos
from cocos.actions import *
import pyglet

import Globals

class SpellWheel(cocos.layer.Layer):
    BACKGROUND_IMAGE = "Assets/spellwheel_slice.png"

    def __init__(self):
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
            self.backgrounds[i].color = 255,0,0
            self.add(self.backgrounds[i])


        
