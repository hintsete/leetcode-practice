# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        L_prev=dummy
        current=head
        for _ in range(left-1):
            L_prev=current
            current=current.next
        prev=None
        for _ in range((right-left)+1):
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        L_prev.next.next=current
        L_prev.next=prev
        return dummy.next

        


        # current=head
        # for _ in range(left-1):
        #     current=current.next
        # for _ in range((right-left)+1):
        #     prev=None
        #     current=head
        #     while current:
        #         next_node=current.next
        #         current.next=prev
        #         prev=current
        #         current=next_node
        


    
      