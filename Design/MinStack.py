class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val:int):
        if not self.stack:
            self.stack.append((val, val))
        else:
            min_val = self.stack[-1][1]
            self.stack.append((val, min(min_val, val)))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        return self.stack[-1][0] if self.stack else 0

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            raise ValueError




# sol = MinStack()
# sol.push(-2)
# sol.push(0)
# sol.push(-3)
# print(sol.getMin())
# sol.pop()
# print(sol.top())
# print(sol.getMin())
