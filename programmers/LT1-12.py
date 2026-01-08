# [리트코드] House Robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]

        # dp[n] n집까지의 최대 금액

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2], dp[i - 3] + nums[i])

        # nums
        # [2,1,1,2]
        # dp
        # [2,1,3,0]

        return dp[n - 1]