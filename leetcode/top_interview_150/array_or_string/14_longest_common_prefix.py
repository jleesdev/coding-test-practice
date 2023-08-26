# https://leetcode.com/problems/longest-common-prefix
# Runtime 48ms (44.69%)
# Memory 16.25mb (92.37%)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum_length = 200
        for str in strs:
            length = len(str)
            if length < minimum_length:
                minimum_length = length

        prefix = ''
        for i in range(minimum_length):
            flag = True
            char = strs[0][i]
            for j in range(1, len(strs)):
                if char == strs[j][i]:
                    continue
                else:
                    flag = False
                    break
            if flag is True:
                prefix += char
            else:
                break

        return prefix
