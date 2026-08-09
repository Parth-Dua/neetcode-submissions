class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = ""
        max_str = max(strs)
        print(max_str)
        for i in range(len(max_str)): 
            char = max_str[i]
            common = True
            for s in strs: 
                if len(s) <= i or s[i] != char :
                    common = False
                    
            if common == False: 
                break
                
            if common == True: 
                ans+=char
        return ans