# https://leetcode.com/problems/merge-sorted-array/description


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m+n and j < n:
            num1 = nums1[i]
            num2 = nums2[j]

            if num1 == 0 and i >= m+j:
                nums1[i:] = nums2[j:]
                break
            elif num1 > num2:
                tmp = nums1[i:]
                nums1[i] = num2
                nums1[i+1:] = tmp[:-1]
                i += 1
                j += 1
            else:
                i += 1
