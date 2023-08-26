# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal (Medium)
# Runtime 63ms (91.02%)
# Memory 21.12mb (83.41%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {inorder[i]: i for i in range(len(inorder))}

        def buildSubTree(preorder, left, right):
            if len(preorder) == 0:
                return None
            if left < 0 or right > len(inorder):
                return None

            # do not pop the value before return None.
            root_idx = inorder_index[preorder[0]]
            if root_idx < left or root_idx > right:
                return None

            root = TreeNode(preorder.pop(0))
            root.left = buildSubTree(preorder, left, root_idx-1)
            root.right = buildSubTree(preorder, root_idx+1, right)
            # print(root)
            return root

        return buildSubTree(preorder, 0, len(inorder)-1)
