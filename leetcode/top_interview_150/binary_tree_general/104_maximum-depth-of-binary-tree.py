# https://leetcode.com/problems/maximum-depth-of-binary-tree (Easy)
# Runtime 51ms (55.44%)
# Memory 17.69mb (90.02%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        node_stack = [root]
        depth_stack = [1]
        max_depth = 1

        while len(node_stack) > 0:
            node = node_stack.pop()
            cur_depth = depth_stack.pop()

            if node.left is not None:
                node_stack.append(node.left)
                depth_stack.append(cur_depth+1)
                max_depth = max(max_depth, cur_depth+1)

            if node.right is not None:
                node_stack.append(node.right)
                depth_stack.append(cur_depth+1)
                max_depth = max(max_depth, cur_depth+1)

        return max_depth
