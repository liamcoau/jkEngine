from jkEngine.abstracts import MapSystem
from jkEngine.sfml import Texture, Color, Vector2, RectangleShape
from jkEngine.utils import Vector, Sprite2D
import random, math

class MapSystem (MapSystem):
	def __init__ (self):
		#Attributes
		self.aspectTypes = ["position"]
		texture = Texture.from_file("jkEngine/resources/Example Game/background.png")
		self.background = Sprite2D(texture)
		self.background.setZindex(-1)
		self.currentBlocks = 0
		self.damageBlockTexture = Texture.from_file("jkEngine/resources/Example Game/damage_block.png")
		super().__init__()
	
	def init (self, world):
		super().init(world)
		self.worldEntity = []
		self.world.groupManager.addGroup("damage block")
		self.world.groupManager.addGroup("ground geometry")
		self.generateGround(Vector(-640, 232))
		#self.backgroundEntity = self.world.entityManager.newEntity()
		#self.backgroundEntity.addComponent(Vector(0,0), "position")
		#self.backgroundEntity.addComponent(0.0, "rotation")
		#self.background.offset = Vector(640, 360)
		#self.backgroundEntity.addComponent(self.background, "sprite")
		self.g = self.world.engine.getGraphicsAccess()
		self.pawn = self.world.tagManager.getID("Pawn")
		
	def generateGround (self, position):
		self.worldEntity.append(self.world.entityManager.newEntity())
		self.world.groupManager.addToGroup(self.worldEntity[-1], "ground geometry")
		self.worldEntity[-1].addComponent(position, "position")
		self.worldEntity[-1].addComponent(0.0, "rotation")
		groundBlockTexture = Texture.from_file("jkEngine/resources/Example Game/ground.png")
		groundBlock = Sprite2D(groundBlockTexture)
		groundBlock.setZindex(1)
		self.worldEntity[-1].addComponent(groundBlock, "sprite")
		self.worldEntity[-1].addComponent([{((self.currentBlocks % 3) + 1): [[RectangleShape((1280, 128)), (0, 0)]]}, {}], "collision")
		self.currentBlocks += 1
		if self.currentBlocks > 1:
			p1 = random.randrange(1216)
			p2 = random.randrange(1216)
			#p3 = random.randrange(1216)
			#p4 = random.randrange(1216)
			while (math.sqrt((p1 - p2) * (p1 - p2))) < 65:
				p2 = random.randrange(1280)
			self.generateDamageBlock(Vector((self.currentBlocks * 1280) + p1 - 1280, 232))
			self.generateDamageBlock(Vector((self.currentBlocks * 1280) + p2 - 1280, 232))
			#self.generateDamageBlock(Vector((self.currentBlocks * 1280) + p3 - 1280, 232))
			#self.generateDamageBlock(Vector((self.currentBlocks * 1280) + p4 - 1280, 232))
		
	def generateDamageBlock (self, position):
		block = self.world.entityManager.newEntity()
		self.world.groupManager.addToGroup(block, "damage block")
		block.addComponent(position, "position")
		block.addComponent(0.0, "rotation")
		
		damageBlock = Sprite2D(self.damageBlockTexture)
		damageBlock.setZindex(2)
		block.addComponent(damageBlock, "sprite")
		block.addComponent([{-1: [[RectangleShape((64, 64)), (0, 0)]]}, {}], "collision")
		
	def tick (self, deltaTime):
		#self.aspect["position"][self.backgroundEntity.id] = self.aspect["position"][self.world.tagManager.getID("PlayerCamera")].copy().add(Vector(-640, -360))
		location = self.aspect["position"][self.pawn] 
		if location[0] > (self.currentBlocks - 1) * 1280:
			self.generateGround(Vector((self.currentBlocks * 1280) - 640, 232))
		