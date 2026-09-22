class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Not connected, directed 

        # Return true if there is a cycle 

        # DFS -> when we visit a node which we are "visiting" then True

        # Adjacency list
        graph = [[] for _ in range(numCourses)]
        
        for course, prereq in prerequisites: 
            graph[prereq].append(course )

        state = [0]*numCourses
        # 0 = undiscovered, 1 = visiting/ discovered, 2 = visited/ finished all neighbors

        res = [ ]

        def dfs(node): 
            
            if state[node] == 2: 
                return True 
            
            if state[node] == 1:
                return False 
        
            ans = True 
            state[node] = 1 

            

            for neighbor in graph[node]: 
                ans = ans and dfs(neighbor)

            res.append(node)
            state[node] = 2

            return ans 
        
        for i in range(numCourses): 

            if not dfs(i): 
                return []

        return res[::-1] 

        
        