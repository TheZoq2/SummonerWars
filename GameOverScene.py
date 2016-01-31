import cocos
import pyglet

import Globals

from BackgroundLayer import *

class GameOverLayer(cocos.layer.Layer):
    def __init__(self, winner, loser):
        super(GameOverLayer, self).__init__()

        self.message = winner + " has outspelled " + loser

        self.goText = cocos.text.Label("Game Over!", anchor_x="center", font_size=24, font_name=Globals.FONT_NAME)
        self.winnerText = cocos.text.Label(self.message, anchor_x="center", font_size=24, font_name=Globals.FONT_NAME)

        self.goText.position = Globals.VID_WIDTH / 2, 500
        self.winnerText.position = Globals.VID_WIDTH / 2, 300

        self.add(self.goText)
        self.add(self.winnerText)


class GameOverScene(cocos.scene.Scene):
    def __init__(self, winnerName, loserName):
        super(GameOverScene, self).__init__(
                    BackgroundLayer(),
                    GameOverLayer(winnerName, loserName),
                )
