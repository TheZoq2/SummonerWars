import cocos
import pyglet
from cocos.actions import *

from SpellWheel import *
from BackgroundLayer import *
from EffectLayer import *
from Player import *

def selectJoystick(joyList, startIndex):
    joystickIndex = startIndex
    joystick = joyList[joystickIndex]
    
    while str(joystick.device).find("Teensy") != -1:
        joystickIndex += 1
        joystick = joyList[joystickIndex]

    return (joystick, joystickIndex)


cocos.director.director.init(width=Globals.VID_WIDTH, height=Globals.VID_HEIGHT, caption=Globals.GAME_NAME, fullscreen=Globals.VID_FULLSCREEN)

joyList = pyglet.input.get_joysticks()
print(joyList)

joystick,joyIndex = selectJoystick(joyList, 0)

print("Player1: " + str(joystick.device))

joystick2,joyIndex = selectJoystick(joyList, joyIndex + 1)
print("Player2: " + str(joystick2.device))

SpellWheel.generateSymbols()

sw1 = SpellWheel(joystick, (100,300))
sw2 = SpellWheel(joystick2, (500,300))

player = Player(sw1)
player2 = Player(sw2)

player.setOther(player2)
player2.setOther(player)

cocos.director.director.run(cocos.scene.Scene(
    BackgroundLayer(),
    EffectLayer(),
    player.spellWheel,
    player2.spellWheel
))

