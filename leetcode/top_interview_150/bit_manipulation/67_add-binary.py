# https://leetcode.com/problems/add-binary (Easy)
# Runtime 42ms (71.95%)
# Memory 16.39mb (44.06%)


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
