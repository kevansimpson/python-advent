import os
import re

def read_lines(year, filename):
    with open(test_file(year, filename),'r') as f:
        return f.readlines()

def read_string(year, filename):
    with open(test_file(year, filename),'r') as f:
        return f.read()

def split_string(year, filename, regex):
    with open(test_file(year, filename),'r') as f:
        return re.split(regex, f.read())

def test_file(year, filename):
    return os.path.join(os.getcwd(), 'test', year, filename)