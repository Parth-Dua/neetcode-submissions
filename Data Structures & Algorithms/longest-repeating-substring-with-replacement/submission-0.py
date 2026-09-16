from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0,0 
        n = len(s)

        ans = 0
        hashmap = defaultdict(int)
        while r<n :
            
            # FIrst add to the window 
            hashmap[s[r]] += 1

            # Condition not met
            while (r-l+1) - max(hashmap.values()) > k: 

                #Shrink
                hashmap[s[l]] -= 1
                l+=1
            
            # Condition met
            ans = max(ans, r-l+1)
            r+=1
        
        return ans
