class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort based on start 
        intervals.sort(key = lambda i: i[0])
        
        res = [intervals[0]]

        for start, end in intervals[1:]: 
            # No Overlap: start of new > finish of last 
            if start > res[-1][1]: 
                res.append([start,end])
            # Full overlap
            elif end <= res[-1][1] :
                continue 
            # Partial overlap 
            else: 
                res[-1][1] = end 
            
        return res 
