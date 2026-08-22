# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        index = length - n
        if index == 0:
            return head.next
        current = head
        for x in range(index - 1):
            current = current.next
        # if current == head:
        #     return head.next
        if current.next:
            current.next = current.next.next
        return head