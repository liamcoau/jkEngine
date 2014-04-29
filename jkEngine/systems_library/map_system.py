from jkEngine.abstracts import MapSystem
from jkEngine.sfml import Image, Texture, Color, Vector2, RectangleShape
from jkEngine.utils import Vector, Sprite2D

class MapSystem (MapSystem):
	def __init__ (self):
		#Attributes
		self.aspectTypes = ["position"]
		texture = Texture.from_file("jkEngine/resources/Example Game/background.png")
		self.background = Sprite2D(texture)
		self.background.setZindex(-1)
		self.groundBlock = Sprite2D(Texture.from_image(Image.create(2000, 100, Color.GREEN)))
		self.groundBlock.setZindex(1)
		super().__init__()
	
	def init (self, world):
		super().init(world)
		self.worldEntity = self.world.entityManager.newEntity()
		self.world.tagManager.setTag(self.worldEntity, "ground geometry")
		self.worldEntity.addComponent(Vector(0, 310), "position")
		self.worldEntity.addComponent(0.0, "rotation")
		self.worldEntity.addComponent(self.groundBlock, "sprite")
		self.worldEntity.addComponent([{1: [[RectangleShape((2000, 100)), (0, 0)]]}, {}], "collision")
		self.backgroundEntity = self.world.entityManager.newEntity()
		self.backgroundEntity.addComponent(Vector(0,0), "position")
		self.backgroundEntity.addComponent(0.0, "rotation")
		self.backgroundEntity.addComponent(self.background, "sprite")
		self.background.offset = Vector(640, 360)
		self.g = self.world.engine.getGraphicsAccess()
		self.g.draw(self.groundBlock)
		self.pawn = self.world.tagManager.getID("Pawn")
		
	def tick (self, deltaTime):
		self.background.position = self.aspect["position"][self.world.tagManager.getID("PlayerCamera")]
		self.g.draw(self.groundBlock)