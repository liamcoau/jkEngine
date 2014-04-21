from jkEngine.abstracts import MapSystem
from jkEngine.sfml import Image, Texture, Sprite, Color, Vector2, RectangleShape
from jkEngine.utils import Vector

class MapSystem (MapSystem):
	def __init__ (self):
		#Attributes
		self.aspectTypes = []
		self.groundBlock = Sprite(Texture.from_image(Image.create(2000, 100, Color.GREEN)))
		self.groundBlock.position = Vector(0, 310)
		super().__init__()
	
	def init (self, world):
		super().init(world)
		self.worldEntity = self.world.entityManager.newEntity()
		self.worldEntity.addComponent(Vector(0, 310), "position")
		self.worldEntity.addComponent([{1: [[RectangleShape((2000, 100)), (0, 0)]]}, {}], "collision")
		self.g = self.world.engine.getGraphicsAccess()
		self.g.draw(self.groundBlock)
		self.pawn = self.world.tagManager.getID("Pawn")
		
	def tick (self, deltaTime):
		self.g.draw(self.groundBlock)