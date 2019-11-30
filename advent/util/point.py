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

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.x == other.x and
            self.y == other.y
        )
    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ']'


# Point + Direction
class Vector(Point):
    __forward={
        Dir.UP: lambda v, dist :            Vector(v.x,         v.y + dist, Dir.UP),
        Cardinal.NORTH: lambda v, dist :    Vector(v.x,         v.y + dist, Cardinal.NORTH),
        Dir.RIGHT: lambda v, dist :         Vector(v.x + dist,  v.y,        Dir.RIGHT),
        Cardinal.EAST: lambda v, dist :     Vector(v.x + dist,  v.y,        Cardinal.EAST),
        Dir.DOWN: lambda v, dist :          Vector(v.x,         v.y - dist, Dir.DOWN),
        Cardinal.SOUTH: lambda v, dist :    Vector(v.x,         v.y - dist, Cardinal.SOUTH),
        Dir.LEFT: lambda v, dist :          Vector(v.x - dist,  v.y,        Dir.LEFT),
        Cardinal.WEST: lambda v, dist :     Vector(v.x - dist,  v.y,        Cardinal.WEST),
    }

    __reverse={
        Dir.UP: lambda v, dist :            Vector(v.x,         v.y - dist, Dir.DOWN),
        Cardinal.NORTH: lambda v, dist :    Vector(v.x,         v.y - dist, Cardinal.SOUTH),
        Dir.RIGHT: lambda v, dist :         Vector(v.x - dist,  v.y,        Dir.LEFT),
        Cardinal.EAST: lambda v, dist :     Vector(v.x - dist,  v.y,        Cardinal.WEST),
        Dir.DOWN: lambda v, dist :          Vector(v.x,         v.y + dist, Dir.UP),
        Cardinal.SOUTH: lambda v, dist :    Vector(v.x,         v.y + dist, Cardinal.NORTH),
        Dir.LEFT: lambda v, dist :          Vector(v.x + dist,  v.y,        Dir.RIGHT),
        Cardinal.WEST: lambda v, dist :     Vector(v.x + dist,  v.y,        Cardinal.EAST),
    }

    __left={
        Dir.UP: lambda v, dist :            Vector(v.x - dist,  v.y,        Dir.LEFT),
        Cardinal.NORTH: lambda v, dist :    Vector(v.x - dist,  v.y,        Cardinal.WEST),
        Dir.RIGHT: lambda v, dist :         Vector(v.x,         v.y + dist, Dir.UP),
        Cardinal.EAST: lambda v, dist :     Vector(v.x,         v.y + dist, Cardinal.NORTH),
        Dir.DOWN: lambda v, dist :          Vector(v.x + dist,  v.y,        Dir.RIGHT),
        Cardinal.SOUTH: lambda v, dist :    Vector(v.x + dist,  v.y,        Cardinal.EAST),
        Dir.LEFT: lambda v, dist :          Vector(v.x,         v.y - dist, Dir.DOWN),
        Cardinal.WEST: lambda v, dist :     Vector(v.x,         v.y - dist, Cardinal.SOUTH),
    }

    __right={
        Dir.UP: lambda v, dist :            Vector(v.x + dist,  v.y,        Dir.RIGHT),
        Cardinal.NORTH: lambda v, dist :    Vector(v.x + dist,  v.y,        Cardinal.EAST),
        Dir.RIGHT: lambda v, dist :         Vector(v.x,         v.y - dist, Dir.DOWN),
        Cardinal.EAST: lambda v, dist :     Vector(v.x,         v.y - dist, Cardinal.SOUTH),
        Dir.DOWN: lambda v, dist :          Vector(v.x - dist,  v.y,        Dir.LEFT),
        Cardinal.SOUTH: lambda v, dist :    Vector(v.x - dist,  v.y,        Cardinal.WEST),
        Dir.LEFT: lambda v, dist :          Vector(v.x,         v.y + dist, Dir.UP),
        Cardinal.WEST: lambda v, dist :     Vector(v.x,         v.y + dist, Cardinal.NORTH),
    }

    def __init__(self, x=0, y=0, dir=Dir.UP):
        Point.__init__(self, x, y)
        self.dir = dir

    def forward(self, dist):
        return Vector.__forward.get(self.dir)(self, dist)

    def reverse(self, dist):
        return Vector.__reverse.get(self.dir)(self, dist)

    def turnLeft(self, dist):
        return Vector.__left.get(self.dir)(self, dist)

    def turnRight(self, dist):
        return Vector.__right.get(self.dir)(self, dist)

    def to_point(self):
        return Point(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y, self.dir))

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__ and
            self.x == other.x and
            self.y == other.y and
            self.dir == other.dir
        )
    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return '[' + str(self.x) + ',' + str(self.y) + '] ' + self.dir.name
