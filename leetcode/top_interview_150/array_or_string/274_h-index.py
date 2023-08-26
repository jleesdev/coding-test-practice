# https://leetcode.com/problems/h-index
# Runtime 42.0ms (90.00%)
# Memory 16.59mb (84.21%)


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        n = len(citations)
        h_idx = 0

        for i in range(n):
            # many papers but few citations
            # e.g. [1, 0, 3, 5, 6]
            if n-i >= citations[i] and h_idx < citations[i]:
                h_idx = citations[i]
            # many citations but few papers
            # e.g. [100] or [100,99]
            elif n-i <= citations[i] and h_idx < n-i:
                h_idx = n-i

        return h_idx
