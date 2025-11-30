import collections
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        inrecursion = set()
        adj = collections.defaultdict(list)

        for crs,pre in prerequisites:
            adj[pre].append(crs)

        def dfs(course):
            visited.add(course)
            inrecursion.add(course)
            for nei in adj[course]:
                if nei not in visited and dfs(nei):
                    return True
                elif nei in inrecursion:
                    return True
            inrecursion.remove(course)
            return False

        for i in range(numCourses):
            if i not in visited and dfs(i):
                return False
        return True

sol = Solution()
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(sol.canFinish(numCourses, prerequisites))

