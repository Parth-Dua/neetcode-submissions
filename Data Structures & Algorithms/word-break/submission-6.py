from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_set = set(wordDict)
        
        @cache
        def helper(i): 
            
            # Termination Case
            if i == len(s): 
                return True 

            # Base Case
            if i >len(s): 
                return False 

            ans = False 

            for word in wordDict: 
                word_len = len(word)

                if s[i:i+word_len] == word: 
                    # That is good we found one thing
                    ans = ans or helper(i+word_len)

            return ans 

        return helper(0)

