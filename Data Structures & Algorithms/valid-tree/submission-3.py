class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # Tree is connected, undirected graph with no cycles

        # CHeck connected and no cycles 

        graph = [[] for _ in range(n)]

        for u,v in edges: 
            graph[u].append(v) 
            graph[v].append(u) 

        state = [0]*n
        def dfs(node, parent ): 


            if  state[node] == 2: 
                return True 

            if state[node] == 1: 
                return False 

            # Now we are visiting an undiscovered node 
            state[node] = 1 
            
            res = True
            for neighbor in graph[node]: 
                if neighbor!=parent: 
                    res = res and dfs(neighbor, node)

            # Completed
            state[node] = 2 

            return res 


        
        if not dfs(0, -1) :
            return False 

        for i in range(n): 
            if state[i]!=2:
                return False 

        return True 
