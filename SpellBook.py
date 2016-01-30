import Globals
import random
from enum import Enum

########################
## Possible ingredients

class Ingredients(Enum):
    fire = 0
    water = 1

##############################
## State spell implementation

state_spells = {
    (): "NoEffect",
    (Ingredients.fire, Ingredients.water): "FireWater",
    (Ingredients.water, Ingredients.fire): "WaterFire",
    (Ingredients.fire, Ingredients.fire, Ingredients.fire, Ingredients.fire): "DragonFire",
}

class StateCaster:

    def __init__(self, recipes):
        self.__recipes = recipes

    def new_spell(self):
        self.__ingredients = []

    def add_ingredient(self, ingredient):
        self.__ingredients.append(ingredient)

    def cast_spell(self):
        try:
            return self.__recipes[tuple(self.__ingredients)]
        except KeyError:
            return self.__recipes[()]

################
## Spell caster

class Caster(StateCaster):

    def __init__(self):
        super().__init__(state_spells)
        random.seed()

    def refill_ingredient(self):
        return random.randrange(0, Globals.NUM_INGREDIENTS)

