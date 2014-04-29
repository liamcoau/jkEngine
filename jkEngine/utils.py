from jkEngine.sfml import Sprite, Rectangle, Vector2, Texture
from math import sqrt

def getClass (classOrInstance):
    if type(classOrInstance) is type: return classOrInstance
    else: return classOrInstance.__class__

def getClassName (classOrInstance):
    if type(classOrInstance) is type: return classOrInstance.__qualname__
    else: return classOrInstance.__class__.__qualname__

def vectConst (vector, constant):
    if isinstance(vector, Vector) and (type(constant) is float or type(constant) is int):
        return vector.copy().scale(constant)
    else:
        if not isinstance(vector, Vector):
            print("Class of {0}, {1}, is not Vector. (utils.py:vectConst)".format(vector, getClass(vector)))
        else:
            print("Type of {0}, {1}, is not float or int. (utils.py:vectConst)".format(constant, type(constant)))

def vectSum (vectorSet):
    length = 0
    for index in range(len(vectorSet)):
        vect = vectorSet[index]
        if isinstance(vect, Vector):
            if len(vect) > length:
                length = len(vect)
        else:
            print("Class of {0}, {1}, is not Vector. (utils.py:vectSum)".format(vect, getClass(vect)))
            del vectorSet[index]
    result = Vector([0.0] * length)
    for vect in vectorSet:
        result.add(vect)
    return result

def vectAddVect (vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1.copy().add(vector2)
    else:
        if not isinstance(vector1, Vector):
            print("Class of {0}, {1}, is not Vector. (utils.py:vectAddVect)".format(vector1, getClass(vector1)))
        else:
            print("Class of {0}, {1}, is not Vector. (utils.py:vectAddVect)".format(vector2, getClass(vector2)))

def vectSubVect (vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1.copy().sub(vector2)
    else:
        if not isinstance(vector1, Vector):
            print("Class of {0}, {1}, is not Vector. (utils.py:vectSubVect)".format(vector1, getClass(vector1)))
        else:
            print("Class of {0}, {1}, is not Vector. (utils.py:vectSubVect)".format(vector2, getClass(vector2)))

def dot (vector1, vector2):
    if isinstance(vector1, Vector) and isinstance(vector2, Vector):
        return vector1.copy().dot(vector2)
    else:
        if not isinstance(vector1, Vector):
            print("Class of {0}, {1}, is not Vector. (utils.py:dot)".format(vector1, getClass(vector1)))
        else:
            print("Class of {0}, {1}, is not Vector. (utils.py:dot)".format(vector2, getClass(vector2)))

class Vector(list):
    def __init__ (self, *elements):
        for element in elements:
            if type(element) is float:
                list.append(self, element)
            elif type(element) is list:
                for index in element:
                    if type(index) is float:
                        list.append(self, index)
                    elif type(index) is int:
                        list.append(self, float(index))
            elif type(element) is tuple:
                for index in element:
                    if type(index) is float:
                        list.append(self, index)
                    elif type(index) is int:
                        list.append(self, float(index))
            elif type(element) is int:
                list.append(self, float(element))
            elif type(element) is Vector2:
                list.append(self, element.x)
                list.append(self, element.y)

    def __iter__ (self):
        class Iterator:
            def __init__ (self, elements):
                self.elements = elements
                self.counter = 0
            def __iter__ (self):
                return self
            def __next__ (self):
                if self.counter == len(self.elements):
                    raise StopIteration
                else:
                    self.counter += 1
                    return self.elements[self.counter - 1]
        return Iterator(self[:])
    
    def set (self, vector):
        if isinstance(vector, Vector):
            self.add(vector.copy().sub(self))
    
    def scaleTo (self, constant):
        self.scale(constant / self.len())
        return self.copy()
    
    def len (self):
        return sqrt(self.dot(self))

    def add (self, vector):
        if isinstance(vector, Vector):
            for index in range(len(self) if len(self) <= len(vector) else len(vector)):
                self[index] += vector[index]
            return self.copy()
        else:
            print("Class of {0}, {1}, is not Vector. (utils.py:Vector.add)".format(vector, getClass(vector)))

    def sub (self, vector):
        if isinstance(vector, Vector):
            for index in range(len(self) if len(self) <= len(vector) else len(vector)):
                self[index] -= vector[index]
            return self.copy()
        else:
            print("Class of {0}, {1}, is not Vector. (utils.py:Vector.sub)".format(vector, getClass(vector)))

    def scale (self, constant):
        if type(constant) is float or type(constant) is int:
            for index in range(len(self)):
                self[index] *= constant
            return self.copy()
        else:
            print("Type of {0}, {1}, is not either float or int. (utils.py:Vector.scale)".format(constant, type(constant)))

    def dot (self, vector):
        total = 0.0
        if isinstance(vector, Vector):
            for index in range(len(self) if len(self) <= len(vector) else len(vector)):
                total += self[index] * vector[index]
            return total
        else:
            print("Class of {0}, {1}, is not Vector. (utils.py:Vector.dot)".format(vector, getClass(vector)))

    def copy (self):
        return Vector(self[:])

class Sprite2D(Sprite):
    animation = False
    zindex = 0

    def setZindex (self, zindex):
        if type(zindex) is int:
            self.zindex = zindex
    
    def setAnimation (self, animation):
        if isinstance(animation, Animation):
            self.animation = animation
    
class Animation():
    def __init__ (self, sprite, animLength, width, height, columns, framesNumber):
        self.sprite = sprite
        self.animLength = animLength
        self.current = 0
        self.time = 0.0
        self.frames = []
        self.paused = False
        rows = framesNumber // columns
        if (framesNumber % columns) > 0:
            rows += 1
        for row in range(rows):
            if len(self.frames) + columns > framesNumber:
                for column in range(framesNumber % columns):
                    self.frames.append([((column*(width//columns))+1,(row*(height//rows))+1),(width//columns,height//rows)])
            else:
                for column in range(columns):
                    self.frames.append([((column*(width//columns))+1,(row*(height//rows))+1),(width//columns,height//rows)])
        
    def getFrame (self, deltaTime):
        if not self.paused:
            self.time += deltaTime
        if self.time >= self.animLength:
            self.time -= self.animLength
            self.current = 0
        elif (self.time - (self.current * self.animLength / len(self.frames))) > (self.animLength / len(self.frames)):
            self.current += 1
        self.sprite.texture_rectangle = Rectangle(self.frames[self.current][0], self.frames[self.current][1])
        return self.sprite
    
    def setFrames (self, frames):
        self.frames = frames
    
    def pause (self, paused):
        if paused == True:
            self.paused = True
        elif paused == False:
            self.paused = False
