import cocos
from cocos.actions import *
import pyglet

import math
import random

import Globals


class SpellWheel(cocos.layer.Layer, pyglet.event.EventDispatcher): 
    BACKGROUND_IMAGE = "Assets/spellwheel_slice.png" 
    is_event_handler = True

    symbolMap = []
    def generateSymbols():
        for img in Globals.RUNE_IMAGES:
            SpellWheel.symbolMap.append(img)
        
        SpellWheel.symbolMap = random.shuffle(symbolMap)

    def __init__(self, joystick, position):
        super( SpellWheel, self).__init__()
        self.ingredients = [] 
        self.selectedIngredients = []

        self.position = position

        self.backgrounds = []
        self.ingSprites = []

        #Visualisation stuff
        for i in range(0, Globals.INGREDIENTS_PER_TURN):
            self.backgrounds.append(cocos.sprite.Sprite(self.BACKGROUND_IMAGE))

            angle = i * 360 / Globals.INGREDIENTS_PER_TURN

            self.backgrounds[i].rotation = angle
            self.backgrounds[i].position = self.position
            self.backgrounds[i].image_anchor = 0,0
            self.backgrounds[i].color = 255,255,255
            self.add(self.backgrounds[i])

        self.currentAngle = 0
        self.currentSector = 0

        self.joystick = joystick
        print(joystick.device)

        self.joystick.open()

        self.joystick.push_handlers(self)

        SpellWheel.register_event_type("on_self_cast")

        
    def on_joybutton_press(self, joystick, button):
        if button in Globals.SELECT_BUTTONS:
            if not self.currentSector in self.selectedIngredients:
                self.selectedIngredients.append(self.currentSector)

        if button in Globals.BACK_BUTTONS:
            if self.selectedIngredients:
                self.selectedIngredients.pop()

        if button in Globals.SELF_CAST_BUTTONS:
            self.dispatch_event("on_self_cast", self)

        self.updateSectorVisualisation()

        print(button)

    def on_joyaxis_motion(self, joystick, axis, value):
        #Calculate stick angle
        x = joystick.rx
        y = joystick.ry

        angle = math.atan2(y, x) * 360/(2*math.pi) + 90

        if(angle < 0): 
            angle += 360

        #Highlight the current sector
        self.currentSector = math.floor(angle / 360 * Globals.INGREDIENTS_PER_TURN)

        self.updateSectorVisualisation()

    def updateSectorVisualisation(self):
        #Reset color on all the backgrounds
        for i in range(len(self.backgrounds)):
            bg = self.backgrounds[i]
            bg.do(Globals.UpdateAction())
            
            if i in self.selectedIngredients:
                bg.color = 255,0,0
            else:
                bg.color = 255,255,255
        
        self.backgrounds[self.currentSector].color = 0,0,255 

    def setIngredients(self, ingredients):
        self.ingredients = ingredients

    def getSelectedIngredients(self):
        result = []
        for sel in selectedIngredients:
            result.append(self.ingredients[sel])

        return result
