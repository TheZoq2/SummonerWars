import random

from SpellWheel import *
import Globals
class Player:
    def __init__(self):
        self.currentIngredients = []

        self.spellWheel = SpellWheel()

        self.currentHealth = 100
        self.statusEffects = {"onHitTarget": [], "onGetHit": [], "onTargetSelf": [], "onTargetEnemy": []}
        self.fails = 0  # While >0, spells cast by this player fail.
        self.isProtected = False

    def addStatusEffect(self, effect, effectType, duration):
        """Allows the provided effect function to be called based on its effectType, until duration ends"""
        self.statusEffects[effectType].append((effect, duration))


    def choseNewIngredients(self):
        for i in range(0, Globals.INGREDIENTS_PER_TURN):
            self.ingredients[i] = random.random(0, Globals.NUM_INGREDIENTS)

        #Tell the spell wheel about this change
        self.spellWheel.setIngredients(self.ingredients);

    def updateIngredients(self):

