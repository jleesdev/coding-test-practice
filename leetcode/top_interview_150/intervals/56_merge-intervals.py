# https://leetcode.com/problems/merge-intervals (Medium)
# Runtime 138ms (77.01%)
# Memory 21.35mb (21.49%)


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        # print(intervals)
        n = len(intervals)
        start, end = intervals[0]
        answers = []

        for i in range(1, n):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                answers.append([start, end])
                start, end = intervals[i]
        answers.append([start, end])

        return answers
