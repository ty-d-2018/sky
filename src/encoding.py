from position.py import Volume
from metaMessage.py import Greeting

class Puff:
    def __init__(self):
        self.position = None
        self.edges = {}
        self.name = ""
        self.isActive = True
        self.msg = {}
        self.state = {}
        self.action = None

    def sayGreeting(self):
        activeStatus = "I am active" if self.isActive else "I am inactive"
        globalPos = f"(x: {self.getPosition("x")}, y: {self.getPosition("y")}, z: {self.getPosition("z")})"

        greeting = Greeting()
        greeting.addToMsg("Hello Sky and Ground")
        greeting.addSeperator("*", "\n\n")
        greeting.addStatus("My position is", globalPos, ":")
        greeting.addStatus(activeStatus, "", "")
        greeting.addStatus("I can call on", ":", f"#{len(self.edges)} friends and neighbors")
        greeting.addStatus("My name is", ":", self.name)
        greeting.addNewLine()
        greeting.addSeperator("+", "\n\n")

        print(greeting)

    def appendGreeting(self, prevMsg, nextMsg):
        return f"{prevMsg}{nextMsg}"

    def findPuff(self, name, candidate):
        if amIPuff(self.getPuff(candidate)):
            print("Puff here you are!")
        else:
            print("Puff not here")

    def amIPuff(self, tempName):
        if self.name == tempName:
            return True
        
        return False
    
    def getActive(self):
        return self.isActive

    def getPuff(self, key):
        return self.edges[key]

    def sendMsg(self, puffer):
        puffer.obtainMsg(self.state)
        
    def obtainMsg(self, msg):
        self.state = msg

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def addEdge(self, key, puff):
        self.edges[key] = puff

    def setMessage(self, msg):
        self.msg = msg


    def setPosition(self, x, y, z):
        self.position = Volume(x, y, z)

    def reverseActive(self):
        self.isActive = not self.isActive

    def setState(self, state):
        self.state = state

    def generate(self):
        pass

    def filterState(self, criteria):
        pass

    def initAction(self, action):
        self.action = action

    def activatePuffBehavior(self):
        (self.action)()

    def getPosition(self, key):
        volumeData = self.position.getData()

        return volumeData.get(key, 0.0)

class PuffBuilder:
    def __init__(self):
        self.puffer = Puff()

    def createOrigin(self, xx, yy, zz):
        origin = {
            "x": xx,
            "y": yy,
            "z": zz
        }

        return origin

    def buildDefault(self):
        self.createOrigin(10, 100, 1000)
        self.puffer = self.dummyPuff("Origin", origin)


    def dummyPuff(self, name, pos, max):
        puff = Puff()
        puff.setName(name)
        puff.setPosition(pos.get("x"), pos.get("y"), pos.get("z"))
        
        for i in (0, max):
            newOrigin = self.createOrigin(pos["x"] + i, pos["y"] + i, pos["z"] + i)
            puff.addEdge(i, dummyPuff(f"{name}#{i}"), newOrigin, max - i)

        return puff

    def build():
        constructedPuffer = self.puffer
        self.puffer = Puff()

        return constructedPuffer