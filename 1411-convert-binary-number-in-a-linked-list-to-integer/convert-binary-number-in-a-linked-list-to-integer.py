# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current=head
        binary_list=[]
        while current:
            binary_list.append(str(current.val))
            current=current.next
        print(binary_list)
        return int("".join(binary_list),2)
        
        # print(binary_str)
        # return int(my_str,2)