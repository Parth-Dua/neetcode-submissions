class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Question: Can the graph be disconnected? If it is then a collection of disconnected trees should return true? 
        

        # Convert edge list to adjacency list of directed 

        graph = [[] for _ in range(n)]
        for u,v in edges: 
            graph[u].append(v)
            graph[v].append(u)


        # Will there be an issue with this approach of DFS in undirected graph like double counting etc. 

        state = [0] * n

        def dfs(node, parent ): 
            
            if  state[node] != 0 : 
                return False 
            
            # Mark as visiting
            state[node] = 1 


            # Visit the neighbors
            for neighbor in graph[node]: 
                if neighbor!= parent: 
                    if not dfs(neighbor, node ): 
                        return False 

            # Mark as visited   
            
            state[node] = 2
            return True 
    
        # Run the algo
        if not dfs(0, -1):
            return False
        
        # If all not visited -> means not connected then return False 
        for node in state: 
            if node != 2: 
                return False 
            
        return True
