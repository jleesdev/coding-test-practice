# https://leetcode.com/problems/integer-to-roman
# Runtime 50ms (83.59%)
# Memory 16.32mb (55.34%)


class Solution:
    def intToRoman(self, num: int) -> str:
        nums = []
        for denom in [1000, 100, 10, 1]:
            quotient = num // denom
            nums.append(quotient)
            remainder = num % denom
            num = remainder

        roman = ''
        for i, num in enumerate(nums):
            if num != 0:
                if i == 0:
                    for _ in range(num):
                        roman += 'M'
                elif i == 1:
                    if num == 4:
                        roman += 'CD'
                    elif num == 9:
                        roman += 'CM'
                    else:
                        if num >= 5:
                            roman += 'D'
                            num -= 5
                        for _ in range(num):
                            roman += 'C'
                elif i == 2:
                    if num == 4:
                        roman += 'XL'
                    elif num == 9:
                        roman += 'XC'
                    else:
                        if num >= 5:
                            roman += 'L'
                            num -= 5
                        for _ in range(num):
                            roman += 'X'
                elif i == 3:
                    if num == 4:
                        roman += 'IV'
                    elif num == 9:
                        roman += 'IX'
                    else:
                        if num >= 5:
                            roman += 'V'
                            num -= 5
                        for _ in range(num):
                            roman += 'I'

        return roman
