# https://leetcode.com/problems/simplify-path (Medium)
# Runtime 39ms (81.70%)
# Memory 16.54mb (7.07%)


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        answer = ''

        for name in path:
            if name != '' and name != '.':
                if name == '..':
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(name)

        answer = '/' + '/'.join(stack)
        # print(stack, answer)

        return answer
