class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])
        
        def do_overlap(intvl1, intvl2): 
            return max(intvl1[0], intvl2[0]) <= min(intvl1[1], intvl2[1])
        
        res = [intervals[0]]
        for s,e in intervals[1:]: 
            if do_overlap([s,e], res[-1]) :
                res[-1] = [min(s, res[-1][0]),max(e, res[-1][1]) ]

            else: 
                res.append([s,e])

        return res
        