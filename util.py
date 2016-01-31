import Globals
import random

symbolMap = []
def generateSymbols():
    for img in Globals.RUNE_IMAGES:
        symbolMap.append(img)
    
    random.shuffle(symbolMap)


