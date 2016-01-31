import Globals
import SpellEffects

import random
from enum import *

########################
## Possible ingredients

class Ingredients(IntEnum):
    air = 0
    water = 1
    earth = 2
    fire = 3
    light = 4
    dark = 5
    cosmic = 6
    blood = 7

    def __lt__(self, other):
        return self.value < other.value



##############################
## State spell implementation

state_spells = {
    (): SpellEffects.NoEffect,
    (Ingredients.fire, Ingredients.blood): SpellEffects.BloodArrow,
    (Ingredients.water, Ingredients.water, Ingredients.water): SpellEffects.Strike,
    (Ingredients.water, Ingredients.light): SpellEffects.OpenMind,
    (Ingredients.air, Ingredients.fire, Ingredients.fire): SpellEffects.Oops,
    (Ingredients.air, Ingredients.cosmic): SpellEffects.Anguish,
    (Ingredients.air, Ingredients.blood): SpellEffects.Turmoil,
    (Ingredients.fire, Ingredients.cosmic): SpellEffects.Nova,
    (Ingredients.light, Ingredients.blood): SpellEffects.Heal,
    (Ingredients.light, Ingredients.light, Ingredients.blood): SpellEffects.GreaterHeal,
    (Ingredients.air, Ingredients.water, Ingredients.earth, Ingredients.fire, Ingredients.light,
                                    Ingredients.dark, Ingredients.cosmic, Ingredients.blood): SpellEffects.OmniPower,
    (Ingredients.light, Ingredients.dark): SpellEffects.Equilibrium,
    (Ingredients.light, Ingredients.light, Ingredients.light): SpellEffects.Strike,
    (Ingredients.dark, Ingredients.dark, Ingredients.dark): SpellEffects.Strike,
    (Ingredients.fire, Ingredients.fire, Ingredients.fire): SpellEffects.Strike,
    (Ingredients.air, Ingredients.air, Ingredients.air): SpellEffects.Strike,
    (Ingredients.earth, Ingredients.earth, Ingredients.earth): SpellEffects.Strike,
    (Ingredients.blood, Ingredients.blood, Ingredients.blood): SpellEffects.Strike,
    (Ingredients.cosmic, Ingredients.cosmic, Ingredients.cosmic): SpellEffects.Strike,
    (Ingredients.earth, Ingredients.fire): SpellEffects.Eruption,
    (Ingredients.air, Ingredients.light): SpellEffects.Fade,
    (Ingredients.dark, Ingredients.blood): SpellEffects.CorruptedBlood,

}

assert(list(map(lambda seq: (list(seq) == sorted(list(seq))), list(state_spells))))

list(Ingredients)

class StateCaster:

    def __init__(self, recipes):
        self.__recipes = recipes
        self.__ingredients = []

    def new_spell(self):
        self.__ingredients = []

    def add_ingredient(self, ingredient):
        print("Ingredient added")
        self.__ingredients.append(ingredient)

    def cast_spell(self):
        try:
            print(self.__ingredients)
            spell = self.__recipes[tuple(sorted(self.__ingredients))]
        except KeyError:
            spell = self.__recipes[()]
        self.__ingredients = []
        return spell


################
## Spell caster

class Caster(StateCaster):

    def __init__(self):
        super().__init__(state_spells)
        random.seed()

    def refill_ingredient(self):
        #return random.randrange(0, Globals.NUM_INGREDIENTS)
        return random.choice(list(Ingredients))

