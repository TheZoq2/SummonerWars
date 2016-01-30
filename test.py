import cocos
import pyglet
from cocos.actions import *

from SpellWheel import *
from Background import *
from Player import *

cocos.director.director.init(width=Globals.VID_WIDTH, height=Globals.VID_HEIGHT, caption=Globals.GAME_NAME, fullscreen=Globals.VID_FULLSCREEN)

joystickIndex = 0
joystick = pyglet.input.get_joysticks()[joystickIndex]

while str(joystick.device).find("Teensy") != -1:
    print(joystick.device)
    joystickIndex += 1
    joystick = pyglet.input.get_joysticks()[joystickIndex]

print(joystick.device)

sw = SpellWheel(joystick, (100,100))

player = Player(sw)

cocos.director.director.run(cocos.scene.Scene(
    Background(),
    player.spellWheel
))
