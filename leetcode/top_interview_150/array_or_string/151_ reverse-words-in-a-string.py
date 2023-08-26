# https://leetcode.com/problems/reverse-words-in-a-string
# Runtime 33ms (95.34%)
# Memory 16.36mb (83.35%)


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
