class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(i,j,pos): 
            
            # Terminating case
            if pos == len(word): 
                return True

            # Not found situation 
            if i >= len(board) or j >= len(board[0]) or i<0 or j<0: 
                return False
            
            # Character matched: 
            if board[i][j] == word[pos]: 

                temp = board[i][j]
                board[i][j] = '#'

                # Up   
                up = helper(i-1, j ,pos+1)
                # down
                down = helper(i+1, j ,pos+1)
                # left 
                left = helper(i, j-1 ,pos+1)
                # right
                right = helper(i, j+1 ,pos+1)


                board[i][j] = temp

                return up or down or left or right

            return False
        

        for x in range(len(board)): 
            for y in range(len(board[0])): 
                # x,y is starting position
                if helper(x,y,0) == True: 
                    return True
        
        return False
            