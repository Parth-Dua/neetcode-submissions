from collections import defaultdict

class Solution:
    hashmap = defaultdict(lambda: None)
    hashmap[0] = 0
    hashmap[1] = 1
    hashmap[2] = 2

    def climbStairs(self, n: int) -> int:
        
        if n ==1: return 1
        if n==2: return 2

        last = self.hashmap[n-1] if self.hashmap[n-1] != None else self.climbStairs(n-1)
        second_last = self.hashmap[n-2] if self.hashmap[n-2] != None else self.climbStairs(n-2)

        self.hashmap[n] = last + second_last
        return self.hashmap[n]
