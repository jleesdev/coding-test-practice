# https://leetcode.com/problems/minimum-size-subarray-sum
# Runtime 212ms (97.30%)
# Memory 29.50mb (23.35%)


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        answer = n+1
        start = 0
        end = 1
        current_sum = sum(nums[start:end])

        while True:
            if start == n and end == n :
                break
            if answer == 1:
                break
            else:
                if current_sum >= target:
                    answer = min(answer, end - start)
                    current_sum -= nums[start]
                    start += 1
                if current_sum < target:
                    if end >= n:
                        break
                    current_sum += nums[end]
                    end += 1

        if answer == n+1:
            answer = 0

        return answer
