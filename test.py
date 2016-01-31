import cocos
import pyglet
from cocos.actions import *

from GameScene import *



cocos.director.director.init(width=Globals.VID_WIDTH, height=Globals.VID_HEIGHT, caption=Globals.GAME_NAME, fullscreen=Globals.VID_FULLSCREEN)



cocos.director.director.run(GameScene())

