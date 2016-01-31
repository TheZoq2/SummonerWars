import cocos
from cocos.actions import *
import pyglet

import math
import random

import Globals
import util


class SpellWheel(cocos.layer.Layer, pyglet.event.EventDispatcher): 
    BACKGROUND_IMAGE = Globals.WHEEL_SLICE
    is_event_handler = True

    WHEEL_RADIUS = 60

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
            self.backgrounds[i].image_anchor = 0,0
            self.backgrounds[i].color = 255,255,255
            self.add(self.backgrounds[i])

        self.currentAngle = 0
        self.currentSector = 0

        if joystick:
            self.joystick = joystick
            self.joystick.open()
            self.joystick.push_handlers(self)

        SpellWheel.register_event_type("on_self_cast")
        SpellWheel.register_event_type("on_normal_cast")

        
    def on_joybutton_press(self, joystick, button):
        if button in Globals.SELECT_BUTTONS:
            if not self.currentSector in self.selectedIngredients and self.currentSector != None:
                self.selectedIngredients.append(self.currentSector)

        if button in Globals.BACK_BUTTONS:
            if self.selectedIngredients:
                self.selectedIngredients.pop()

        if button in Globals.SELF_CAST_BUTTONS:
            self.trySelfCast()

        if button in Globals.NORMAL_CAST_BUTTON:
            self.tryNormalCast()

        self.updateSectorVisualisation()
        
        print(button)


    def on_joyaxis_motion(self, joystick, axis, value):
        if axis == "rz":
            if value > Globals.TRIGGER_THRESHOLD:
                self.tryNormalCast()

        if axis == "z":
            if value > Globals.TRIGGER_THRESHOLD:
                self.trySelfCast()

            if value < -Globals.TRIGGER_THRESHOLD:
                self.tryNormalCast()

        #Calculate stick angle
        if axis == "rx" or axis == "ry":
            x = joystick.rx
            y = joystick.ry

            if abs(x) > 0.1 or abs(y) > 0.1:
                angle = math.atan2(y, x) * 360/(2*math.pi) + 90

                if(angle < 0): 
                    angle += 360

                #Highlight the current sector
                self.currentSector = math.floor(angle / 360 * Globals.INGREDIENTS_PER_TURN)

            else:
                self.currentSector = None

        self.updateSectorVisualisation()

    def trySelfCast(self):
        if self.selectedIngredients:
            self.dispatch_event("on_self_cast", self)

    def tryNormalCast(self):
        if self.selectedIngredients:
            self.dispatch_event("on_normal_cast", self)


    def updateSectorVisualisation(self):
        #Reset color on all the backgrounds
        for i in range(len(self.backgrounds)):
            bg = self.backgrounds[i]
            bg.do(util.UpdateAction())
            
            if i in self.selectedIngredients:
                bg.color = 255,0,0
            else:
                bg.color = 255,255,255
        
        if self.currentSector != None:
            selectedColor = self.backgrounds[self.currentSector].color
            self.backgrounds[self.currentSector].color = (
                    selectedColor[0] * 0.5,
                    selectedColor[1] * 0.5,
                    selectedColor[2] * 0.5,
                    )

    def setIngredients(self, ingredients):
        self.ingredients = ingredients
        self.selectedIngredients = []

        for sprite in self.ingSprites:
            self.remove(sprite)

        self.ingSprites = []
        #Create the sprites
        for i in range(len(self.ingredients)):
            angle = (i + 0.5) * 360 / Globals.INGREDIENTS_PER_TURN

            angle = -angle
            angle += 180

            ingID = self.ingredients[i]
            
            angleRad = angle / 180 * math.pi

            spriteX = math.cos(angleRad - math.pi / 2) * SpellWheel.WHEEL_RADIUS
            spriteY = math.sin(angleRad - math.pi / 2) * SpellWheel.WHEEL_RADIUS

            sprite = cocos.sprite.Sprite(util.symbolMap[ingID])

            sprite.position = (spriteX, spriteY)
            self.add(sprite)
            
            self.ingSprites.append(sprite)


    def getSelectedIngredients(self):
        result = []
        for sel in self.selectedIngredients:
            result.append(self.ingredients[sel])

        return result
    
    def getSelectedIngredientIndexes(self):
        return self.selectedIngredients
    
    def on_damage_taken(self):
        SHAKE_AMOUNT = 20
        actionChain = util.UpdateAction()

        for i in range(0,20):
            newX = self.position[0] + (random.random() - 0.5) * SHAKE_AMOUNT
            newY = self.position[1] + (random.random() - 0.5) * SHAKE_AMOUNT

            SHAKE_AMOUNT -= 1
            actionChain += Place((newX, newY))
            actionChain += Delay(0.05)

        self.do(actionChain)

