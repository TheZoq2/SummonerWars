import cocos
from cocos.actions import *
import pyglet

import Globals

class HealthBar(cocos.layer.Layer): 
    def __init__(self, position):
        super(HealthBar, self).__init__()

        self.position = position

        self.sprite = cocos.sprite.Sprite("Assets/hpbar.png")
        self.add(sprite)

    def on_health_change(self, player):
        size = player.getHealth() / Globals.MAX_HEALTH

        self.sprite.scale_x = size

        self.sprite.do(Globals.UpdateAction())


