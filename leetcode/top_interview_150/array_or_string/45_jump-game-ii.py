# https://leetcode.com/problems/jump-game-ii
# Runtime 4352ms (23.55%)
# Memory 17.40mb (77.20%)


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        INF = float('inf')
        dp = [INF] * n
        dp[0] = 0

        for idx in range(n - 1):
            step = nums[idx]
            for next_idx in range(idx + 1, idx + step + 1):
                if next_idx < n:
                    dp[next_idx] = min(dp[idx] + 1, dp[next_idx])

        return dp[-1]
