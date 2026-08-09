# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 

        second = slow.next
        slow.next = None
        prev = None
        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp 

        # prev is the start of reversed second half
        first, second = head, prev
        while second : # since second is gonna be shorter in both odd and even cases
            tmp1, tmp2 = first.next, second.next
            first.next = second 
            second.next = tmp1
            first = second.next
            second = tmp2

        
