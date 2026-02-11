import random
import bisect
from typing import List

class Solution:

    def __init__(self, w: List[tuple[str, int]]):
        """
        Build prefix sum array.
        Example:
        w = [1, 3, 2]
        prefix = [1, 4, 6]
        """
        self.w = w
        self.prefix = []
        running_sum = 0

        for s, weight in w:
            running_sum += weight
            self.prefix.append(running_sum)

        # Total sum of weights
        self.total = running_sum

    def pickIndex(self) -> int:
        """
        Generate a random number in range [1, total]
        and find the smallest index whose prefix sum >= random number
        """
        target = random.randint(1, self.total)

        # Binary search to find the first index >= target
        index = bisect.bisect_left(self.prefix, target)
        return self.w[index][0]

w = [('x', 1), ('y',3)]
obj = Solution(w)
param_1 = obj.pickIndex()
print(param_1)