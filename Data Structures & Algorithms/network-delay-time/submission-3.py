class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = [[] for _ in range (n+1)]

        # Adjacency list
        for u,v,t in times: 
            graph[u].append((v,t))

        visited = set()

        minheap = [(0,k)] # (dist from k, node)


        dist = 0 
        while len(visited) < n: 
            
            # something can't be visited
            if not minheap: 
                return -1

            dist_from_k, node = heapq.heappop(minheap)

            # If already visited do nothing
            if node in visited:
                continue

            # This is unvisited node - greedily dist is finalized
            visited.add(node)

            dist = max(dist,dist_from_k)

            # now populate the heap

            for neighbor, weight in graph[node] :
                # Add the unvisited ones to the minheap
                if neighbor not in visited: 
                    heapq.heappush(minheap, (dist_from_k +weight ,neighbor))

        return dist


            
