import cocos
import pyglet
from cocos.actions import *

from SpellWheel import *


cocos.director.director.init(width=Globals.VID_WIDTH, height=Globals.VID_HEIGHT, caption=Globals.GAME_NAME, fullscreen=Globals.VID_FULLSCREEN)
cocos.director.director.run (cocos.scene.Scene(SpellWheel(pyglet.input.get_joysticks()[0], (200, 200))))

