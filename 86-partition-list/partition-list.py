# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less=ListNode(None)
        l=less
        more=ListNode(None)
        m=more
        current=head
        while current:
            if current.val<x:
                l.next=current
                l=l.next

            else:
                m.next=current
                m=m.next
            current=current.next
        
        # print(less)
        # print(more)
        l.next=more.next
        m.next=None
        return less.next
    

     
