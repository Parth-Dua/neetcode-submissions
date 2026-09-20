class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Cycle detetion
        # If cycle -> cannot work, else can work 
        graph = [[] for _ in range(numCourses)]


        for course, prereq in prerequisites: 
            graph[prereq].append(course)

        state = [0] * numCourses
        # 0 is unvisited, 1 is currently visiting, 2 is visited 

        def dfs(node): 

            if state[node] == 1:
                return False 

            if state[node] ==2 : 
                return True   

            # Mark as currently visiting 
            state[node] = 1
            
            for neighbor in graph[node]: 

                res = dfs(neighbor)
                # Even if one neighbor returns False -> Cycle is there 
                if not res: 
                    return False 

            state[node] = 2 # Visited 
            return True 

         
        for course in range(numCourses): 
            if not dfs(course): 
                return False
        return True 





        



