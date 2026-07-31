class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def help(n,k,ans): 
            
            # Terminating case
            if k == 0: 
                res.append(ans)
                return
            
            # Recurse back, not include subset case
            if n <= 0 :
                return

            # incl i
            help(n-1, k-1 ,ans + [n])

            # not incl i
            help(n-1, k, ans)

            return 
        
        help(n,k, [])
        return res



             