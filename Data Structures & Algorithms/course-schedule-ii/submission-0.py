class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # TOPO Sort -> DFS and then decreasing finish times
         

        graph = [ [] for i in range(numCourses)]

        for course, prereq in prerequisites :
            graph[prereq].append(course )


        state = [0] * numCourses

        # 0 is unvisited, 1 is visiting, 2 is visited
        ans = []

        def dfs(node): 
            if state[node] == 1: 
                return False 

            if state[node] == 2: 
                return True 

            # Mark as visiting
            state[node] = 1

            for neighbor in graph[node]: 

                if not dfs(neighbor): 
                    return False 

            # Mark as visited
            ans.append(node)
            state[node] = 2 

            return True 

        for course in range(numCourses): 
            if not dfs(course): 
                return []

        return ans[::-1]
             
