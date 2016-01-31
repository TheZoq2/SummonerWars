import cocos
from cocos.actions import *

# Name of the game
GAME_NAME="Summoner Wars"

# Video resolution
VID_WIDTH=1280
VID_HEIGHT=720
VID_FULLSCREEN=False

# Game play
INGREDIENTS_PER_TURN = 8  # amount of available ingredients that the player has for each spell
NUM_INGREDIENTS      = 8  # amount of ingredients that exist in the game
MAX_HEALTH = 100

POS_WHEEL_1 = (275,500)
POS_WHEEL_2 = (1015,500)
POS_HPBAR_1 = (50,650)
POS_HPBAR_2 = (1100,650)
POS_BOTTLES_1 = (120,120)
POS_BOTTLES_2 = (900,120)
LABEL_OFFSET=(0,-140)
USER_OFFSET=(130,0)
TARGET_OFFSET=(-100,0)

# Controller mapping & setting
SELECT_BUTTONS = [10, 0, 5, 9, 4]
BACK_BUTTONS = [1]
SELF_CAST_BUTTONS = [3]
NORMAL_CAST_BUTTON = [2]
TRIGGER_THRESHOLD = 0.5

# Assets
FONT_FILE = "Assets/PressStart2P.ttf"
FONT_NAME = "Press Start 2P"

BOTTLE_FOREGROUND = "Assets/bottle.png"
BOTTLE_BACKGROUND = "Assets/bottleBackground.png"

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
]
WHEEL_SLICE = "Assets/spellwheel_slice.png"

BACKGROUND_LAYER = "Assets/background.png"
CLOUD_LAYER_1 = "Assets/cloudlayer2.png"
CLOUD_LAYER_2 = "Assets/cloudlayer1.png"

HEALTHBAR_IMAGE = "Assets/hpbar.png"
HEALTHBAR_BACKGROUND = "Assets/hpbackground.png"

SPELL_DEFAULT = "Assets/particle_fire.png"
SPELL_NOSPELL = "Assets/particle_fire.png"
SPELL_STRIKE = "Assets/particle_fire.png"
