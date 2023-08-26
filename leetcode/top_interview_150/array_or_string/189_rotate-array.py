# https://leetcode.com/problems/rotate-array


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        remainder = k % n
        nums[:] = nums[-remainder:] + nums[:-remainder]
