from advent.util.input import read_lines
from advent._2016.day04 import Room, north_pole_room, shift_text, sum_sector_ids

def test_examples():
    # real room because the most common letters are a (5), b (3),
    # and then a tie between x, y, and z, which are listed alphabetically.
    room1 = 'aaaaa-bbb-z-y-x-123[abxyz]'
    assert Room(room1).is_real() == True
    # real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
    room2 = 'a-b-c-d-e-f-g-h-987[abcde]'
    assert Room(room2).is_real() == True
    # is a real room.
    room3 = 'not-a-real-room-404[oarel]'
    assert Room(room3).is_real() == True
    # is not
    room4 = 'totally-real-room-200[decoy]'
    assert Room(room4).is_real() == False

    assert sum_sector_ids([room1, room2, room3, room4]) == 1514

    # qzmt-zixmtkozy-ivhz-343 is very encrypted name.
    assert shift_text(343, 'qzmt-zixmtkozy-ivhz') == 'very encrypted name'

def test_answers():
    input = read_lines('_2016', 'input04.txt')
    assert sum_sector_ids(input) == 137896
    assert north_pole_room(input, 'northpole object storage') == 501
