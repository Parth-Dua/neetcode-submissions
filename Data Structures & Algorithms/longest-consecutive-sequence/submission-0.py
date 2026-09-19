from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        longest = 0

        for i in nums: 

            if i-1 not in s: 
                
                # This is  the  start 
                length = 0
                while (i+length) in s: 
                    length += 1
                longest = max(longest, length)

        return longest 