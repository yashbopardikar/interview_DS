from collections import defaultdict
class Solution:
    def topoSort(self, V, edges):
        # Code here
        visited = set()
        stack = []
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        def dfs(adj, u, visited, stack):
            visited.add(u)
            for nei in adj[u]:
                if nei not in visited:
                    dfs(adj, nei, visited, stack)
            stack.append(u)

        for i in range(V):
            if i not in visited:
                dfs(adj, i, visited, stack)
        return stack[::-1]


sol = Solution()
print(sol.topoSort(4,[[3, 0], [1, 0], [2, 0],[0,3]]))