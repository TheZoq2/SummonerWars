import cocos
import pyglet
from cocos.scenes import *

import util

from BackgroundLayer import *
from EffectLayer import *

from SpellWheel import *
from Player import *
from HealthBar import *
from LastSpellDisplay import *
from GameOverScene import *

class GameScene(cocos.scene.Scene):

    def __init__(self):
        joyList = pyglet.input.get_joysticks()
        print(joyList)

        
        joystick,joyIndex = self.selectJoystick(joyList, 0)
        if joystick:
            print("Player1: " + str(joystick.device))
        
        joystick2,joyIndex = self.selectJoystick(joyList, joyIndex + 1)
        if joystick2:
            print("Player2: " + str(joystick2.device))
        
        util.generateSymbols()
        
        sw1 = SpellWheel(joystick, Globals.POS_WHEEL_1)
        sw2 = SpellWheel(joystick2, Globals.POS_WHEEL_2)
        
        hp1 = HealthBar(Globals.POS_HPBAR_1)
        hp2 = HealthBar(Globals.POS_HPBAR_2)
        
        spellDisplay1 = LastSpellDisplay(Globals.POS_BOTTLES_1)
        spellDisplay2 = LastSpellDisplay(Globals.POS_BOTTLES_2)
        
        self.player = Player(sw1)
        self.player2 = Player(sw2)
        
        self.player.push_handlers(hp1)
        self.player2.push_handlers(hp2)
        
        self.player.push_handlers(spellDisplay1)
        self.player2.push_handlers(spellDisplay2)

        self.player.push_handlers(self)
        self.player2.push_handlers(self)
        
        self.player.setOther(self.player2)
        self.player2.setOther(self.player)

        super(GameScene, self).__init__(
            BackgroundLayer(),
            EffectLayer(),
            self.player.spellWheel,
            self.player2.spellWheel,
            hp1,
            hp2,
            spellDisplay1,
            spellDisplay2,
        )

    def selectJoystick(self, joyList, startIndex):
        joystickIndex = startIndex
        try:
            joystick = joyList[joystickIndex]
        except IndexError:
            return None,joystickIndex
        
        while str(joystick.device).find("Teensy") != -1:
            joystickIndex += 1
            joystick = joyList[joystickIndex]

        return (joystick, joystickIndex)

    def on_hp_change(self, player):
        if player.getHealth() <= 0:
            winnerName = ""
            loserName = ""

            #Create a game over scene and replace yourself with that
            if player == self.player:
                winnerName = "Player 1"
                loserName = "Player 2"
            else:
                winnerName = "Player 1"
                loserName = "Player 2"

            goScene = GameOverScene(winnerName, loserName)

            cocos.director.director.push(TurnOffTilesTransition( goScene, duration=1 ))

