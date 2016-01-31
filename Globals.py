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
NUM_INGREDIENTS = 8

POS_PLAYER_1 = (275,400)
POS_PLAYER_2 = (1015,400)
POS_WHEEL_1 = (139,270)
POS_WHEEL_2 = (507,270)
POS_HPBAR_1 = (100,700)
POS_HPBAR_2 = (1200,700)

SELECT_BUTTONS = [10, 0, 5, 9, 4]
BACK_BUTTONS = [1]
SELF_CAST_BUTTONS = [3]
NORMAL_CAST_BUTTON = [2]

TRIGGER_THRESHOLD = 0.5

MAX_HEALTH = 100

RUNE_IMAGES = [
    "Assets/ingredients/rune1.png",
    "Assets/ingredients/rune2.png",
    "Assets/ingredients/rune3.png",
    "Assets/ingredients/rune4.png",
    "Assets/ingredients/rune5.png",
    "Assets/ingredients/rune6.png",
    "Assets/ingredients/rune7.png",
    "Assets/ingredients/rune8.png",
    "Assets/ingredients/rune9.png",
    "Assets/ingredients/rune10.png",
    "Assets/ingredients/rune11.png",
    "Assets/ingredients/rune12.png",
    "Assets/ingredients/rune13.png",
    "Assets/ingredients/rune14.png",
    "Assets/ingredients/rune15.png",
    "Assets/ingredients/rune16.png",
    "Assets/ingredients/rune17.png",
    "Assets/ingredients/rune18.png",
    "Assets/ingredients/rune19.png",
    "Assets/ingredients/rune20.png",
    "Assets/ingredients/rune21.png",
    "Assets/ingredients/rune22.png",
    "Assets/ingredients/rune23.png",
    "Assets/ingredients/rune24.png",
    "Assets/ingredients/rune25.png",
    "Assets/ingredients/rune26.png",
    "Assets/ingredients/rune27.png"
]

class UpdateAction( InstantAction ):
    def init(self):
        pass
    def start(self):
        pass

