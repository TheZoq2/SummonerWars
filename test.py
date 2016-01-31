import cocos
import pyglet
from cocos.actions import *

from GameScene import *

import Globals


cocos.director.director.init(width=Globals.VID_WIDTH, height=Globals.VID_HEIGHT, caption=Globals.GAME_NAME, fullscreen=Globals.VID_FULLSCREEN)


source = pyglet.media.load(Globals.MUSIC_FILE)

looper = pyglet.media.SourceGroup(source.audio_format, None)
looper.loop = True
looper.queue(source)
musicPlayer = pyglet.media.Player()
musicPlayer.queue(looper)
musicPlayer.play()

cocos.director.director.run(GameScene())

