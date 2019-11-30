from advent.util.point import Vector

def follow_directions(steps):
    loc = Vector()
    for step in steps:
        dist = int(step[1:])
        if step.startswith('L'): loc = loc.turnLeft(dist)
        else: loc = loc.turnRight(dist)

    return abs(loc.x) + abs(loc.y)

def visited_twice(steps):
    visited = set()
    loc = Vector()
    for step in steps:
        dist = int(step[1:])
        if step.startswith('L'): loc = loc.turnLeft(0)
        else: loc = loc.turnRight(0)
    
        visited.add(loc.to_point())
        for _d in range(dist):
            loc = loc.forward(1)
            pt = loc.to_point()
            if pt in visited: return abs(pt.x) + abs(pt.y)
            else: visited.add(pt)

    return -1
