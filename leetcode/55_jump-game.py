# https://leetcode.com/problems/jump-game


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left_jump = nums[0]

        for idx in range(1, len(nums)):
            if left_jump == 0:
                return False

            left_jump -= 1

            if left_jump < nums[idx]:
                left_jump = nums[idx]

        return True
