class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)

        maxheap = list(count.values()) # max heap of the frequency of each element
         
        heapq.heapify_max(maxheap)

        time = 0 

        q = deque() # [count, time_avaiable]  this is the cooldown queue
    
        # Logic: Take the most freq element from the heap then put it inside the q if more frequences are remaining. If the element in the queue has reached the time, then it is ready to be added to the heap back. # If the heap is also empty and the no elements to be processed in the queue, this means definite idle time, so time just increases. 

        while maxheap or q: 
            time+=1 

            if maxheap: 
                x = heapq.heappop_max(maxheap) # x is the current count

                if x -1 >= 1: 
                    # Add to queue
                    q.append([x-1, time + n ]) # time is the time when it will become available again

            if q and q[0][1] == time:  # that element is free again
                x, time1 =  q.popleft()
                heapq.heappush_max(maxheap, x)

        return time 
               







