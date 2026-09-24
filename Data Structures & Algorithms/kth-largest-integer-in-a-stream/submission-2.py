class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k 
        heapq.heapify(self.heap)

        # Keep only the k largest elements here -

        while (len(self.heap) > k): 
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:

        # O(log n) to insert
        heapq.heappush(self.heap, val)

        # now there are k+1 values

        # Now we pop one value - again k values
        if len(self.heap) > self.k: 
            heapq.heappop(self.heap)

        return self.heap[0]

        