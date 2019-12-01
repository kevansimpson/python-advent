import re

def count_triangles(cols):
    return len(list(filter(lambda tri : is_triangle(tri[0], tri[1], tri[2]), cols)))

def vertical_triangles(cols):
    count = 0
    for x in range(0, len(cols), 3):
        for c in range(3):
            if is_triangle(cols[x][c], cols[x + 1][c], cols[x + 2][c]): count += 1

    return count

def is_triangle(a, b, c):
    abc = list([a, b, c])
    abc.sort()
    return (abc[0] + abc[1] > abc[2]) and (abc[0] + abc[2] > abc[1]) and (abc[1] + abc[2] > abc[0])

def parse_columns(lines):
    return list(map(lambda line : list(map(int, re.findall(r'\d+', line))), lines))
