from jkEngine.abstracts import TickSystem
from jkEngine.spawnables_library.pawn import *
from jkEngine.abstracts import Config
from jkEngine.utils import Vector

class PlayerSystem(TickSystem, Config):
    def __init__ (self):
        self.aspectTypes = []
        self.selfName = "Engine.PlayerSystem"
        self.configFile = ""
        self.keys = {"0":"A","1":"B","2":"C","3":"D","4":"E","5":"F","6":"G","7":"H","8":"I","9":"J","10":"K","11":"L","12":"M","13":"N","14":"O","15":"P","16":"Q","17":"R","18":"S","19":"T","20":"U","21":"V","22":"W","23":"X","24":"Y","25":"Z"}
        self.binds = {"W":"fwd","A":"sleft","S":"back","D":"sright"}
        #self.binds = {}
        super().__init__()

    def setBinds (self):
        self.fwd = False
        self.sleft = False
        self.back = False
        self.stright = False

    def handle (self, keypress):
        print(keypress.code)
        if keypress.pressed:
            setattr(self, self.binds[self.keys[str(keypress.code)]], True)
        elif keypress.released:
            setattr(self, self.binds[self.keys[str(keypress.code)]], False)

    def init (self, world):
        super().init(world)
        self.world.spawn(Pawn, tag="Pawn", position=Vector(50,50), collision=[{1: [[RectangleShape((80, 120)), (-40, -60)]]}, {"collide": self.pawnCollide}])
        
    def pawnCollide (self, event):
        print("Pawn Collide!!")
