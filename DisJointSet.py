class Solution:
    def __init__(self):
        self.rank = []
        self.parent = []

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(x)
        return self.parent[x]

    def union(self, x, y):
        x_parent = self.parent[x]
        y_parent = self.parent[y]

        if x_parent == y_parent:
            return
        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[y_parent] > self.rank[x_parent]:
            self.parent[x_parent] = y_parent
        elif self.rank[x_parent] == self.rank[y_parent]:
            self.parent[y_parent] = x_parent
            self.rank[x_parent] +=1

















    # def __init__(self):
    #     self.parent = []
    #     self.rank = []
    #
    # def find(self, x):
    #     if x == self.parent[x]:
    #         return self.parent[x]
    #     self.parent[x] = self.find(self.parent[x])
    #     return self.parent[x]
    #
    # def Union(self, x, y):
    #     x_parent = self.find(x)
    #     y_parent = self.find(y)
    #
    #     if x_parent == y_parent:
    #         return
    #     if self.rank[x_parent] > self.rank[y_parent]:
    #         self.parent[y_parent] = x_parent
    #     elif self.rank[x_parent] < self.rank[y_parent]:
    #         self.parent[x_parent] = y_parent
    #     elif self.rank[x_parent] == self.rank[y_parent]:
    #         self.parent[x_parent] = y_parent
    #         self.rank[y_parent] += 1