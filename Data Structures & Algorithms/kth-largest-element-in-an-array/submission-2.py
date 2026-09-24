class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n= len(nums)

        for _ in range(n-k): 
            heapq.heappop(nums)
        
        return nums[0]