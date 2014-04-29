from jkEngine.entity_manager import *
from jkEngine.system_manager import *
from jkEngine.tag_manager import *
from jkEngine.group_manager import *
from jkEngine.abstracts import Spawnable, MapSystem
from jkEngine.utils import getClassName, getClass

class World:
    #Constructor
    def __init__ (self, engine):
        #Attributes
        self.engine = engine
        self.entityManager = EntityManager(self)
        self.sysManager = SystemManager(self)
        self.tagManager = TagManager(self)
        self.groupManager = GroupManager(self)
        self.map = None
        def startup ():
            self.sysManager.startSys()
        self.engine.attachStartup(startup)
        
    #Methods        
    def spawn (self, spawnClass, **kwargs):
        if issubclass(spawnClass, Spawnable):
            entity = self.entityManager.newEntity()
            spawnable = spawnClass()
            components = spawnable.initComponents(kwargs, self.tagManager, self.groupManager)

            for comp in components.keys():
                self.entityManager.addComponent(entity.id, components[comp], comp)
            if hasattr(spawnable, "tag"):
                self.tagManager.setTag(entity, spawnable.tag)
            if hasattr(spawnable, "groups"):
                if type(groups) is list:
                    for group in groups:
                        if self.groupManager.isGroup(group):
                            self.groupManager.addToGroup(entity.id, group)
                        else:
                            self.groupManager.addGroup(group)
                            self.groupManager.addToGroup(entity.id, group)
                elif type(groups) is str:
                    if self.groupManager.isGroup(groups):
                            self.groupManager.addToGroup(entity.id, groups)
                    else:
                        self.groupManager.addGroup(groups)
                        self.groupManager.addToGroup(entity.id, groups)
            return entity
        else: print("{0} is not a subclass of Spawnable.".format(getClassName(spawnClass)))
        
    def addSys (self, system):
        self.sysManager.addSys(system)

    def update (self):
        self.sysManager.update()

    def addMapSys (self, map_system):
        #Map should already be added to System Manager
        if self.map is None:
            if isinstance(map_system, MapSystem):
                self.map = map_system
            else:
                print("Class of {0}, {1}, is not instance of MapSystem. (world.py:World.addMapSys)".format(map_system, getClass(map_system)))
        else:
            print("Map is already added. (world.py:World.addMapSys)")
