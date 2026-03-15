# dijkstra using min heap
from collections import defaultdict
import heapq


class Solution:
    def djks(V, edges, src):
        adj  = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))

        dist = [float('inf')] * V
        dist[src] = 0
        heap = [(0,src)]

        while heap:
            curr_d, node = heapq.heappop(heap)

            if curr_d > dist[node]:
                continue

            for nei, w in adj[node]:
                new_d = curr_d + w
                if new_d < dist[nei]:
                    dist[nei] = new_d
                    heapq.heappush(heap,(new_d, nei))

        return dist


# Example usage:
V = 3
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2

print(Solution.djks(V, edges, src))
