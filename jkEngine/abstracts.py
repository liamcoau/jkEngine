from abc import ABCMeta

#Component class is not actually currently used for anything, supposed to be used as base class for all component types.
class Component(metaclass=ABCMeta):
    pass


#Inheriting the Config class will give systems the ability to read from .ini files.
class Config(metaclass=ABCMeta):
    #Attributes
    selfName = None
    classLocals = locals()
    #classLocals["classLocals"] = None

    #Methods
    def config (self, configFile):
        selected = False
        key = None
        value = None
        print(self.classLocals)
        print(self.classLocals["classLocals"])
        if configFile[-4:] == ".ini":
            for line in open(configFile):
                line = line.strip()
                if line[0] == "[":
                    if line[1:-1] == self.selfName:
                        selected = True
                    elif selected == True:
                        selected = False
                elif not line[0] == ";" or line[0] == "\\":
                    if selected:
                        if "=" in line:
                            key = line[:line.index("=")]
                            key.strip()
                            value = line[line.index("=")+1:]
                            value.strip()
                            if hasattr(self, key):
                                self.key = value
                            else:
                                print("No attribute {0} of {1}. (abstracts.py:Config.config".format(key, self))
                    else:
                        pass #wtf is with this line dude, get it fixed
        else:
            pass

#Used for classes which run every frame and do calculations involving time.
class TickClass(metaclass=ABCMeta):
    def __init__ (self):
        from jkEngine.jk import Jk
        self.clock = Jk.getClock()
        self.lastTime = self.clock.elapsed_time.seconds

    #Methods
    def callTick (self):
        time = self.clock.elapsed_time.seconds
        self.tick(time - self.lastTime)
        self.lastTime = time

    def tick (self, dTime):
        pass

#Base class for all systems, with some basic functionality.
class System(metaclass=ABCMeta):
    #Need to keep here because __init__ isn't run by child classes
    aspect = []
    active = False

    def init (self, world):
        self.world = world
        assert not type(self.aspectTypes) is None
        self.aspect = self.world.entityManager.getAspect(self.aspectTypes)

    def start (self):
        self.active = True

    def stop (self):
        self.active = False

#Base classes which can be spawned by systems.
class Spawnable(metaclass=ABCMeta):
    def initComponents (self, kwargs):
        #Initialize components with info from kwargs
        components = {}
        return components

#Systems which want to use TickClass extend from here.
class TickSystem(System, TickClass):
    def init (self, world):
        super().init(world)

#Systems only for processing entities (tag, group).
class EntitySystem(System):
    pass

#Systems which run every specific time or frame interval.
class IntervalSystem(System):
    pass

#Systems which are triggered by events.
class TriggerSystem(System):
    def trigger (self, event):
        pass

#Systems controlling the map.
class MapSystem(TickSystem):
    pass
