from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    
        @cache
        def helper(i ) :

            if i >= len(s):
                # Empty string
                return True
            
            for w in wordDict: 

                if (i + len(w)) <= len(s) and s[i: i+len(w)] == w: 
                    if helper(i+ len(w)): # The remaining string gives us True
                        return True
                
            return False
        
        return helper(0)
