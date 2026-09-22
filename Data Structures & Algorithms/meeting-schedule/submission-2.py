"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        if not intervals: 
            return True

        intervals.sort(key = lambda i: i.start)

        def do_overlap(interval1, interval2): 

            return max(interval1.start, interval2.start) < min(interval1.end, interval2.end)

        prev = intervals[0]
        for curr in intervals[1:]: 
            if do_overlap(prev, curr): 
                return False
            prev = curr

        return True 