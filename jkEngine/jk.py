import jkEngine.sfml as sf
from jkEngine.world import *
from jkEngine.abstracts import Config

#The engine itself. Start up jkEngine by creating an instance of Jk.
class Jk(Config):
    #Constructor
    def __init__ (self, width, height, gameName):
        #Attributes
        #Config stuff (1px = ?m)
        self.close = False
        self.startups = []
        self.updateList = []
        self.w = sf.RenderWindow(sf.VideoMode(width, height), gameName)
        self.w.clear()
        self.w.display()
        self.world = World(self)

    #Begins running the engine. Do when all component types and systems are set up.
    def start (self):
        if len(self.startups) > 0:
            for startup in self.startups:
                startup()

        while (not self.close):
            #Main loop
            for event in self.w.events:
                if type(event) is sf.CloseEvent:
                    self.close = True
                elif type(event) is sf.KeyEvent:
                    pass
                    self.world.sysManager.systems["PlayerSystem_0"].handle(event)
            if len(self.updateList) > 0:
                for function in updateList:
                    function()
            self.w.clear()
            self.world.update()
            #self.w.draw(sf.Sprite(sf.Texture.from_file("background.png")))
            self.w.display()
        self.w.close()

    #Methods
    
    #Given a function, will run it when the engine starts.
    def attachStartup (self, startupFunction):
        self.startups.append(startupFunction)
        
    #Given a function, will call it every cycle.
    def attachUpdate (self, updateFunction):
        updateList.append(updateFunction)

    #Passed on to the addSys method on the world object.
    def addSys (self, system):
        self.world.sysManager.addSys(system)

    #Will return the object of the window the engine is in.
    def getGraphicsAccess (self):
        return self.w
    
    #Immediately closes the window.
    def exit (self):
        self.w.close()

    #Returns an sfml clock.
    @staticmethod
    def getClock ():
        return sf.Clock()
        
#If this file is executed, this will open a small example window.
if __name__ == "__main__":
    jk = Jk(400, 400, "jk Engine Example")
    jk.start()
