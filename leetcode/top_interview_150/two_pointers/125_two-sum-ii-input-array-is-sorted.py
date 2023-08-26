# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# Runtime 132ms (53.04%)
# Memory 17.20mb (58.01%)


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1 = 0
        idx2 = len(numbers) - 1

        while idx1 < idx2:
            number = numbers[idx1] + numbers[idx2]
            if target == number:
                break
            elif target > number:
                idx1 += 1
            else:  # target < number
                idx2 -= 1

        return [idx1+1, idx2+1]
