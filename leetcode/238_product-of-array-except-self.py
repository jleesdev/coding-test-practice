# https://leetcode.com/problems/product-of-array-except-self
# Runtime 189ms (91.65%)
# Memory 25.51mb (15.22%)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_answers = [1] * n
        right_answers = [1] * n

        for idx in range(1, n):
            left_answers[idx] = left_answers[idx - 1] * nums[idx - 1]

        for idx in range(n - 2, -1, -1):
            right_answers[idx] = right_answers[idx + 1] * nums[idx + 1]

        answers = [left_answers[idx] * right_answers[idx] for idx in range(n)]
        # print(left_answers, right_answers, answers)

        return answers
