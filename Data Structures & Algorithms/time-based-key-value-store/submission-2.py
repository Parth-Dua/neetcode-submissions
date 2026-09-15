class TimeMap:

    def __init__(self):
        self.d = dict() 
        # key : [[values], [timestamps]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d: 
            self.d[key] = [[value] ,[timestamp]]
        else: 
            self.d[key][0].append(value)
            self.d[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        
        # Return the value with the largest timestamp < current timestamp 


        # Brute Force : timestamp, timestamp - 1, timestamp -2 , ... 

        # Binary Search: between 0 and timestamp
        if key not in self.d :
            return ""
        timestamps = self.d[key][1]
        index = self.largest_smaller_than_t(timestamps, timestamp)
        if index == -1 : 
            return ""

        return self.d[key][0][index]

            

    def largest_smaller_than_t(self, array, t): 

        l, r = 0, len(array)-1
        ans = -1 
        while l<=r: 
            mid = (l+r) //2 
            if array[mid] <= t: 
                # Candidate
                ans = mid 
                # Search for larger that is right
                l = mid + 1
            else: 
                # Look for smaller 
                r = mid - 1 

        
        return ans

            
            
