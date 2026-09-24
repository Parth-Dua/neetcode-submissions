class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
 
        heap = []

        for freq, char in [(a, "a"), (b, "b"), (c, "c")]:
            if freq > 0:
                heap.append((freq, char))

        heapq.heapify_max(heap)
        ans = []

        while heap: 

            max_freq, char = heapq.heappop_max(heap)

            # In valid check for 'aaa'
            if len(ans) >=2 and  (ans[-1] == ans[-2] == char): 

                # can't use this one
                if not heap: 
                    break

                freq_sec, char_sec = heapq.heappop_max(heap)
                ans.append(char_sec)
                if freq_sec > 1:
                    heapq.heappush_max(heap, (freq_sec-1, char_sec))

                heapq.heappush_max(heap, (max_freq, char))

            else:                
                ans.append(char)
                if max_freq > 1:
                    heapq.heappush_max(heap, (max_freq-1, char))

        return "".join(ans)



