from advent.util.point import Vector

def follow_directions(steps):
    loc=Vector()
    for step in steps:
        dist = int(step[1:])
        if step.startswith('L'): loc = loc.turnLeft(dist)
        else: loc = loc.turnRight(dist)

    return abs(loc.x) + abs(loc.y)
