class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq._heapify_max(stones)

        while len(stones) >1: 

            largest = heapq.heappop_max(stones)
            second_largest = heapq.heappop_max(stones)

            if largest > second_largest: 
                heapq.heappush_max(stones, largest-second_largest)

        return stones[0] if len(stones)>0 else 0

