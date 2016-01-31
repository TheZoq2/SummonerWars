import cocos
import pyglet
from cocos.actions import *

from SpellWheel import *
from BackgroundLayer import *
from EffectLayer import *
from Player import *
from HealthBar import *

def selectJoystick(joyList, startIndex):
    joystickIndex = startIndex
    try:
        joystick = joyList[joystickIndex]
    except IndexError:
        return None,joystickIndex
    
    while str(joystick.device).find("T1eensy") != -1:
        joystickIndex += 1
        joystick = joyList[joystickIndex]

    return (joystick, joystickIndex)


cocos.director.director.init(width=Globals.VID_WIDTH, height=Globals.VID_HEIGHT, caption=Globals.GAME_NAME, fullscreen=Globals.VID_FULLSCREEN)

joyList = pyglet.input.get_joysticks()
print(joyList)

joystick,joyIndex = selectJoystick(joyList, 0)
if joystick:
    print("Player1: " + str(joystick.device))

joystick2,joyIndex = selectJoystick(joyList, joyIndex + 1)
if joystick2:
    print("Player2: " + str(joystick2.device))

util.generateSymbols()

sw1 = SpellWheel(joystick, Globals.POS_WHEEL_1)
sw2 = SpellWheel(joystick2, Globals.POS_WHEEL_2)

hp1 = HealthBar(Globals.POS_HPBAR_1)
hp2 = HealthBar(Globals.POS_HPBAR_2)

player = Player(sw1, Globals.POS_PLAYER_1)
player2 = Player(sw2, Globals.POS_PLAYER_2)

player.push_handlers(hp1)
player2.push_handlers(hp2)

player.setOther(player2)
player2.setOther(player)

cocos.director.director.run(cocos.scene.Scene(
    BackgroundLayer(),
    EffectLayer(),
    player.spellWheel,
    player2.spellWheel,
    hp1,
    hp2,
))

