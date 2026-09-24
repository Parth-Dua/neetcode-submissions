class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq = {}

        for i in s:
            if i in freq:
                freq[i]+=1
            else: 
                freq[i] = 1 
            
        print(freq)

        # [(freq, char), (freq, char)]
        heap = []
        for char, freq in freq.items(): 
            heap.append((freq,char))

        final_s = []

        heapq.heapify_max(heap)

        # Most frequent is at the root 

        while heap: 
            freq, char = heapq.heappop_max(heap)

            if final_s and char == final_s[-1]: 
                if not heap: 
                    return ""
                # Choose the next one
                freq_sec, char_sec = heapq.heappop_max(heap)
                final_s.append(char_sec)

                # Add back to the heap
                if freq_sec > 1: 
                    heapq.heappush_max(heap, (freq_sec-1, char_sec))

                heapq.heappush_max(heap, (freq, char))

            else: 
                #Choose this one
                final_s.append(char)
                if freq > 1: 
                    heapq.heappush_max(heap, (freq-1, char))

        return "".join(final_s)
