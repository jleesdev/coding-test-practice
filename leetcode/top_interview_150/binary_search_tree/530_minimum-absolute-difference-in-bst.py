# https://leetcode.com/problems/minimum-absolute-difference-in-bst (Easy)
# Runtime 56ms (79.07%)
# Memory 18.80mb (15.56%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = 100000
        sorted_nums = []

        def inorder(node):
            if node is None:
                return None
            else:
                inorder(node.left)
                sorted_nums.append(node.val)
                inorder(node.right)

        inorder(root)
        print(sorted_nums)
        for i in range(1, len(sorted_nums)):
            min_diff = min(min_diff, sorted_nums[i] - sorted_nums[i - 1])

        return min_diff
