class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0: 
            return []
        m = ["abc" , "def", "ghi", "jkl" , "mno" , "pqrs" , "tuv" , "wxyz"] 



        def get_char_string(digit): 
            return m[int(digit) - 2]

        ans = []
        curr = []

        def helper(i): 
            
            # Terminating case 
            if i >= len(digits): 
                ans.append("".join(curr))
                return 

            
            # Recursion 
            for char in get_char_string(digits[i]): 

                curr.append(char)
                helper(i+1)
                curr.pop()

        helper(0)
        return ans 

