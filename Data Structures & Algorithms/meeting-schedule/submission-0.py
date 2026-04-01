"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        
        intervals = sorted(intervals, key=lambda interval: interval.start)
        for i in intervals:
            print(f"({i.start}, {i.end})")
        
        for i in range(1, len(intervals)):
            i2 = intervals[i]
            i1 = intervals[i - 1]

            if i1.end > i2.start:
                return False

        return True