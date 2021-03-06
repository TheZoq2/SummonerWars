import cocos
from cocos.actions import *
import pyglet

import Globals
import util
from Actions import *

class HealthBar(cocos.layer.Layer): 
    def __init__(self, position):
        super(HealthBar, self).__init__()

        self.position = position

        self.sprite = cocos.sprite.Sprite(Globals.HEALTHBAR_IMAGE)
        self.bg = cocos.sprite.Sprite(Globals.HEALTHBAR_BACKGROUND)

        self.sprite.image_anchor = 0,0
        self.bg.image_anchor = 0,0

        self.add(self.bg)
        self.add(self.sprite)

    def on_hp_change(self, player):
        size = player.getHealth() / Globals.MAX_HEALTH

        self.sprite.scale_x = size

        self.sprite.do(UpdateAction())

        print("Health changed")
        print(player.getHealth())


