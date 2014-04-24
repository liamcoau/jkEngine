from jkEngine.abstracts import TickSystem
from jkEngine.utils import vectSum, vectAddVect, vectSubVect, vectConst, dot, Vector
from jkEngine.sfml import CircleShape, RectangleShape

class PhysicsCollisionSystem (TickSystem):
    def __init__ (self):
        #Attributes
        self.aspectTypes = ["physics", "position", "rotation", "collision"]
        self.leftover = 0.0
        self.zindices = {}
        super().__init__()

    def tick (self, dTime):
        self.collision(dTime)
        #times = (dTime + self.leftover) // 0.01
        #self.leftover = (dTime + self.leftover) % 0.01
        #for index in range(int(times)):
        for key in self.aspect["physics"].keys():
            self.verlet(key, dTime)
            self.aspect["physics"][key]["lastdTime"] = dTime
        for key in self.aspect["physics"].keys():
            comp = self.aspect["physics"][key]
            #1 pixel = 1 dm
            comp["forces"] = [Vector(0.0, 98.1 * comp["mass"])]

    def verlet (self, key, dTime):
        if self.aspect["physics"][key]["mass"] <= 0.0 or not type(self.aspect["position"][key]) is Vector:
            return
        pos = self.aspect["position"][key]
        phys = self.aspect["physics"][key]
        velocity = pos.copy().sub(phys["previous"]).scale(dTime/phys["lastdTime"])
        phys["previous"] = pos.copy()
        accel = vectSum(phys["forces"]).scale(1 / phys["mass"])
        #print("{0} = dTime, {1} = accel, {2} = vel, {3} = pos".format(dTime, accel.copy().scale(dTime * dTime), velocity.copy().scale(1/dTime), pos))
        pos.add(velocity.add(accel.scale(dTime * dTime)))

    #Will not work without vector class
    def euler (self, key, dTime):
        #halfStep doesn't need self parameter
        def halfStep (comp, pos, rot, dTime):
            comp["velocity"][:] = vectSum([comp["velocity"], vectConst(vectSum(comp["forces"]), 1 / (2 * comp["mass"]))])[:]
            #pos = vectSum replaced the address of the name and didn't affect the original vector
            pos[:] = vectSum([pos, vectConst(comp["velocity"], 0.5 * dTime)])[:]
        comp = self.aspect["physics"][key]
        pos = self.aspect["position"][key]
        print(self.aspect["position"][key])
        halfStep(comp, pos, self.aspect["rotation"][key], dTime)
        halfStep(comp, pos, self.aspect["rotation"][key], dTime)
        #Should move back to tick
        comp["momentum"] = vectConst(comp["velocity"], comp["mass"])
        comp["Ek"] = 0.5 * comp["mass"] * dot(comp["velocity"], comp["velocity"])
        comp["Ep"] = 9.81 * comp["mass"] * self.aspect["position"][key][1]

    def collision (self, dTime):
        self.zindices = {}
        colls = self.aspect["collision"]
        for key in colls.keys():
            coll = colls[key][0]
            if isinstance(coll, dict):
                for index in coll.keys():
                    for element in coll[index]:
                        if key in self.aspect["position"]:
                            element[0].position = self.aspect["position"][key].copy().add(Vector(element[1]))
                        else:
                            print("Entity {0} has collision model but no position. (physics_collision_system.py:PhysicsCollisionSystem.collision)".format(key))
                    if index in self.zindices.keys():
                        self.zindices[index].append([coll[index], key])
                    else:
                        self.zindices[index] = [[coll[index], key]]
        sortedzindices = []
        for index in self.zindices.keys():
            sortedzindices.append(index)
        sortedzindices.sort()
        
        for index in sortedzindices:
            for i in range(len(self.zindices[index]) - 1):
                for j in range(i+1, len(self.zindices[index])):
                    #Handle multiple shapes in self.zindices[index][i][0]
                    #Do the box break
                    if self.colliding(self.zindices[index][i][0][0][0], self.zindices[index][j][0][0][0]):
                        self.resolve(self.zindices[index][i][0][0][0], self.zindices[index][j][0][0][0], i, j)
                        
    def resolve (self, shape1, shape2, ID1, ID2):
        if not ID1 in self.aspect["physics"].keys():
            tl1 = Vector(shape1.position)
            br1 = tl1.copy().add(Vector(shape1.size))
            tl2 = Vector(shape2.position)
            br2 = tl2.copy().add(Vector(shape2.size))
            self.aspect["position"][ID2][1] += tl1[1] - br2[1]
        elif not ID2 in self.aspect["physics"].keys():
            tl1 = Vector(shape1.position)
            br1 = tl1.copy().add(Vector(shape1.size))
            tl2 = Vector(shape2.position)
            br2 = tl2.copy().add(Vector(shape2.size))
            self.aspect["position"][ID1][1] += tl2[1] - br1[1]
    
    def colliding (self, shape1, shape2):
        def definitive ():
            return True
        
        if type(shape1) is RectangleShape and type(shape2) is RectangleShape:
            tl1 = Vector(shape1.position)
            br1 = tl1.copy().add(Vector(shape1.size))
            #print(tl1, br1)
            tl2 = Vector(shape2.position)
            br2 = tl2.copy().add(Vector(shape2.size))
            #print(tl2, br2)
            #print(tl2[0] >= tl1[0], tl2[0] <= br1[0])
            #print(br2[0] >= tl1[0], br2[0] <= br1[0])
            #print(tl2[1] >= tl1[1], tl2[1] <= br1[1])
            #print(br2[1] >= tl1[1], br2[1] <= br1[1])
            #print("###")
            if (tl2[0] >= tl1[0] and tl2[0] <= br1[0]) or (br2[0] >= tl1[0] and br2[0] <= br1[0]):
                if tl2[1] <= br1[1] and br2[1] >= tl1[1]:
                    return True
                else:
                    return False
            elif (tl2[1] >= tl1[1] and tl2[1] <= br1[1]) or (br2[1] >= tl1[1] and br2[1] <= br1[1]):
                if tl2[0] <= br1[0] and br2[0] >= tl1[0]:
                    return True
                else:
                    return False
            else:
                return False
        elif type(shape1) is RectangleShape and type(shape2) is CircleShape:
            return True
        elif type(shape1) is CircleShape and type(shape2) is RectangleShape:
            return True
        elif type(shape1) is CircleShape and type(shape2) is CircleShape:
            return True
        else:
            print("Shapes received not of proper type. (physics_collision_system.py:PhysicsCollisionSystem.colliding")
