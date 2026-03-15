from collections import defaultdict, deque


class Solution:
    def topoSort(self, V, edges):
        indegree = [0]*V
        que = deque()
        print("Yash")
        visited = set()
        resp = []
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        for i in range(V):
            for nei in adj[i]:
                indegree[nei] += 1
        print(indegree)

        for i, val in enumerate(indegree):
            if val == 0:
                que.append(i)
        print(que)

        ans = []
        while que:
            q = que.popleft()
            resp.append(q)
            for nei in adj[q]:
                indegree[nei] -=1
                if (indegree[nei] == 0):
                    que.append(nei)
        print(resp)
        return resp



sol = Solution()
sol.topoSort(4, [[3, 0], [1, 0], [2, 0]])