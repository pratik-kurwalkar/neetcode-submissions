# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        previous = head
        while True:
            current = None
            if list1 == None:
                previous.next = list2
                break
            if list2 == None:
                previous.next = list1
                break
            if list1.val < list2.val:
               current = list1
               list1 = list1.next
            else:
                current = list2
                list2 = list2.next
            previous.next = current
            previous = current
        return head
