from jkEngine.abstracts import TickSystem
from jkEngine.spawnables_library.pawn import *
from jkEngine.abstracts import Config
from jkEngine.utils import Vector, Animation

class PlayerSystem(TickSystem, Config):
    def __init__ (self):
        self.aspectTypes = []
        self.selfName = "Engine.PlayerSystem"
        self.configFile = ""
        self.keys = {"0":"A","1":"B","2":"C","3":"D","4":"E","5":"F","6":"G","7":"H","8":"I","9":"J","10":"K","11":"L","12":"M","13":"N","14":"O","15":"P","16":"Q","17":"R","18":"S","19":"T","20":"U","21":"V","22":"W","23":"X","24":"Y","25":"Z"}
        self.binds = {"W":"fwd","A":"sleft","S":"back","D":"sright","E":"jump"}
        self.setBinds()
        self.state = "jumping"
        self.canJump = False
        self.lastJump = 0.0
        super().__init__()

    def setBinds (self):
        self.fwd = False
        self.sleft = False
        self.back = False
        self.sright = False
        self.jump = self.pawnJump
    
    def pawnJump (self, keypress):
        if keypress.pressed and self.canJump and (self.clock.elapsed_time.seconds - self.lastJump) > 0.5:
            print((self.clock.elapsed_time.seconds - self.lastJump))
            self.canJump = False
            print("jump!")
            self.pawn["physics"]["impulses"].append(Vector(0, -10000))
            self.lastJump = self.clock.elapsed_time.seconds            
        
    def tick (self, deltaTime):
        if self.state == "walking":
            self.pawn["sprite"].animation.pause(False)
            self.pawn["physics"]["forces"].append(Vector(2000, 0))
        else:
            self.pawn["sprite"].animation.pause(True)
        self.state = "jumping"

    def handle (self, keypress):
        #print(getattr(self, self.binds[self.keys[str(keypress.code)]]))
        if type(getattr(self, self.binds[self.keys[str(keypress.code)]])) is bool:
            if keypress.pressed:
                setattr(self, self.binds[self.keys[str(keypress.code)]], True)
            elif keypress.released:
                    setattr(self, self.binds[self.keys[str(keypress.code)]], False)
        elif hasattr(getattr(self, self.binds[self.keys[str(keypress.code)]]), "__call__"):
            getattr(self, self.binds[self.keys[str(keypress.code)]]).__call__(keypress)

    def init (self, world):
        super().init(world)
        self.pawn = self.world.entityManager.getEntityInfo(self.world.spawn(Pawn, tag="Pawn", position=Vector(50,50), collision=[{1: [[RectangleShape((80, 120)), (-40, -60)]]}, {"collide": self.pawnCollide}]))
        
    def pawnCollide (self, event):
        if self.world.tagManager.getTag(event.other) == "ground geometry":
            self.state = "walking"
            if not self.canJump:
                print("lol")
            self.canJump = True
            #print("Pawn Collide!!")
