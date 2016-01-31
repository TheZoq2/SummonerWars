from cocos.actions import *

class Remove(InstantAction):

    def start(self):
        self.target.kill()

class ColorLerp(IntervalAction):

    def init(self, from_color, to_color, duration):
        super(ColorLerp, self).init(duration)
        self.from_color = from_color
        self.to_color = to_color
        self.duration = duration

    def update(self, t):
        r = self.to_color[0] * t + self.from_color[0] * (1-t)
        g = self.to_color[1] * t + self.from_color[1] * (1-t)
        b = self.to_color[2] * t + self.from_color[2] * (1-t)
        self.target.color = r,g,b

class UpdateAction(InstantAction):

    def init(self):
        pass

    def start(self):
        pass
