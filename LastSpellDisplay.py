import cocos
import pyglet

import util
import Globals
import random

class LastSpellDisplay(cocos.layer.Layer):
    SPREAD_X = 200
    SPREAD_Y = 100

    def __init__(self, position):
        super(LastSpellDisplay, self).__init__()

        self.position = position
        
        self.sprites = []

    def on_spell_cast(self, usedIngredients):
        #Remove old bottles
        for sprite in self.sprites:
            self.remove(sprite)

        self.sprites = []
        for ing in usedIngredients:
            bottlePos = self.SPREAD_X * random.random(),self.SPREAD_Y * random.random()

            bottleScale = 0.4 - 0.2 * bottlePos[1] / self.SPREAD_Y

            bgSprite = cocos.sprite.Sprite(Globals.BOTTLE_BACKGROUND)
            fgSprite = cocos.sprite.Sprite(Globals.BOTTLE_FOREGROUND)
            symbolSprite = cocos.sprite.Sprite(util.symbolMap[ing])
            
            bgSprite.color = (random.randint(0,1) * 150, random.randint(0,1) * 150, random.randint(0,1) * 150)
            bgSprite.position = bottlePos

            bgSprite.add(fgSprite)
            fgSprite.add(symbolSprite)

            bgSprite.scale = bottleScale
            symbolSprite.scale = 2
            symbolSprite.position = (0, -25)
            
            self.add(bgSprite, z=-bottlePos[1])
            self.sprites.append(bgSprite)



        
