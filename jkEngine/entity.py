class Entity:
    def __init__ (self, id, world):
        self.id = id
        self.world = world
    
    #Methods
    def addComponent (self, component, componentType):
        self.world.entityManager.addComponent(self, component, componentType)

    def removeComponent (self, component, componentType):
        self.world.entityManager.removeComponent(self, component, componentType)
