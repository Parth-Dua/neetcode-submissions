class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = "("

        def helper(n, s, countOpen): 

            if n == 0: 
                s+= ')' * countOpen
                res.append(s)
                return
            
            # Open

            helper(n-1, s + "(", countOpen+1)

            # Close
            if countOpen>0: 
                helper(n, s+ ")", countOpen-1)

        helper(n-1, "(", 1)
        return res
