from jkEngine.abstracts import TickSystem
import sfml as sf

class GUISystem(TickSystem):
    def __init__ (self):
        #Attributes
        self.aspectTypes = []
        super().__init__()

    def init (self, world):
        super().init(world)
        self.g = self.world.engine.getGraphicsAccess()
        
    def tick (self, deltaTime):
        pass
        #fps = sf.Text("FPS: " + str(1/deltaTime))
        #fps.character_size = 100
        #ps.font = sf.Font.from_file("arial.ttf")
        #fps.style = sf.Text.BOLD
        #fps.color = sf.Color.WHITE
        #fps.position = (100, 500)
        #print(fps.font)
        #self.g.draw(fps)