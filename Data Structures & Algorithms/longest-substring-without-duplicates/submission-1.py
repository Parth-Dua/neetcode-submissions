class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        n = len(s)
        ans = 0
        l, r = 0,0

        current_window = set()
        while r<n:  
            
            while s[r] in current_window: 
                # Shrink
                current_window.discard(s[l])
                l+=1

            current_window.add(s[r])
            ans = max(ans, r - l + 1)
            r+=1
         

        return ans












        # length = len(s)
        # longest_subs_length = 0 

        # # Sliding Window

        # if length <= 1: return length

        # l, r = 0, 1
        # hashset = set()
        # hashset.add(s[l])

        # ans = 0

        # while r<length: 
            
        #     # Shrink until conditon is met
        #     while s[r] in hashset: 
        #         hashset.discard(s[l])
        #         l+=1
            
        #     # right element aint repeated
        #     # Keep on extending
        #     hashset.add(s[r])
        #     ans = max(ans, r-l+1)
        #     r+=1


        # return ans
