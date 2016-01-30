import random

from SpellWheel import *
import SpellBook 
import Globals

class Player:
    def __init__(self, spellWheel):
        self.currentIngredients = []

        self.spellWheel = spellWheel
        #Subscribe to events from the spell wheel
        self.spellWheel.push_handlers(self)

        self.caster = SpellBook.Caster()

        self.currentHealth = 100
        self.statusEffects = {"onHitTarget": [], "onGetHit": [], "onTargetSelf": [], "onTargetEnemy": []}
        self.fails = 0  # While >0, spells cast by this player fail.
        self.isProtected = False

        self.choseNewIngredients()

    def addStatusEffect(self, effect, effectType, duration):
        """Allows the provided effect function to be called based on its effectType, until duration ends"""
        self.statusEffects[effectType].append((effect, duration))


    def choseNewIngredients(self):
        for i in range(0, Globals.INGREDIENTS_PER_TURN):
            self.currentIngredients.append(random.randint(0, Globals.NUM_INGREDIENTS))

        #Tell the spell wheel about this change
        self.spellWheel.setIngredients(self.currentIngredients);

    def updateIngredients(self):
        #Get the used ingredients from the spell wheel
        indexes = self.spellWheel.getSelectedIngredientIndexes()

        #Replace the ingredients in those slots with new ones
        for i in indexes:
            self.currentIngredients[i] = self.caster.refill_ingredient()

        self.spellWheel.setIngredients(self.currentIngredients)

    
    def on_self_cast(self, wheel):
        print(self.spellWheel.getSelectedIngredientIndexes())

        self.caster.cast_spell()(self, self)

        self.updateIngredients()

