from jkEngine.abstracts import Spawnable
from jkEngine.utils import Vector

class Camera (Spawnable):
    def __init__ (self):
        self.tag = "PlayerCamera"
        
    def initComponents (self, kwargs, tagManager, groupManager):
        components = {}
        position = kwargs.get("position")
        if not isinstance(position, Vector):
            position = Vector(40.0, 60.0)
        components["position"] = position
        rotation = kwargs.get("rotation")
        if type(rotation) is float:
            components["rotation"] = rotation
        else:
            components["rotation"] = 0.0
        physics = kwargs.get("physics")
        if type(physics) is dict:
            components["physics"] = physics
        else:
            components["physics"] = {"mass": 0.0, "velocity": Vector(0.0, 0.0), "momentum": Vector(0.0, 0.0), "previous": position, "lastdTime": 1.0, "forces": [], "Ek": 0.0, "Ep": 0.0}
        if not kwargs.get("tag") == None:
            self.tag = kwargs.get("tag")
        return components