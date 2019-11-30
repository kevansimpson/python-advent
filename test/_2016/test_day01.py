from advent.util.input import split_string
from advent._2016.day01 import follow_directions, visited_twice

def test_examples():
    # Following R2, L3 leaves you 2 blocks East and
    # 3 blocks North, or 5 blocks away.
    assert follow_directions(['R2', 'L3']) == 5
    # R2, R2, R2 leaves you 2 blocks due South of your starting
    # position, which is 2 blocks away.
    assert follow_directions(['R2', 'R2', 'R2']) == 2
    # R5, L5, R5, R3 leaves you 12 blocks away
    assert follow_directions(['R5', 'L5', 'R5', 'R3']) == 12

    # if your instructions are R8, R4, R4, R8,
    # the first location you visit twice is 4 blocks away
    assert visited_twice(['R8', 'R4', 'R4', 'R8']) == 4

def test_answers():
    input = split_string('_2016', 'input01.txt', ',\\s*')
    assert follow_directions(input) == 288
    assert visited_twice(input) == 111
