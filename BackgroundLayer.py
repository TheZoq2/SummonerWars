import cocos
from cocos.actions import *
import Globals

class BackgroundLayer(cocos.layer.Layer):

    BACKGROUND_IMAGE = "Assets/background.png"
    CLOUD_LAYER_1 = "Assets/cloudlayer1.png"
    CLOUD_LAYER_2 = "Assets/cloudlayer2.png"

    def __init__(self):
        super(BackgroundLayer, self).__init__()

        background = cocos.sprite.Sprite(self.BACKGROUND_IMAGE, anchor=(0,0))
        self.add(background)

        cloudlayer1 = cocos.sprite.Sprite(self.CLOUD_LAYER_1, anchor=(0,0))
        cloudlayer1.do(Place((0,0)) + MoveTo((1280,0), 60) + Repeat(Place((-800,0)) + MoveTo((1280,0), 60)))

        cloudlayer2 = cocos.sprite.Sprite(self.CLOUD_LAYER_2, anchor=(0,0))
        cloudlayer2.do(Place((0,0)) + MoveTo((1280,0), 50) + Repeat(Place((-1200,0)) + MoveTo((1280,0), 50)))

        cloudlayer3 = cocos.sprite.Sprite(self.CLOUD_LAYER_1, anchor=(0,0))
        cloudlayer3.do(Place((0,0)) + MoveTo((-800,0), 60) + Repeat(Place((1280,0)) + MoveTo((-800,0), 60)))

        cloudlayer4 = cocos.sprite.Sprite(self.CLOUD_LAYER_2, anchor=(0,0))
        cloudlayer4.do(Place((0,0)) + MoveTo((-800,0), 50) + Repeat(Place((1200,0)) + MoveTo((-800,0), 50)))

        self.add(cloudlayer2)
        self.add(cloudlayer1)
        self.add(cloudlayer3)
        self.add(cloudlayer4)

