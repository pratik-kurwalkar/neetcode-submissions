# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        current_node = head
        next_node = current_node.next
        current_node.next = None
        next_to_next_node = next_node.next
        while next_to_next_node:
            next_node.next = current_node
            current_node = next_node
            next_node = next_to_next_node
            next_to_next_node = next_to_next_node.next
        next_node.next = current_node
        return next_node