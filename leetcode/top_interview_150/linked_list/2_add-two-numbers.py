# https://leetcode.com/problems/add-two-numbers (Medium)
# Runtime 73ms (51.85%)
# Memory 16.36mb (63.87%)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        tmp = 0
        while True:
            if l1 is None and l2 is None:
                break
            elif l1 is None:
                val1 = 0
                val2 = l2.val
                l2 = l2.next
            elif l2 is None:
                val1 = l1.val
                l1 = l1.next
                val2 = 0
            else:
                val1 = l1.val
                val2 = l2.val
                l1 = l1.next
                l2 = l2.next

            val = val1 + val2 + tmp
            if val >= 10:
                answer.append(val - 10)
                tmp = 1
            else:
                answer.append(val)
                tmp = 0
            # print(answer)

        if tmp == 1:
            answer.append(tmp)
        head = ListNode(answer[0])
        node = head
        for i in range(1, len(answer)):
            node.next = ListNode(answer[i])
            node = node.next

        # print(head)
        return head
