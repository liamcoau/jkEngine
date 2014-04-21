from jkEngine.abstracts import TickSystem
from jkEngine.utils import Sprite2D
import jkEngine.sfml as sf

class RenderSystem (TickSystem):
    def __init__ (self):
        #Attributes
        self.aspectTypes = ["sprite", "position", "rotation", "collision"]
        self.zindices = {}
        self.drawCollision = False
        super().__init__()

    def init (self, world):
        super().init(world)
        self.g = self.world.engine.getGraphicsAccess()

    def tick (self, deltaTime):
        sprites = self.aspect["sprite"]
        for index in sprites.keys():
            sprite = sprites[index]
            if isinstance(sprite, Sprite2D):
                sprite.position = self.aspect["position"][index]
                sprite.rotation = self.aspect["rotation"][index]
                if sprite.zindex in self.zindices.keys():
                    self.zindices[sprite.zindex].append(sprite)
                else:
                    self.zindices[sprite.zindex] = [sprite]
        sortedzindices = []
        for index in self.zindices.keys():
            sortedzindices.append(index)
        sortedzindices.sort()
        for index in sortedzindices:
            for sprite in self.zindices[index]:
                if not sprite.animation:
                    self.g.draw(sprite)
                else:
                    self.g.draw(sprite.animation.getFrame(deltaTime))
        self.zindices = {}
        if self.drawCollision:
            for key in self.aspect["collision"].keys():
                self.g.draw(self.aspect["collision"][key][0][1][0][0])
