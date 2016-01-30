import cocos
import pyglet
from cocos.actions import *

from SpellWheel import *


cocos.director.director.init()
cocos.director.director.run (cocos.scene.Scene(SpellWheel(pyglet.input.get_joysticks()[0])))

