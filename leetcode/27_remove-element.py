# https://leetcode.com/problems/remove-element


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            num = nums[i]
            if num == val:
                nums[i:] = nums[i+1:]
                # not necessary code: nums = nums[:-1]
            else:
                i += 1
            # print(nums)

        return len(nums)
