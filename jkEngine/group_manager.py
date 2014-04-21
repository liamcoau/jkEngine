class GroupManager():
    def __init__ (self, world):
        self.world = world
        self.groups = {}

    def addGroup (self, group):
        if not group in self.groups.keys():
            self.groups[group] = []

    def removeGroup (self, group):
        del self.groups[group]

    def isGroup (self, groupName):
        return groupName in self.groups.keys()

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
