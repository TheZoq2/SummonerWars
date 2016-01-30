import cocos

class Background(cocos.layer.Layer):

    BACKGROUND_IMAGE = "Assets/background.png"

    def __init__(self):
        super(Background, self).__init__()

        background = cocos.sprite.Sprite(self.BACKGROUND_IMAGE)
        background.position = 1280/2,720/2
        self.add(background)
