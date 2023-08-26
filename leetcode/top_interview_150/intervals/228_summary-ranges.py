# https://leetcode.com/problems/summary-ranges (Easy)
# Runtime 44ms (44.26%)
# Memory 16.21mb (71.27%)


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answers = []

        n = len(nums)
        if n > 0:
            start = end = nums[0]
            for i in range(1, n):
                if nums[i] - end != 1:
                    answer = str(start)
                    if start < end:
                        answer += '->' + str(end)
                    answers.append(answer)
                    start = nums[i]
                end = nums[i]

            answer = str(start)
            if start < end:
                answer += '->' + str(end)
            answers.append(answer)

        return answers
