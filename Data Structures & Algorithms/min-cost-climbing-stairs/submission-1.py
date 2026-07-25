from collections import defaultdict

class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        target_lvl = len(cost)
        m = defaultdict(lambda: None)
        return self.helper(cost, target_lvl, m)

    def  helper(self, cost, target_lvl, m): 
        # minimum cost to reach the target_lvl 
        if target_lvl == 0 : return 0
        if target_lvl == 1: return 0
        
        one_below_incl = cost[target_lvl-1]+m[target_lvl-1] if m[target_lvl-1] != None else cost[target_lvl-1] + self.helper(cost, target_lvl-1, m) 
        two_below_incl = cost[target_lvl-2] + m[target_lvl-2] if m[target_lvl-2] != None else cost[target_lvl-2] + self.helper(cost, target_lvl-2, m)

        m[target_lvl] = min(one_below_incl, two_below_incl)
        return m[target_lvl] 