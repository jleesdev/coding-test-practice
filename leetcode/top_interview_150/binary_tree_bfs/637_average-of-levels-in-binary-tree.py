# https://leetcode.com/problems/average-of-levels-in-binary-tree (Easy)
# Runtime 59ms (56.40%)
# Memory 18.85mb (68.29%)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        node_queue = [root]
        depth_queue = [1]
        count = []
        answer = []

        while node_queue:
            node = node_queue.pop(0)
            depth = depth_queue.pop(0)
            if depth > len(answer):
                answer.append(node.val)
                count.append(1)
            else:
                answer[depth-1] += node.val
                count[depth-1] += 1

            if node.left is not None:
                node_queue.append(node.left)
                depth_queue.append(depth+1)
            if node.right is not None:
                node_queue.append(node.right)
                depth_queue.append(depth+1)

        # print(answer, count)
        for i in range(len(answer)):
            answer[i] /= count[i]

        return answer
