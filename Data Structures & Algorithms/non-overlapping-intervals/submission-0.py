class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def do_overlap(intvl1, intvl2): 
            s1, e1 = intvl1[0], intvl1[1]
            s2, e2 = intvl2[0], intvl2[1]
            rightmost_start = max(s1,s2)
            leftmost_end = min(e1,e2)

            if rightmost_start < leftmost_end :
                return True 

            return False 
            
        intervals.sort()

        res = [intervals[0]]

        for start, end in intervals[1:]: 

            if do_overlap([start,end], res[-1]): 

                # Choose the one with earlier end - greedy
                if end < res[-1][1]: 
                    res[-1] = [start,end] 

            else: 
                res.append([start, end])        

        print(res)
        return len(intervals) - len(res) 
                