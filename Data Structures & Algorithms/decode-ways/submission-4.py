from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        
        @cache
        def helper(s) :
            
            if len(s) == 0: 
                return 1 

            # Atleast one element
            if s[0] == '0': 
                return 0

            # Exactly one element that is not 0
            if len(s) == 1 : 
                return 1

            # len(s) >=2 and The first character is valid

            ans = helper(s[1:]) # Current decoding
            
            # Second character is valid 
            if (s[0] == '1' ) or (s[0] == '2' and s[1] not in ['7','8','9'] ): 
                ans+= helper(s[2:])

            return ans 
    
        return helper(s)
                
                
            