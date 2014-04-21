from jkEngine.entity import *

class TagManager():
    def __init__ (self, world):
        self.world = world
        self.tags = {}
        self.reverseTags = {}

    def getID (self, tag):
        assert self.tags[tag] == self.tags[self.reverseTags[self.tags[tag]]]
        return self.tags[tag]

    def getTag (self, entity):
        if type(entity) is int:
            #assert
            return self.reverseTags[entity]
        elif isinstance(entity, Entity):
            #assert
            return self.reverseTags[entity.id]
            
    def setTag (self, entity, tag):
        if type(entity) is int:
            self.tags[tag] = entity
            self.reverseTags[entity] = tag
        elif isinstance(entity, Entity):
            self.tags[tag] = entity.id
            self.reverseTags[entity.id] = tag
