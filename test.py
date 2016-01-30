import cocos
import pyglet
from cocos.actions import *

from SpellWheel import *
from Background import *
from Player import *

cocos.director.director.init(width=Globals.VID_WIDTH, height=Globals.VID_HEIGHT, caption=Globals.GAME_NAME, fullscreen=Globals.VID_FULLSCREEN)

sw = SpellWheel(pyglet.input.get_joysticks()[0], (200, 200))

player = Player(sw)

cocos.director.director.run(cocos.scene.Scene(
    Background(),
    player.spellWheel
))
