import random

from SpellWheel import *
import SpellBook 
import Globals

import pyglet

class Player(pyglet.event.EventDispatcher):
    def __init__(self, spellWheel, position):
        self.currentIngredients = []

        self.other = None

        self.spellWheel = spellWheel
        #Subscribe to events from the spell wheel
        self.spellWheel.push_handlers(self)

        self.caster = SpellBook.Caster()

        self.currentHealth = Globals.MAX_HEALTH
        self.statusEffects = {"onHitTarget": [], "onGetHit": [], "onTargetSelf": [], "onTargetEnemy": []}
        self.fails = 0  # While >0, spells cast by this player fail.
        self.isProtected = False

        self.position = position

        self.choseNewIngredients()

        Player.register_event_type("on_hp_change")
        Player.register_event_type("on_spell_cast")

    #Look away!
    def setOther(other, self):
        other.other = self


    def increaseHealth(self, amount):
        self.currentHealth += amount
        if self.currentHealth > 100:
            self.currentHealth = 100

        self.dispatch_event("on_hp_change", self)

    def reduceHealth(self, amount):
        self.currentHealth -= amount

        self.dispatch_event("on_hp_change", self)

    def getHealth(self):
        assert self.currentHealth <= 100
        return self.currentHealth

    def addStatusEffect(self, effect, effectType, duration):
        """Allows the provided effect function to be called based on its effectType, until duration ends"""
        self.statusEffects[effectType].append((effect, duration))


    def choseNewIngredients(self):
        for i in range(0, Globals.INGREDIENTS_PER_TURN):
            self.currentIngredients.append(self.caster.refill_ingredient())

        #Tell the spell wheel about this change
        self.spellWheel.setIngredients(self.currentIngredients);

    def updateIngredients(self):
        #Get the used ingredients from the spell wheel
        indexes = self.spellWheel.getSelectedIngredientIndexes()

        #Replace the ingredients in those slots with new ones
        for i in indexes:
            self.currentIngredients[i] = self.caster.refill_ingredient()

        self.spellWheel.setIngredients(self.currentIngredients)

    
    def castSpell(self, event, target):
        self.dispatch_event(event, self.spellWheel.getSelectedIngredients())

        for ingredient in self.spellWheel.getSelectedIngredients():
            self.caster.add_ingredient(ingredient)

        self.caster.cast_spell()(self, target)

        self.updateIngredients()

    def on_self_cast(self, wheel):
        self.castSpell("on_spell_cast", self)

    def on_normal_cast(self, wheel):
        self.castSpell("on_spell_cast", self.other)

