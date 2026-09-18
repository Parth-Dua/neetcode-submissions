class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()

        ans = set()

        curr = []
        
        def helper(i, target): 

            # Terminating case: useful  
            if target == 0: 
                ans.add(tuple(curr))
                return 

            # Terminating case:  useless
            if i == len(nums) or target< 0: 
                return

            # Incl i only if not in the curr
            curr.append(nums[i])
            helper(i+1, target - nums[i])
            curr.pop()
            

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            # Not include i 
            helper(i+1, target)

        helper(0,target)

        return [list(x) for x in ans]
