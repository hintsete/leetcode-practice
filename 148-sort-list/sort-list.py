# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def merge(left,right):
            dummy=ListNode()
            current=dummy
            while left and right:
                if left.val<=right.val:
                    current.next=left
                    left=left.next
                else:
                    current.next=right
                    right=right.next


                current=current.next

            current.next=left if left else right
            return dummy.next

          
        def mergesort(head):
            slow=head
            fast=head.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next

            mid=slow.next
            slow.next=None
            return head, mid

        left,right=mergesort(head)
        left_sorted=self.sortList(left)
        right_sorted=self.sortList(right)
        return merge(left_sorted,right_sorted)
        # def merge(left_half,right_half):
        #     sorted_arr=[]
        #     i=0
        #     j=0
        #     while i<len(left_half) and j <len(right_half):
        #         if curr

        #     return sorted_arr
        


        # def mergesort(l,r,curr):
        #     if l==r:
        #         return [l]

        #     slow=fast=head
        #     while curr and curr.next:
        #         slow=slow.next
        #         fast=fast.next.next

        #     slow.next=None
        #     left_arr=head
        #     right_arr=fast

        #     [1,2]


            
            # count=0
            # curr=head
            # while curr:
            #     count+=1
            #     curr=curr.next

            # print(count)
            # mid=count//2
            # left_arr= mergesort(l,mid)
            # right_arr=mergesort(mid,r)

            