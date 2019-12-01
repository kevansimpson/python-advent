from collections import Counter
from operator import itemgetter
import re

def sum_sector_ids(rooms):
    return sum(list(map(lambda r : Room(r).get_sector_id(), rooms)))

def north_pole_room(rooms, target):
    for r in rooms:
        room = Room(r)
        name = shift_text(room.sector_id, room.encrypted_name)
        if (name == target): return room.sector_id

    return -1

strs = 'abcdefghijklmnopqrstuvwxyz'      #use a string like this, instead of ord() 
def shift_text(shift, text):
    data = []
    for i in text:                     #iterate over the text not some list
        if i.strip() and i in strs:                 # if the char is not a space ""  
            data.append(strs[(strs.index(i) + shift) % 26])    
        else:
            data.append(i)           #if space the simply append it to data
    output = ''.join(data)
    return output.replace('-', ' ')

class Room:
    def __init__(self, line):
        raw = re.match(r'([^\d]+)-(\d+)\[(\w+)\]', line)
        self.encrypted_name = raw.group(1)
        self.sector_id = int(raw.group(2))
        self.checksum = raw.group(3)

    def get_sector_id(self):
        return self.sector_id if self.is_real() else 0

    def is_real(self):
        count = Counter(self.encrypted_name.replace('-', ''))
        cksum = sorted(sorted(count.most_common(), key=itemgetter(0)), key=itemgetter(1), reverse=True)
        testCksum = ''.join(map(lambda pair : pair[0], cksum[0:5]))        
        return self.checksum == testCksum

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return 'Room(' + self.encrypted_name + '-(' + str(self.sector_id) + ')[' + self.checksum + '])'
