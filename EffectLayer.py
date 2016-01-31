import Globals

import cocos
from cocos.actions import *
from cocos.actions.interval_actions import *
from cocos.text import Label
from cocos.sprite import Sprite
from SpellEffects import effectDispatchCenter

from pyglet import font

class ColorLerp(IntervalAction):

    def init(self, from_color, to_color, duration):
        super(ColorLerp, self).init(duration)
        self.from_color = from_color
        self.to_color = to_color
        self.duration = duration

    def update(self, t):
        r = self.to_color[0] * t + self.from_color[0] * (1-t)
        g = self.to_color[1] * t + self.from_color[1] * (1-t)
        b = self.to_color[2] * t + self.from_color[2] * (1-t)
        self.target.color = r,g,b

def Shoot(from_pos, to_pos, duration):
    return ( Place(from_pos) + Show() + MoveTo(to_pos, duration) + Hide() )

class EffectLayer(cocos.layer.Layer):

    def __init__(self):
        super(EffectLayer, self).__init__()
        effectDispatchCenter.push_handlers(self)
        font.add_file(Globals.FONT_FILE)
        self.assets = {
            "Default": Sprite(Globals.SPELL_DEFAULT),
            "Oops": Sprite(Globals.SPELL_DEFAULT),
            "NoSpell": Sprite(Globals.SPELL_NOSPELL),
            "Heal": Sprite(Globals.SPELL_DEFAULT),
            "GreaterHeal": Sprite(Globals.SPELL_DEFAULT),
            "Strike": Sprite(Globals.SPELL_DEFAULT),
            "OpenMind": Sprite(Globals.SPELL_DEFAULT),
            "Anguish": Sprite(Globals.SPELL_DEFAULT),
            "BloodArrow": Sprite(Globals.SPELL_DEFAULT),
            "Turmoil": Sprite(Globals.SPELL_DEFAULT),
            "Nova": Sprite(Globals.SPELL_DEFAULT),
            "Equilibrium": Sprite(Globals.SPELL_DEFAULT),
            "OmniPower": Sprite(Globals.SPELL_DEFAULT),
            "Eruption": Sprite(Globals.SPELL_DEFAULT),
            "Fade": Sprite(Globals.SPELL_DEFAULT),
            "CorruptedBlood": Sprite(Globals.SPELL_DEFAULT),
        }
        self.effects = {
            "Default": self._Default,
            "Oops": self._Oops,
            "NoSpell": self._NoSpell,
            "Heal": self._Heal,
            "GreaterHeal": self._Heal,
            "Strike": self._Strike,
            "OpenMind": self._Default,
            "Anguish": self._Default,
            "BloodArrow": self._Default,
            "Turmoil": self._Default,
            "Nova": self._Default,
            "Equilibrium": self._Default,
            "OmniPower": self._Default,
            "Eruption": self._Default,
            "Fade": self._Default,
        }

    def _Default(self, user, target):
        sprite = self.assets["Default"]
        user_position = user.spellWheel.position[0] + Globals.USER_OFFSET[0], user.spellWheel.position[1] + Globals.USER_OFFSET[1]
        target_position = target.spellWheel.position[0] + Globals.TARGET_OFFSET[0], target.spellWheel.position[1] + Globals.TARGET_OFFSET[1]
        sprite.do(Shoot(user_position, target_position, 1.0) | ColorLerp((255,255,255), (200,10,10), 1.0) | FadeOut(1.0))
        self.add(sprite)

    def _NoSpell(self, user, target):
        sprite = self.assets["NoSpell"]
        user_position = user.spellWheel.position[0] + Globals.USER_OFFSET[0], user.spellWheel.position[1] + Globals.USER_OFFSET[1] - 56
        target_position = user.spellWheel.position[0] + Globals.USER_OFFSET[0], user.spellWheel.position[1] + Globals.USER_OFFSET[1] + 64
        sprite.do(Shoot(user_position, target_position, 1.0) | ColorLerp((127,127,127), (255,255,255), 1.0) | FadeOut(1.0))
        self.add(sprite)

    def _Oops(self, user, target):
        sprite = self.assets["Oops"]
        user_position = user.spellWheel.position[0] + Globals.USER_OFFSET[0], user.spellWheel.position[1] + Globals.USER_OFFSET[1]
        target_position = user.spellWheel.position[0] + Globals.TARGET_OFFSET[0], user.spellWheel.position[1] + Globals.TARGET_OFFSET[1]
        sprite.do(Shoot(user_position, target_position, 1.0) | ColorLerp((255,255,255), (200,10,10), 1.0) | FadeOut(1.0))
        self.add(sprite)

    def _Heal(self, user, target):
        sprite = self.assets["Heal"]
        user_position = user.spellWheel.position[0] + Globals.USER_OFFSET[0], user.spellWheel.position[1] + Globals.USER_OFFSET[1]
        target_position = target.spellWheel.position[0] + Globals.TARGET_OFFSET[0], target.spellWheel.position[1] + Globals.TARGET_OFFSET[1]
        sprite.do(Shoot(user_position, target_position, 1.0) | ColorLerp((192,192,192), (255,255,255), 1.0) | FadeOut(1.0))
        self.add(sprite)

    def _Strike(self, user, target):
        sprite = self.assets["Strike"]
        user_position = user.spellWheel.position[0] + Globals.USER_OFFSET[0], user.spellWheel.position[1] + Globals.USER_OFFSET[1]
        target_position = target.spellWheel.position[0] + Globals.TARGET_OFFSET[0], target.spellWheel.position[1] + Globals.TARGET_OFFSET[1]
        sprite.do(Shoot(user_position, target_position, 1.0) | ColorLerp((127,127,127), (0,0,0), 1.0) | FadeOut(1.0))
        self.add(sprite)

    def _show_spell_visual(self, user, target, spell):
        try:
            self.effects[spell](user, target)
        except KeyError:
            pass

    def _show_spell_label(self, user, spell):
        label = Label(spell, anchor_x="center", font_size=16, font_name=Globals.FONT_NAME)
        label.position = user.spellWheel.position[0]+Globals.LABEL_OFFSET[0],user.spellWheel.position[1]+Globals.LABEL_OFFSET[1]
        label.opacity = 0
        label.do(FadeIn(0.2) + Delay(0.8) + FadeOut(0.4))
        self.add(label)

    def on_spell(self, user, target, spell):
        self._show_spell_label(user, spell)
        self._show_spell_visual(user, target, spell)
