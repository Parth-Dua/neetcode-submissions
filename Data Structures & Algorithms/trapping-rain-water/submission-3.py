class Solution:
    def trap(self, height: List[int]) -> int:
        

        n = len(height)
        l = 0

        # # l is the first non zero value
        # while height[l] == 0: 
        #     l+=1

        r = l+1

        total_area = 0
        curr_sum = 0

        while l < n and r < n:  
            
            if height[r] >= height[l]: 

                # Found trapped water
                total_area+=curr_sum
                #print("Found trapped: ", curr_sum)
                l = r
                r = l+1
                curr_sum = 0
            
            else: 
                
                # Inside the trapped area
                curr_sum = curr_sum + height[l] - height[r]

                r+=1

        
        right = n - 1
        i = right - 1
        curr_sum = 0

        while i >= l:

            if height[i] >= height[right]:

                total_area += curr_sum

                right = i
                curr_sum = 0

            else:
                curr_sum += height[right] - height[i]

            i -= 1
        
        return total_area
            

