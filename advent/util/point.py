from enum import Enum

class Dir(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"

class Cardinal(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"

# Cartesian x,y
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ']'


# Point + Direction
class Vector(Point):
    left={
        Dir.UP: lambda v, dist :
            Vector(v.x - dist, v.y, Dir.LEFT),
        Cardinal.NORTH: lambda v, dist :
            Vector(v.x - dist, v.y, Cardinal.WEST),
        Dir.RIGHT: lambda v, dist :
            Vector(v.x, v.y - dist, Dir.UP),
        Cardinal.EAST: lambda v, dist :
            Vector(v.x, v.y - dist, Cardinal.NORTH),
        Dir.DOWN: lambda v, dist :
            Vector(v.x + dist, v.y, Dir.RIGHT),
        Cardinal.SOUTH: lambda v, dist :
            Vector(v.x + dist, v.y, Cardinal.EAST),
        Dir.LEFT: lambda v, dist :
            Vector(v.x, v.y + dist, Dir.DOWN),
        Cardinal.WEST: lambda v, dist :
            Vector(v.x, v.y + dist, Cardinal.SOUTH),
    }

    right={
        Dir.UP: lambda v, dist :
            Vector(v.x + dist, v.y, Dir.RIGHT),
        Cardinal.NORTH: lambda v, dist :
            Vector(v.x + dist, v.y, Cardinal.EAST),
        Dir.RIGHT: lambda v, dist :
            Vector(v.x, v.y + dist, Dir.DOWN),
        Cardinal.EAST: lambda v, dist :
            Vector(v.x, v.y + dist, Cardinal.SOUTH),
        Dir.DOWN: lambda v, dist :
            Vector(v.x - dist, v.y, Dir.LEFT),
        Cardinal.SOUTH: lambda v, dist :
            Vector(v.x - dist, v.y, Cardinal.WEST),
        Dir.LEFT: lambda v, dist :
            Vector(v.x, v.y - dist, Dir.UP),
        Cardinal.WEST: lambda v, dist :
            Vector(v.x, v.y - dist, Cardinal.NORTH),
    }

    def __init__(self, x=0, y=0, dir=Dir.UP):
        Point.__init__(self, x, y)
        self.dir = dir

    def turnLeft(self, dist):
        return Vector.left.get(self.dir)(self, dist)

    def turnRight(self, dist):
        return Vector.right.get(self.dir)(self, dist)

    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + '] ' + self.dir.name
