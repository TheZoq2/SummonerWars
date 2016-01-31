import cocos
from cocos.actions import *
import Globals

class BackgroundLayer(cocos.layer.Layer):

    def __init__(self):
        super(BackgroundLayer, self).__init__()

        background = cocos.sprite.Sprite(Globals.BACKGROUND_LAYER, anchor=(0,0))
        self.add(background)

        cloudlayer1 = cocos.sprite.Sprite(Globals.CLOUD_LAYER_1, anchor=(0,0))
        cloudlayer1.do(Place((0,0)) + MoveTo((1280,0), 60) + Repeat(Place((-1280,0)) + MoveTo((1280,0), 120)))

        cloudlayer2 = cocos.sprite.Sprite(Globals.CLOUD_LAYER_2, anchor=(0,0))
        cloudlayer2.do(Place((0,0)) + MoveTo((1280,0), 45) + Repeat(Place((-1280,0)) + MoveTo((1280,0), 90)))

        cloudlayer3 = cocos.sprite.Sprite(Globals.CLOUD_LAYER_1, anchor=(0,0))
        cloudlayer3.do(Place((-1280,0)) + MoveTo((1280,0), 120) + Repeat(Place((-1280,0)) + MoveTo((1280,0), 120)))

        cloudlayer4 = cocos.sprite.Sprite(Globals.CLOUD_LAYER_2, anchor=(0,0))
        cloudlayer4.do(Place((-1280,0)) + MoveTo((1280,0), 90) + Repeat(Place((-1280,0)) + MoveTo((1280,0), 90)))

        self.add(cloudlayer1)
        self.add(cloudlayer2)
        self.add(cloudlayer3)
        self.add(cloudlayer4)

