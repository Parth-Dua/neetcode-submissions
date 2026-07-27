class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l , r = 0, len(heights) -1 
        m = 0

        while l<r and l<len(heights) and r<len(heights): 
            area = (r-l) * min(heights[l], heights[r])

            if area>m: m=area

            if heights[l] > heights[r]: 
                r-=1
            else: 
                l+=1
            
        return m
