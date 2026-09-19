class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
         
        # if k << n 

        # min heap - stores the k largest elements and the root = kth largest element 

        n = len(nums)

        heap = [nums[0]]

        for i in range(1, n): 
            
            # Add to the min heap only if it is greater than the current minimum 
            heapq.heappush(heap, nums[i])   

            if len(heap) > k: 
                # We need only largest k elements in the heap 
                heapq.heappop(heap)

        return heap[0]
        

