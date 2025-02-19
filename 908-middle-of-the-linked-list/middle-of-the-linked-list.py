# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length=0
        current=head
        while current:
            length+=1
            current=current.next
        half=length//2
        while half>0:
            head=head.next
            half-=1
        return head