import Globals
import random

########################
## Possible ingredients

ingredients = [
    "fire",
    "water"
]

##############################
## State spell implementation

state_spells = {
    (): "NoEffect",
    ("fire", "water"): "FireWater",
    ("water", "fire"): "WaterFire",
    ("fire", "fire", "fire", "fire"): "DragonFire"
}

class StateCaster:

    def __init__(self, recipes):
        self.__recipes = recipes

    def new_spell(self):
        self.__ingredients = []

    def add_ingredient(self, name):
        self.__ingredients.append(name)

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
        selected_ingredient = random.randrange(0, Globals.NUM_INGREDIENTS * 4) % Globals.NUM_INGREDIENTS
        return ingredients[selected_ingredient]

