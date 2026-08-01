class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        def block_places(x,y, blocked) :
            # Block the places if the queen is inserted at i,j
            for i in range(n): 
                for j in range(n) :

                    if i == x or j == y or abs(i-x) == abs(j-y): 
                        blocked[i][j] = True

                    # Block Diagonals
        
        def place_queen(x,y, curr): 
            # Place the queen in the string at x,y
            curr[x] = curr[x][:y] + "Q" + curr[x][y+1:] 
            
            

        def helper(row, curr, blocked) : 

            # Terminating case
            # one queen in each row
            if row == n: 
                res.append(curr)
                return
            
            # All positions where we can place the second queen
            for col in range(n): 

                    if not blocked[row][col]: 

                        curr_temp = curr.copy()
                        blocked_temp = [ blocked_row.copy()for blocked_row in blocked ]
                        # PLace the queen at yth position in x in curr
                        place_queen(row, col, curr_temp)
                    # Block the places which need to be blocked by the new queen
                        block_places(row, col, blocked_temp)

                        
                        helper(row+1, curr_temp,  blocked_temp)

            return 
        

        curr = ["." * n for _ in range(n)]
        blocked = [[False] * n for _ in range(n)]
        helper(0, curr, blocked)
        return res
