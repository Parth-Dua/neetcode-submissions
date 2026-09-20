class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u,v in edges: 
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node ): 
            if node in visited: # For cycles 
                return 

            visited.add(node)

            for neighbor in graph[node]: 
                 
                    dfs(neighbor )
            
            return 

        
        count = 0
        for node in range(n): 
            if node not in visited: 
                count+=1 
                dfs(node )

        return count 

        