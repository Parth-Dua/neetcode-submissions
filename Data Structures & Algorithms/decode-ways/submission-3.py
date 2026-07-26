from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def rec(i): 
            # BC1: Empty String
            if i>=len(s): 
                return 1
            
            # BC2: Only one element
            if i == len(s) -1 : 
                return 1 if s[i] != '0' else 0

            ways = 0
            # Only first char
            if s[i] != '0': 
                ways += rec(i+1)

            # first two characters
            if s[i]!= '0' and int(s[i: i+2]) in range(1,27)   : 
                ways+= rec(i+2)
            
            return ways 

        return rec(0)