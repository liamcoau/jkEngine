import jkEngine.sfml as sf
from jkEngine.world import *
from jkEngine.abstracts import Config

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

    #Main loop function
    def start (self):
        if len(self.startups) > 0:
            for startup in self.startups:
                startup()
        #self.playerInput = PlayerInput("PlayerInput.ini")

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
    def attachStartup (self, startupFunction):
        self.startups.append(startupFunction)
        
    def attachUpdate (self, updateFunction):
        updateList.append(updateFunction)

    def addSys (self, system):
        self.world.sysManager.addSys(system)

    def getGraphicsAccess (self):
        return self.w
    
    def exit (self):
        self.w.close()

    @staticmethod
    def getClock ():
        return sf.Clock()
        
if __name__ == "__main__":
    #If jk.py is run, this will open an example
    jk = Jk(400, 400, "jk Engine Example")
    jk.start()
