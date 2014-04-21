class PlayerInput(Config):
    #Attributes
    selfName = "Engine.PlayerInput"
    configFile = None
    keys = {"0":"A","1":"B","2":"C","3":"D","4":"E","5":"F","6":"G","7":"H","8":"I","9":"J","10":"K","11":"L","12":"M","13":"N","14":"O","15":"P","16":"Q","17":"R","18":"S","19":"T","20":"U","21":"V","22":"W","23":"X","24":"Y","25":"Z"}
    binds = {"W":"fwd","A":"sleft","S":"back","D":"sright"}
    fwd = False
    sleft = False
    back = False
    sright = False
    
    #Constructor
    def __init__ (self, configFile):
        self.config(configFile)
        #key = None
        #value = None
        #self.configFile = configFile
        #for line in open(configFile):
            #if line[0] == ";" or line[0] == "\\":
                #pass
            #elif line[0] == "[":
                #pass
            #else:
                #exec(line, {"__builtins__": {"self": self, "print": print}}, self.classLocals)
        #Test all keys etc
        #Read keybinds from file
        #Write keys and binds arrays
        #exec("self.A = True")
        #print(self.A)

    #Methods
    def update (self, events):
        for event in events:
            if type(event) is sf.KeyEvent:
                print(event.code)
                if event.pressed:
                    setattr(self, self.binds[self.keys[str(event.code)]], True)
                elif event.released:
                    setattr(self, self.binds[self.keys[str(event.code)]], False)

    def handle (self, keypress):
        print(keypress.code)
        if keypress.pressed:
            setattr(self, self.binds[self.keys[str(keypress.code)]], True)
        elif keypress.released:
            setattr(self, self.binds[self.keys[str(keypress.code)]], False)