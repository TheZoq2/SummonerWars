import cocos
from cocos.actions import *
from cocos.actions.interval_actions import *
from cocos.text import Label
from cocos.sprite import Sprite
from SpellEffects import effectDispatchCenter

def Shoot(from_pos, to_pos, duration):
    return ( Place(from_pos) + Show() + MoveTo(to_pos, duration) + Hide() )

class EffectLayer(cocos.layer.Layer):

    FIRE_IMAGE = "Assets/particle_fire.png"

    def __init__(self):
        super(EffectLayer, self).__init__()
        effectDispatchCenter.push_handlers(self)

        self.fire_counter = 0
        self.fire_pool = [Sprite(self.FIRE_IMAGE) for i in range(10)]

    def on_spell(self, user, target, type):
        label = Label(type)
        label.position = user.position
        label.opacity = 0
        label.do(FadeIn(0.2) + Delay(0.5) + FadeOut(0.4))
        self.add(label)
