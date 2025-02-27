# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=fast=head
        first_half=[]
        second_half=[]
        while fast and fast.next:
            first_half.append(slow.val)
            slow=slow.next
            fast=fast.next.next
        while slow:
            second_half.append(slow.val)
            slow=slow.next
        print(first_half)
        print(second_half)
        second_half=second_half[::-1]
        print(second_half)
        # return[ max(x+y) for x, y in zip(first_half,second_half)]
        max_sum=0
        for x,y in zip(first_half,second_half):
            curr_sum=x+y
            max_sum=max(max_sum,curr_sum)
        return max_sum


        