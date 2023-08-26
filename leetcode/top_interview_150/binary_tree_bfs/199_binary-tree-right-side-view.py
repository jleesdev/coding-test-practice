# https://leetcode.com/problems/binary-tree-right-side-view (Medium)
# Runtime 40ms (74.11%)
# Memory 16.36mb (40.75%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        node_queue = [root]
        depth_queue = [1]
        depth_right_val = dict()

        while node_queue:
            node = node_queue.pop(0)
            depth = depth_queue.pop(0)
            depth_right_val[depth] = node.val

            if node.left is not None:
                node_queue.append(node.left)
                depth_queue.append(depth + 1)
            if node.right is not None:
                node_queue.append(node.right)
                depth_queue.append(depth + 1)

        print(depth_right_val)
        return depth_right_val.values()
