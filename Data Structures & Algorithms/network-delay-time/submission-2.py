class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = [[] for _ in range(n+1)]

        for u,v,time in times: 
            graph[u].append((time, v))

        minheap = [(0,k)]
        visited = set()
        
        time = 0 
        # dist = [0] * n 
        while minheap: 
            weight_node, node = heapq.heappop(minheap)

            if node in visited:
                continue

            visited.add(node)
            time = max(time, weight_node )
            # dist[node-1] = weight_node
            
            for edge_weight, neighbor in graph[node]: 

                if neighbor not in visited: 
                    heapq.heappush(minheap, (weight_node + edge_weight, neighbor))

        return time if len(visited) == n else -1

