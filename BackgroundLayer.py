import cocos
from cocos.actions import *
import Globals

class BackgroundLayer(cocos.layer.Layer):

    BACKGROUND_IMAGE = "Assets/background.png"
    CLOUD_LAYER_1 = "Assets/cloudlayer1.png"
    CLOUD_LAYER_2 = "Assets/cloudlayer2.png"

    def __init__(self):
        super(BackgroundLayer, self).__init__()

        background = cocos.sprite.Sprite(self.BACKGROUND_IMAGE)
        background.image_anchor = 0,0
        self.add(background)

        cloudlayer1 = cocos.sprite.Sprite(self.CLOUD_LAYER_1)
        cloudlayer1.image_anchor = 0,0
        cloudlayer1.velocity = 15,0
        cloudlayer1.do(WrappedMove(Globals.VID_WIDTH, Globals.VID_HEIGHT))

        cloudlayer2 = cocos.sprite.Sprite(self.CLOUD_LAYER_2)
        cloudlayer2.image_anchor = 0,0
        cloudlayer2.velocity = 25,0
        cloudlayer2.do(WrappedMove(Globals.VID_WIDTH, Globals.VID_HEIGHT))

        self.add(cloudlayer2)
        self.add(cloudlayer1)

