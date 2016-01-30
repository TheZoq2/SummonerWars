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


###############################
## Fuzzy spell implementation

import functools

def transfer_same(x):
    return x

fuzzy_spells = [
    {
        "name": "NoEffect",
        "parts": []
    },
    {
        "name":  "FireWater",
        "parts" : [
            {
                "input": "fire",
                "utility": transfer_same
            },
            {
                "input": "water",
                "utility": transfer_same
            }
        ]
    },
]

class FuzzyCaster:

    def __init__(self, recipes):
        self.__recipes = recipes

    def new_spell(self):
        self.__ingredients = {}

    def add_ingredient(self, name):
        self.__ingredients[name] += 1.0/8

    def cast_spell(self):
        for spell in self.__recipes:
            scores = []
            for part in spell["parts"]:
                try:
                    scores.append(part["utility"](self.__ingredients[part["input"]]))
                except KeyError:
                    scores.append(0.0)
            if scores:
                spell["score"] = functools.reduce(lambda x,y: x*y, scores)
            else:
                spell["score"] = 0.0
        def get_score(item):
            return item["score"]
        return sorted(self.__recipes, key=get_score, reverse=True)[0]


################
## Spell caster

class Caster(StateCaster):

    def __init__(self):
        super().__init__(state_spells)
        random.seed()

    def refill_ingredient(self):
        selected_ingredient = random.randrange(0, Globals.NUM_INGREDIENTS * 4) % Globals.NUM_INGREDIENTS
        return ingredients[selected_ingredient]

