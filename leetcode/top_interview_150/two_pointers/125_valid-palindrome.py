# https://leetcode.com/problems/valid-palindrome
# Runtime 46ms (88.15%)
# Memory 17.90mb (27.13%)
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        idx = 0
        n = len(s)

        flag = True
        while idx < int(n / 2):
            if s[idx] == s[n - 1 - idx]:
                idx += 1
            else:
                flag = False
                break

        return flag
