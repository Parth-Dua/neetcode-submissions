class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        h = defaultdict(int)
        for i in nums: 
            h[i] +=1 
            if h[i] > len(nums)//2: 
                return i

        return -1