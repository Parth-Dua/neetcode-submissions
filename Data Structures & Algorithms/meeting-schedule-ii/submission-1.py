"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: 
            return 0
        
        time = []

        for i in intervals: 
            time.append((i.start, 1)) # 1 room required
            time.append((i.end, -1)) # 1 room becomes free 

        time.sort(key = lambda x: (x[0], x[1]))
        
        res = curr_occupied = 0
        for t, room_req in time:
            curr_occupied += room_req 
            res = max(res, curr_occupied)
        return res



