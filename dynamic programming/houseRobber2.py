from typing import List


class HouseRobber:
    # recurssion and memoization
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n ==1:
            return nums[0]
        if n == 2:
            return max(nums)

        def solve(i, n):
            if i > n:
                return 0
            if dp[i] != -1:
                return dp[i]
            steal = nums[i] + solve(i + 2, n)
            skip = solve(i + 1, n)
            dp[i] = max(steal, skip)
            return dp[i]

        dp = [-1] * (n + 1)
        index_0th = solve(0,n-2)
        dp = [-1] * (n + 1)
        index_1th = solve(1,n-1)
        return max(index_0th, index_1th)

# Bottom up Dp
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        dp = [0] * (n+1)
        for i in range(1, n):
            skip = dp[i-1]
            steal = nums[i-1] + (dp[i-2] if i-2 >= 0 else 0)
            dp[i] = max(skip, steal)
        result1 = dp[n-1]
        dp = [0] * (n + 1)
        dp[1] = 0
        for i in range(2, n+1):
            skip = dp[i-1]
            steal = nums[i-1] + (dp[i-2] if i-2 >= 0 else 0)
            dp[i] = max(skip, steal)
        result2 = dp[n]
        return max(result1, result2)

sol = HouseRobber()
print(sol.rob1([1,2,3,1]))



