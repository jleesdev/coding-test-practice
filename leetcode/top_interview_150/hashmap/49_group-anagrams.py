# https://leetcode.com/problems/group-anagrams
# Runtime 102ms (73.41%)
# Memory 20.57mb (43.30%)
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            anagram[key].append(s)
        # print(anagram)

        return anagram.values()
