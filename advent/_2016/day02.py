from advent.util.point import Dir, Point

__DIR_MAP__ = {
    'U': lambda pt : pt.move(0, 1),
    'R': lambda pt : pt.move(1, 0),
    'D': lambda pt : pt.move(0, -1),
    'L': lambda pt : pt.move(-1, 0)
}

SQUARE_GRID = {
    Point(-1, 1):  '1',
    Point(0, 1):   '2',
    Point(1, 1):   '3',
    Point(-1, 0):  '4',
    Point(0, 0):   '5',
    Point(1, 0):   '6',
    Point(-1, -1): '7',
    Point(0, -1):  '8',
    Point(1, -1):  '9'
}

#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D
DIAMOND_GRID = {
    Point(0, 2):   '1',
    Point(-1, 1):  '2',
    Point(0, 1):   '3',
    Point(1, 1):   '4',
    Point(-2, 0):  '5',
    Point(-1, 0):  '6',
    Point(0, 0):   '7',
    Point(1, 0):   '8',
    Point(2, 0):   '9',
    Point(-1, -1): 'A',
    Point(0, -1):  'B',
    Point(1, -1):  'C',
    Point(0, -2):  'D'
}


def bathroom_code(steps, keypad):
    loc = list(keypad.keys())[list(keypad.values()).index('5')]
    code = []
    for step in steps:
        for ch in step.rstrip():
            next = __DIR_MAP__.get(ch)(loc)
            if (keypad.get(next) is not None): loc = next
        # end step
        code.append(keypad.get(loc))

    return ''.join(code)
