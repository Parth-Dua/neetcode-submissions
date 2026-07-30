class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0: 
            return []
        m = ["abc" , "def", "ghi", "jkl" , "mno" , "pqrs" , "tuv" , "wxyz"] 



        def get_char_string(digit): 
            return m[int(digit) - 2]


        def helper(i): 
            if i == len(digits): 
                return [""]
            
            rec_comb = helper(i+1)
            new = []

            for s in get_char_string(digits[i]): 
                for comb in rec_comb: 
                    
                    new.append(s+comb)
                
            return new
        
        return helper(0)

