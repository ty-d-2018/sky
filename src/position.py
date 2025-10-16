
class Volume:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def match(self, xx, yy, zz):
        if self.x == xx and self.y == yy and self.z == zz:
            return True
        else:
            return False

    def getData(self):
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
        }