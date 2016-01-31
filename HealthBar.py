import cocos
from cocos.actions import *
import pyglet

import Globals

class HealthBar(cocos.layer.Layer): 
    def __init__(self, position):
        super(HealthBar, self).__init__()

        self.position = position

        self.sprite = cocos.sprite.Sprite("Assets/hpbar.png")
        self.add(self.sprite)

    def on_hp_change(self, player):
        size = player.getHealth() / Globals.MAX_HEALTH

        self.sprite.scale_x = size

        self.sprite.do(Globals.UpdateAction())

        print("Health changed")
        print(player.getHealth())


