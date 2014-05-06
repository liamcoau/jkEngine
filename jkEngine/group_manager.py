from jkEngine.entity import Entity

#Allows you to create and organize groups of entities under a name.
class GroupManager():
    def __init__ (self, world):
        self.world = world
        self.groups = {}

    #Create a new group.
    def addGroup (self, group):
        if not group in self.groups.keys():
            self.groups[group] = []

    #Delete a group.
    def removeGroup (self, group):
        del self.groups[group]

    #Test to see if a string is the name of a group.
    def isGroup (self, groupName):
        return groupName in self.groups.keys()
    
    #Test to see if an entity is in the group
    def isInGroup (self, entity, group):
        if type(entity) is int:
            if group in self.groups.keys():
                return entity in self.groups[group]
            else:
                print("When attempting to add entity {0} to group '{1}', group did not exist".format(entity, group))
        elif isinstance(entity, Entity):
            if group in self.groups.keys():
                return entity.id in self.groups[group]
            else:
                print("When attempting to add entity {0} to group '{1}', group did not exist".format(entity.id, group))
    
    #Add an entity to a group
    def addToGroup (self, entity, group):
        if type(entity) is int:
            if group in self.groups.keys():
                self.groups[group].append(entity)
            else:
                print("When attempting to add entity {0} to group '{1}', group did not exist".format(entity, group))
        elif isinstance(entity, Entity):
            if group in self.groups.keys():
                self.groups[group].append(entity.id)
            else:
                print("When attempting to add entity {0} to group '{1}', group did not exist".format(entity.id, group))
