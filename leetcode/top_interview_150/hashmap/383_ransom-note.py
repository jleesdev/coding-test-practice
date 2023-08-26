# https://leetcode.com/problems/ransom-note
# Runtime 65ms (65.71%)
# Memory 16.68mb (28.09%)
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_count = defaultdict(int)
        magazine_count = defaultdict(int)

        for char in ransomNote:
            note_count[char] += 1

        for char in magazine:
            magazine_count[char] += 1

        for char in note_count:
            if note_count[char] > magazine_count[char]:
                return False

        return True
