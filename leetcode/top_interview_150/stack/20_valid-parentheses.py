# https://leetcode.com/problems/valid-parentheses (Easy)
# Runtime 35ms (88.04%)
# Memory 16.21mb (83.49%)
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for char in s:
            if char in ['}', ')', ']']:
                if len(stack) == 0:
                    return False
                else:
                    prev_char = stack.pop()
                    if char == '}' and prev_char == '{':
                        continue
                    elif char == ')' and prev_char == '(':
                        continue
                    elif char == ']' and prev_char == '[':
                        continue
                    else:
                        return False
            else:
                stack.append(char)

        if len(stack) > 0:
            return False
        else:
            return True
