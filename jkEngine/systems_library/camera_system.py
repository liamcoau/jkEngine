from jkEngine.abstracts import TickSystem
import jkEngine.sfml as sf
from jkEngine.utils import Vector, vectSubVect, vectAddVect
from jkEngine.spawnables_library.camera import Camera

class CameraSystem (TickSystem):
    def __init__ (self):
        self.aspectTypes = []
        self.cameraVelocity = 200
        self.width = 1280
        self.height = 720
        super().__init__()

    def init (self, world):
        super().init(world)
        self.g = self.world.engine.getGraphicsAccess()
        self.cam = self.world.entityManager.getEntityInfo(self.world.spawn(Camera, tag="PlayerCamera")) #Getting the whole entity
        self.pawn = self.world.entityManager.getEntityInfo(self.world.tagManager.getID("Pawn"))

    def tick (self, dTime):
        view = sf.View()
        aim = self.pawn["position"]
        if vectSubVect(aim, self.cam["position"]).len() > self.cameraVelocity * dTime:
            self.cam["position"].add(vectSubVect(aim, self.cam["position"]).scaleTo(self.cameraVelocity * dTime))
        else:
            self.cam["position"].set(aim)
        view.reset(sf.Rectangle(self.cam["position"], (self.width, self.height)))
        view.center = (view.center[0] - (self.width // 2), view.center[1] - (self.height // 2))
        view.rotate(0)
        self.g.view = view