from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        path = set()
        
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        def helper(i,j): 

            if dp[i][j] != 0:
                return dp[i][j]

            # Do stuff
            longest = 1

            for (x,y) in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
                if (x,y) in path: 
                    continue
                
                if x<len(matrix) and y<len(matrix[0]) and x>=0 and y>=0: 
                    if matrix[x][y] > matrix[i][j]:
                        path.add((x,y)) 
                        neighbour_length = helper(x,y) # Rec call
                        path.remove((x, y))
                        longest = max(longest, neighbour_length+1 )

            dp[i][j] = longest
            return longest

        answer = 1
        for i in range(len(matrix)): 
            for j in range(len(matrix[0])): 
                path.add((i,j))
                answer = max(answer, helper(i, j))
                path.remove((i,j))

        return answer



                



                        
                

