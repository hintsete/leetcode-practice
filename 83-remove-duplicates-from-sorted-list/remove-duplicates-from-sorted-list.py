# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        if not head:
            return 
        while current and current.next:
            nextnode=current.next
            if current.val==nextnode.val:
                current.next=nextnode.next
            else:
                current=current.next
        return head
        