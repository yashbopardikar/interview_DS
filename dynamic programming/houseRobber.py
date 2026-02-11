from typing import List


class HouseRobber:
    # Reccurssion and memozation
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        def solve(i):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            steal = nums[i] + solve(i+2)
            skip = solve(i+1)
            dp[i] = max(steal, skip)
            return dp[i]

        return solve(0)

    # bottom Up

    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n ==1: return nums[0]
        dp = [0] * (n+1)
        dp[1] = nums[0]

        for i in range(2, n+1):
            steal = nums[i-1] + dp[i-2]
            skip = dp[i-1]
            dp[i] = max(steal, skip)

        return dp[n]


    # bottom Up in constant Space
    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n ==1:
            return nums[0]
        dp = [0] * (n+1)
        dp[1] = nums[0]
        prevprev = 0
        prev = nums[0]

        for i in range(2, n+1):
            steal = nums[i-1] + prevprev
            skip = prev
            temp = max(steal, skip)
            prevprev = prev
            prev = temp

        return prev


sol = HouseRobber()
# print(sol.rob([1,2,3,1]))
print(sol.rob2([1,2,3,1]))

