import cocos
from cocos.actions import *

# Name of the game
GAME_NAME="Summoner Wars"

# Video resolution
VID_WIDTH=1280
VID_HEIGHT=720
VID_FULLSCREEN=False

#The amount of available ingredients that the player has for each spell
INGREDIENTS_PER_TURN = 8

#The amount of ingredients that exist in the game
NUM_INGREDIENTS = 16

SELECT_BUTTONS = [10, 0, 5]
BACK_BUTTONS = [1]

RUNE_IMAGES = [
    "Assets/ingredients/runes1.png",
    "Assets/ingredients/runes2.png",
    "Assets/ingredients/runes3.png",
    "Assets/ingredients/runes4.png",
    "Assets/ingredients/runes5.png",
    "Assets/ingredients/runes6.png",
    "Assets/ingredients/runes7.png",
    "Assets/ingredients/runes8.png",
    "Assets/ingredients/runes9.png",
    "Assets/ingredients/runes10.png",
    "Assets/ingredients/runes11.png",
    "Assets/ingredients/runes12.png",
    "Assets/ingredients/runes13.png",
    "Assets/ingredients/runes14.png",
    "Assets/ingredients/runes15.png",
    "Assets/ingredients/runes16.png",
    "Assets/ingredients/runes17.png",
    "Assets/ingredients/runes18.png",
    "Assets/ingredients/runes19.png",
    "Assets/ingredients/runes20.png",
    "Assets/ingredients/runes21.png",
    "Assets/ingredients/runes22.png",
    "Assets/ingredients/runes23.png",
    "Assets/ingredients/runes24.png",
    "Assets/ingredients/runes25.png",
    "Assets/ingredients/runes26.png",
    "Assets/ingredients/runes27.png"
]

class UpdateAction( InstantAction ):
    def init(self):
        pass
    def start(self):
        pass

