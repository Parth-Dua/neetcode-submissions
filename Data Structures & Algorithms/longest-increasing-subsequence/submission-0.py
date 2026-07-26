class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Bottom up with Time O(n^2)

        dp = [1] * len(nums)

        for i in range(len(nums)): 

            index_largest_element_smaller_than_i = -1
            j = i-1
            # calculate that
            while j>=0: 
                if nums[j] < nums[i]:

                    if (
                        index_largest_element_smaller_than_i == -1
                        or dp[j] > dp[index_largest_element_smaller_than_i]
                    ):
                        index_largest_element_smaller_than_i = j
                j-=1

            dp[i] = 1 if index_largest_element_smaller_than_i == -1 else dp[index_largest_element_smaller_than_i]+1

        return max(dp)
