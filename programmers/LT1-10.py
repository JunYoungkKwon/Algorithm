# [리트코드] Min Cost Climbing Stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 인덱스 0 or 1부터 시작
        # 비용 지불하면 한칸 or 두칸 오름

        n = len(cost)
        dp = [0] * (n + 1)

        # dp[i]는 비용 자체가 아니라 누적 최소 비용
        # 시작점에서는 비용을 내지 않는다
        # cost[i]는 i를 밟을 때만 지불

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]

