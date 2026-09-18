class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def helper(i, res ): 

            # BASE CASE: TERMINAL CASE
            if i == len(nums) : 
                ans.append(res.copy())
                return 

            # 2 choices: incl and not incl

            # Include 
            res.append(nums[i])
            helper(i+1, res)
            res.pop()

            # Not Include
            helper(i+1, res)

        helper(0, [])

        return ans


