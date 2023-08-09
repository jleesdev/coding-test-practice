# https://leetcode.com/problems/remove-duplicates-from-sorted-array


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        tmp = nums[i]
        i += 1
        while i < len(nums):
            if tmp == nums[i]:
                nums[i:] = nums[i+1:]
            else:
                tmp = nums[i]
                i += 1

        return len(nums)
