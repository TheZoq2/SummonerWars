import cocos
from cocos.actions import *
from cocos.actions.interval_actions import *
from cocos.text import Label
from cocos.sprite import Sprite
from SpellEffects import effectDispatchCenter

from pyglet import font

def Shoot(from_pos, to_pos, duration):
    return ( Place(from_pos) + Show() + MoveTo(to_pos, duration) + Hide() )

class EffectLayer(cocos.layer.Layer):

    def __init__(self):
        super(EffectLayer, self).__init__()
        effectDispatchCenter.push_handlers(self)
        font.add_file("Assets/PressStart2P.ttf")

    def on_spell(self, user, target, type):
        label = Label(type, anchor_x="center", font_size=16, font_name="Press Start 2P")
        label.position = user.position
        label.opacity = 0
        label.do(FadeIn(0.2) + Delay(0.5) + FadeOut(0.4))
        self.add(label)
