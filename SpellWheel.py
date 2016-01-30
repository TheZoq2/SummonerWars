import cocos
from cocos.actions import *
import pyglet

import Globals

class SpellWheel(cocos.layer.Layer):
    BACKGROUND_IMAGE = "yolo.png"

    def __init__(self):
        self.ingredients = []
        
        self.backgrounds = []
        #Visualisation stuff
        for i in range(0, Globals.INGREDIENTS_PER_TURN):
            self.backgrounds[i] = cocos.sprite.Sprite(self.BACKGROUND_IMAGE)

            angle = i * 360 / Globals.INGREDIENTS_PER_TURN

            self.backgrounds[i].rotation = angle
            self.add(self.backgrounds[i])


        
