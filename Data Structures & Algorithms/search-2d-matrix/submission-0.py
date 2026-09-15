class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        columns = len(matrix[0])
         

        n, m = rows, columns

        # Find the row first 
        l, r = 0, n-1

        
        while l<=r: 
            mid = l + (r-l) // 2 

            if target in range(matrix[mid][0], matrix[mid][-1]+1): 
                # Binary search on the matrix[mid]
                s,e = 0,m-1

                while s<=e: 
                    c = (s+e) // 2 

                    if matrix[mid][c] == target: 
                        return True
                    elif target < matrix[mid][c] : 
                        e = c - 1
                    else: 
                        s = c+1
                    
                return False
            
            elif target < matrix[mid][0]: 
                # Go left
                r = mid - 1 

            else: 
                #Go right
                l = mid + 1

    
        return False
