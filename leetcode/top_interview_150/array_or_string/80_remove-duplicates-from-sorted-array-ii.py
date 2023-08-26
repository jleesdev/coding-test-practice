# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        dup_flag = 0
        while i < len(nums):
            if nums[i - 1] != nums[i]:
                i += 1
                dup_flag = 0
            elif nums[i - 1] == nums[i] and dup_flag == 0:
                i += 1
                dup_flag = 1
            else:
                nums[i:] = nums[i + 1:]

        return len(nums)
