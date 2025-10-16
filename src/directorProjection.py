
class Pose:
    def __init_(self):
        self.label = ""
        self.direction = ""
        self.meaningCode = 0

    def setMeaning(self, c):
        self.meaningCode = c

    def setDirection(self, d):
        self.direction = d

    def setLabel(self, label):
        self.label = label

    def isDirection(self, d):
        if self.getDirection() == d:
            return True
        
        return False

    def getDirection(self):
        return self.direction
    def getMeaning(self):
        return self.meaningCode
    def getLabel(self):
        return self.label

class PoseBuilderLeft:
    def __init__(self):
        self.pose = Pose()
    
    def pointLeft(self):
        self.pose.setMeaning(0)
        self.pose.direction("hard_left")
        self.setLabel("point_left")

        newPose = self.pose
        self.pose = Pose()

        return newPose
    
    def graspLeft(self):
        self.pose.setMeaning(0)
        self.pose.direction("upper_left")
        self.pose.label("grasp_left")


class Hands:
    def __init__(self):
        self.poses = []
        self.projectionCode = []