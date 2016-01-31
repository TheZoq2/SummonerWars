import Globals
import random

from cocos.actions import *

symbolMap = []
def generateSymbols():
    for img in Globals.RUNE_IMAGES:
        symbolMap.append(img)
    
    random.shuffle(symbolMap)
