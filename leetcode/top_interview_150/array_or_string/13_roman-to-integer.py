# https://leetcode.com/problems/roman-to-integer
# Runtime 54ms (69.67%)
# Memory 16.50mb (10.59%)


class Solution:
    def romanToInt(self, s: str) -> int:
        count = 0
        idx = 0
        while idx < len(s):
            if s[idx] == 'I':
                if idx+1 < len(s) and s[idx+1] == 'V':
                    count += 4
                    idx += 1
                elif idx+1 < len(s) and s[idx+1] == 'X':
                    count += 9
                    idx += 1
                else:
                    count += 1
            elif s[idx] == 'V':
                count += 5
            elif s[idx] == 'X':
                if idx+1 < len(s) and s[idx+1] == 'L':
                    count += 40
                    idx += 1
                elif idx+1 < len(s) and s[idx+1] == 'C':
                    count += 90
                    idx += 1
                else:
                    count += 10
            elif s[idx] == 'L':
                count += 50
            elif s[idx] == 'C':
                if idx+1 < len(s) and s[idx+1] == 'D':
                    count += 400
                    idx += 1
                elif idx+1 < len(s) and s[idx+1] == 'M':
                    count += 900
                    idx += 1
                else:
                    count += 100
            elif s[idx] == 'D':
                count += 500
            elif s[idx] == 'M':
                count += 1000
            else:
                print('invalid symbol')
                break
            idx += 1

        return count
    