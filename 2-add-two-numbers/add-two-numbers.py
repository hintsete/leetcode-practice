# Definition for singly-linked list.
# from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       

        # curr1=l1
        # curr2=l2
        dummy=ListNode()
        prev=dummy
        count=0
        while l1 or l2 or count:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            summation=val1+val2+count
            count=summation//10
            prev.next=ListNode(summation%10)
            # prev.next=new_node
            prev=prev.next
            if l1:
                l1=l1.next

            if l2:
                l2=l2.next

        

        return dummy.next


    


  
   