# https://leetcode.com/problems/linked-list-cycle (Easy)
# Runtime 707ms (5.01%)
# Memory 20.48mb (68.20%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        if node is None:
            return False
        nodes = [node]

        while True:
            if node.next is None:
                return False
            else:
                if node.next in nodes:
                    return True
                else:
                    node = node.next
                    nodes.append(node)
