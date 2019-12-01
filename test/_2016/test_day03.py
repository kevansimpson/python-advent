from advent.util.input import read_lines
from advent._2016.day03 import count_triangles, parse_columns, vertical_triangles

def test_examples():
    input = parse_columns(['25 5 10', '15 15 25', '18 20 35'])
    assert count_triangles(input) == 2
    assert vertical_triangles(input) == 1

def test_answers():
    input = parse_columns(read_lines('_2016', 'input03.txt'))
    assert count_triangles(input) == 982
    assert vertical_triangles(input) == 1826
