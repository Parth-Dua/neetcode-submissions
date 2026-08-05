# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(val= -1, next= None)
        dummyHead = dummy

        p1, p2 = list1, list2

        while p1 and p2: 
            if p1.val <= p2.val: 
                temp = p1
                p1 = p1.next
                dummy.next = temp
                dummy = dummy.next
            else: 
                temp = p2
                p2 = p2.next
                dummy.next = temp
                dummy = dummy.next

        if p1: 
            dummy.next = p1 
        elif p2:
            dummy.next = p2 
        
        return dummyHead.next
        



