# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self,head,k):
        prev=None
        current=head
        length=0
        while current and length<k:
            
            nextnode=current.next
            current.next=prev
            prev=current
            current=nextnode
            length+=1
        return prev
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        current=head
        while current:
            length+=1
            current=current.next
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy
        current=head
        while length>=k:
         
            slow=current
            fast=current
            for _ in range(k):
                fast=fast.next

            # print(current)
            newhead=self.reverse(current,k)
            prev.next=newhead
            slow.next=fast
            prev=slow
            current=fast

            length-=k
        return dummy.next

        