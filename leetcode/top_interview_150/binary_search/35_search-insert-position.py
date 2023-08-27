# https://leetcode.com/problems/search-insert-position (Easy)
# Runtime 56ms (70.47%)
# Memory 17.12mb (54.55%)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n

        while True:
            idx = (start + end) // 2
            # print(start, end, idx)
            if nums[idx] == target:
                return idx
            elif target > nums[idx]:
                start = idx + 1
            else:
                end = idx
            # print(start, end, idx)
            if start >= end:
                return start
