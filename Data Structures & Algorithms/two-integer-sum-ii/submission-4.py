class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        l, r = 0, len(nums) - 1

        while l<r: 
            s = nums[l] + nums[r]
            if s == target :
                return [l+1,r+1]
            
            elif s < target :
                # Expand
                l+=1
            
            else: 
                # Shrink
                r-=1

        return []