import random

from SpellWheel import *
import Globals
class Player:
    def __init__(self):
        self.currentIngredients = []

        self.spellWheel = SpellWheel()

    def choseNewIngredients(self):
        for i in range(0, Globals.INGREDIENTS_PER_TURN):
            self.ingredients[i] = random.random(0, Globals.NUM_INGREDIENTS)

        #Tell the spell wheel about this change
        self.spellWheel.setIngredients(self.ingredients);
