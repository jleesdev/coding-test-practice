# https://leetcode.com/problems/majority-element
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        n = len(nums)
        for num in nums:
            count[num] += 1
            if count[num] > n/2:
                break
        return num
