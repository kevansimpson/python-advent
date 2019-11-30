from advent.util.input import read_lines
from advent._2016.day02 import DIAMOND_GRID, SQUARE_GRID, bathroom_code

def test_examples():
    input = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']
    assert bathroom_code(input, SQUARE_GRID) == '1985'
    assert bathroom_code(input, DIAMOND_GRID) == '5DB3'

def test_answers():
    input = read_lines('_2016', 'input02.txt')
    assert bathroom_code(input, SQUARE_GRID) == '76792'
    assert bathroom_code(input, DIAMOND_GRID) == 'A7AC3'
