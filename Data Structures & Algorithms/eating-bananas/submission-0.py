import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        min_eating_speed = max(piles)

        l, r = 1, min_eating_speed - 1
        

        # What smaller than min eating speed gives the valid solution -> gotta be in the range l to r -> find with binary search

        while l<=r:
            
            mid = l + (r-l) //2 

            # Check if works 
            total_hours = 0
            for i in piles: 
                total_hours += math.ceil(i/mid)

            if total_hours <= h: 
                # Case: Works
                min_eating_speed = mid

                # Now search for even lower
                # GO LEFT

                r = mid - 1 

            else: 
                # Case: Not works 
                # Look for something higher
                # GO RIGHT

                l = mid + 1

        return min_eating_speed


