#Base class for  entities. Essentially just a wrapper for the ID. Methods will be removed to adhere to Entity System design philosophy.
class Entity:
    def __init__ (self, id, world):
        self.id = id
        self.world = world
    
    #Methods
    def addComponent (self, component, componentType):
        self.world.entityManager.addComponent(self, component, componentType)

    def removeComponent (self, component, componentType):
        self.world.entityManager.removeComponent(self, component, componentType)
