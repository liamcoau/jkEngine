from jkEngine.utils import getClassName
from jkEngine.entity import *

#This catalogues and managers all of the data, and gives you an API for adding changing and removing it.
class EntityManager:
    def __init__ (self, world):
        self.world = world
        self.componentTypes = {} #Type -> Index
        self.componentClasses = []
        self.components = []
        self.entities = {}
        self.available = [] #Should test if more efficient

    #Used at startup to define which actual class is associated with the type names. ex: "sprite" -> Sprite2D
    def defineComponentType (self, componentType, componentClass):
        self.componentTypes[componentType] = len(self.components)
        self.componentClasses.append(componentClass)
        self.components.append({})
        #create type?
        #could add available list and removeComponentType

    #Used by systems at startup to get their aspects from their aspectTypes.
    def getAspect (self, aspectTypes):
        aspect = {}
        for key in aspectTypes:
            if key in self.componentTypes:
                aspect[key] = self.components[self.componentTypes[key]]
            else: print("{0} is not defined as a component type. (entity_manager.py:EntityManager.getAspect)".format(key))
        return aspect

    #Add a component for an entity.
    def addComponent (self, entity, component, componentType):
        if type(entity) is int:
            if isinstance(component, self.componentClasses[self.componentTypes[componentType]]):
                self.components[self.componentTypes[componentType]][entity] = component
            else:
                print("Type of component ({0}) does not match type of {1}: {2}. (entity_manager.py:EntityManager.addComponent)".format(type(component), componentType, self.componentClasses[self.componentTypes[componentType]]))

        elif isinstance(entity, Entity):
            if isinstance(component, self.componentClasses[self.componentTypes[componentType]]):
                self.components[self.componentTypes[componentType]][entity.id] = component
            else:
                print("Type of component ({0}) does not match type of {1}: {2}. (entity_manager.py:EntityManager.addComponent)".format(type(component), componentType, self.componentClasses[self.componentTypes[componentType]]))

    #Remove a component from an entity.
    def removeComponent (self, entity, componentType):
        if type(entity) is int:
            del self.components[self.componentTypes[componentType]][entity]

        elif isinstance(entity, Entity):
            del self.components[self.componentTypes[componentType]][entity.id]

    #Creates a new entity and returns it.
    def newEntity (self):
        if len (self.available) == 0:
            entityID = len(self.entities.keys())
        else:
            entityID = self.available.pop()
        self.entities[entityID] = Entity(entityID, self.world)
        return self.entities[entityID]

    #"Deletes" an entity and all of its components.
    def removeEntity (self, entity):
        if type(entity) is int:
            self.entities[entity] = None
            self.available.append(entity)
            
            #remove components
            for component in self.components:
                if entity in self.components[component]:
                    #could delete or leave, will set to delete for now
                    del self.components[component][entity]
        elif isinstance(entity, Entity):
            self.available.append(entity.id)
            self.entities[entity.id] = None
            
            #remove components
            for component in self.components:
                if entity.id in self.components[component]:
                    #could delete or leave, will set to delete for now
                    del self.components[component][entity.id]

    #Get the actual entity from its ID.
    def getEntity (self, entityID):
        return self.entities[entityID]

    #Returns all of an entity's components in a dict with component type as the key for each component.
    def getEntityInfo (self, entity):
        info = {}
        if type(entity) is int:
            for key in self.componentTypes.keys():
                comp = self.components[self.componentTypes[key]]
                if entity in comp.keys():
                    info[key] = comp[entity]
            return info
        elif isinstance(entity, Entity):
            for key in self.componentTypes.keys():
                comp = self.components[self.componentTypes[key]]
                if entity.id in comp.keys():
                    info[key] = comp[entity.id]
            return info
