from collections import defaultdict

class Solution:
    def minimumReversals(self, n: int, edges: list[list[int]]) -> list[int]:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append((v,0))
            adj[v].append((u,1))

        visited = set()
        resp = [0] * n

        def dfs_count(node):
            visited.add(node)
            total_cost = 0
            for nei, cost in adj[node]:
                if nei not in visited:
                    immediate_cost = cost
                    sub_tree_cost = dfs_count(nei)
                    total_cost += immediate_cost + sub_tree_cost
            return total_cost

        resp[0] = dfs_count(0)
        visited.clear()

        def dfs_reroot(node):
            visited.add(node)
            for nei, edge_cost in adj[node]:
                if nei not in visited:
                    if edge_cost == 0:
                        resp[nei] = resp[node] + 1
                    else:
                        resp[nei] = resp[node] - 1
                    dfs_reroot(nei)



        dfs_reroot(0)
        return resp

n = 4
edges = [[2,0],[2,1],[1,3]]
sol = Solution()
print(sol.minimumReversals(n,edges))

