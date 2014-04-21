import jkEngine.sfml as sf
from jkEngine.jk import *
from jkEngine.utils import Vector, Sprite2D

#import systems
from jkEngine.systems_library.player_system import *
from jkEngine.systems_library.map_system import *
from jkEngine.systems_library.physics_collision_system import *
from jkEngine.systems_library.camera_system import *
from jkEngine.systems_library.gui_system import *
from jkEngine.systems_library.render_system import *

jk = Jk(640, 360, "Example Game")

#add component types
jk.world.entityManager.defineComponentType("sprite", Sprite2D)
jk.world.entityManager.defineComponentType("position", Vector)
jk.world.entityManager.defineComponentType("collision", list)
jk.world.entityManager.defineComponentType("rotation", float)
jk.world.entityManager.defineComponentType("physics", dict)

#add systems
jk.world.sysManager.addSys(PlayerSystem())
jk.world.sysManager.addSys(MapSystem())
jk.world.sysManager.addSys(PhysicsCollisionSystem())
jk.world.sysManager.addSys(CameraSystem())
jk.world.sysManager.addSys(GUISystem())
jk.world.sysManager.addSys(RenderSystem())

jk.start()
