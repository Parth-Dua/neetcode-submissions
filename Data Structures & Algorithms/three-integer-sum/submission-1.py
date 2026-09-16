class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # O(n^3) is brute force

        # O(n^2) is 2 sum with hashmap with O(n) space

        # Sort the array
        ans = []
        nums.sort()

        for i in range(len(nums)): 
            # Skip duplicate a's
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1 
            r = len(nums) - 1
            a = nums[i]
            target_sum = -1*a
            # sum should be equal to the negative of a

            while l < r: 
                s = nums[l] + nums[r]
                if s == target_sum: 
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    # Skip duplicate right values
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                elif s > target_sum: 
                    r-=1
                else: 
                    l+=1

        return ans

