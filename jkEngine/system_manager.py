from jkEngine.abstracts import System, TickSystem
from jkEngine.utils import getClassName

class SystemManager:
    def __init__ (self, world):
        self.world = world
        self.systems = {}

    #Methods
    def addSys (self, system):
        if not isinstance(system, System): raise TypeError
        else: self.systems[getClassName(system) + "_" + str(len(self.systems))] = system
        system.init(self.world)

    def update (self):
        for key in self.systems.keys():
            if self.systems[key].active:
                if isinstance(self.systems[key], TickSystem):
                    self.systems[key].callTick()

    def startSys (self, *systems):
        if len(systems) == 0:
            for key in self.systems.keys():
                self.systems[key].start()
        else:
            for key in range(systems):
                self.systems[systems[key]].start()

    def stopSys (self, *systems):
        if len(systems) == 0:
            for key in self.systems.keys():
                self.systems[key].stop()
        else:
            for key in range(systems):
                self.systems[systems[key]].stop()
