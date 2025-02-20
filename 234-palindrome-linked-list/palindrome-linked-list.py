# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev=None
        current=head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        return prev
    def isequal(self,n1,n2):
        while n1 and n2:
            if n1.val!=n2.val:
                return False
            n1=n1.next
            n2=n2.next
        return True


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return True
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        head2=self.reverse(slow)
        slow.next=None
        res=self.isequal(head,head2)
        head2=self.reverse(head2)
        slow.next=head2
        return res
        