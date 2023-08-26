# https://leetcode.com/problems/length-of-last-word
# Runtime 39ms (69.91%)
# Memory 16.42mb (14.45%)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
