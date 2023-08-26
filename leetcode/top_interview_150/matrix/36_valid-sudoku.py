# https://leetcode.com/problems/valid-sudoku
# Runtime 105ms (68.79%)
# Memory 16.37mb (49.97%)
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_nums = defaultdict(list)
        col_nums = defaultdict(list)
        sub_nums = defaultdict(list)

        r, c = len(board), len(board[0])
        for i in range(r):
            for j in range(c):
                num = board[i][j]
                if num != '.':
                    row_nums[i].append(int(num))
                    col_nums[j].append(int(num))
                    sub_nums[3 * (i // 3) + j // 3].append(int(num))
        # print(row_nums, col_nums, sub_nums)

        for nums in [row_nums, col_nums, sub_nums]:
            for key in nums:
                if len(nums[key]) != len(set(nums[key])):
                    return False

        return True
