from jkEngine.abstracts import Spawnable, Config
from jkEngine.utils import Vector, Sprite2D, Animation
from jkEngine.sfml import Texture, Sprite, RectangleShape

class Pawn(Spawnable, Config):
    def __init__ (self):
        self.tag = "Pawn"
        #load stuff from config file - default_texture
        self.default_texture_file = "jkEngine/resources/Example Game/char_walking3.png"
    
    def initComponents (self, kwargs, tagManager, groupManager):
        components = {}
        ###Position###
        position = kwargs.get("position")
        if not isinstance(position, Vector):
            position = Vector(0.0, 0.0)
        components["position"] = position
        ###Rotation###
        rotation = kwargs.get("rotation")
        if type(rotation) is float:
            components["rotation"] = rotation
        else:
            components["rotation"] = 0.0
        ###Physics###
        physics = kwargs.get("physics")
        if type(physics) is dict:
            components["physics"] = physics
        else:
            components["physics"] = {"mass": 50.0, "velocity": Vector(0.0, 0.0), "momentum": Vector(0.0, 0.0), "previous": position, "lastdTime": 1.0, "forces": [], "Ek": 0.0, "Ep": 0.0}
        ###Collision###
        collision = kwargs.get("collision")
        if type(collision) is list:
            components["collision"] = collision
        else:
            components["collision"] = [{1: [[RectangleShape((80, 120)), (-40, -60)]]}, {}]
        ###Sprite###
        sprite = kwargs.get("sprite")
        if isinstance(sprite, Sprite2D):
            components["sprite"] = sprite
        else:
            texture = Texture.from_file(self.default_texture_file)
            sprite = Sprite2D(texture, 0)
            sprite.position = components["position"]
            sprite.rotation = components["rotation"]
            sprite.zindex = 1
            sprite.setAnimation(Animation(sprite, 0.7, texture.width, texture.height, 8, 8))
            sprite.origin = (40, 60)
            components["sprite"] = sprite
        ###Tag###
        if not kwargs.get("tag") == None:
            self.tag = kwargs.get("tag")
        return components
