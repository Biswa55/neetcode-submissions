"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res=[]
        for i in range(len(intervals)):
            v=[intervals[i].start,0]
            res.append(v)
            g=[intervals[i].end,1]
            res.append(g)
        res.sort(key=lambda x:(x[0],-x[1]))
        resu=0
        room=0
        for i in range(len(res)):
            if res[i][1]==0:
                room+=1
                resu=max(resu,room)
            elif res[i][1]==1:
                room-=1
        return resu               
