class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = set()

        def dfs(i,j, word):

            # Found case 
            if len(word) == 0  :
                return True 

            # Useless case and visited case
            if i<0 or i>=n or j< 0 or j >=m or (i,j) in visited: 
                return False 
            # Current character must match
            if board[i][j] != word[0]:
                return False

            # Now over all the neighbors
            neighbors = [(i-1,j), (i+1,j),(i,j-1),(i,j+1)]
            
            visited.add((i,j))
            ans = False 
            for x,y in neighbors: 
                
                ans = ans or dfs(x,y, word[1:])
            
            visited.remove((i,j))

            return ans

        
        for i in range(n): 
            for j in range(m): 
                
                if dfs(i,j, word) :               
                    return True
                
        return False