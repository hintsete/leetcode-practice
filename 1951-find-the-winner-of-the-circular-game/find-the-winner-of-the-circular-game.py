class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
 





        stack=[]
        for i in range(1,n+1):
            stack.append(i)
            
        def helper(stack,start):
            if len(stack)==1:
                return stack[0]
           
            remove_idx=(start+k-1)%len(stack)
            stack.pop(remove_idx)
            return helper(stack,remove_idx)
        
        return helper(stack,0)

       



        # nums=[]
        # for i in range(1,n+1):
        #     nums.append(i)
        # stack=deque()
        # for i in range(len(nums)):
        #     while i+1<k:


            



        # nums=[]
        # for i in range(1,n+1):
        #     nums.append(i)
        # # print(nums)
        # size=len(nums)
        # c=0
        
        # for idx in range(0, size*2):
        #     value=nums[idx%size]
        #     # window=[:k]
        #     # nums.remove(nums[k-1])
        #     # window-=nums[idx]
        #     # window+=nums[]
        #     lost=idx+(k-1)
            

            
        




     