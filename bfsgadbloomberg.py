from collections import deque


class Solution:
    def caroasis(self, grid, gas):
        rows = len(grid)
        cols = len(grid[0])

        start = target = None

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'c':
                    start = (r,c)
                if grid[r][c] == 'o':
                    target = (r,c)

        if start is None or target is None:
            return False

        que = deque([(start[0], start[1], 0)])
        visited = set()
        visited.add(start)
        dist = [(1,0), (-1,0), (0,1), (0,-1)]
        i = 0
        while que:
            for _ in range(len(que)):
                r,c,d = que.popleft()
                if d > gas:
                    continue
                if (r,c) == target:
                    return i
                for dr, dc in dist:
                    rw, cl = dr+r, dc+c
                    if 0<= rw < rows and 0 <= cl < cols and (rw, cl) not in visited and grid[rw][cl] != 'r':
                        if grid[rw][cl] != '.' and grid[rw][cl] != 'o':
                            gas += int(grid[rw][cl])
                        visited.add((rw,cl))
                        que.append((rw, cl, d +1))
            i +=1
        return False

sol = Solution()
grid= [
    ['.', '.', '.', 'c'],
    ['.', 'r', '1', '.'],
    ['.', 'r', 'r', 'r'],
    ['.', '.', 'o', '.'],
]
gas = 10
print(sol.caroasis(grid,gas))