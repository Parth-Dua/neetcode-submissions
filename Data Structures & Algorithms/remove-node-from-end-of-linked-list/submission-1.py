# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        l = 0 
        curr = head
        while curr: 
            l+=1
            curr = curr.next 

        dummy = ListNode(val= -1, next= head)
        dummyHead = dummy

        for i in range(l-n ): 
            # Everything before the node we want to remove
            dummy = dummy.next

        dummy.next = dummy.next.next

        
        return dummyHead.next