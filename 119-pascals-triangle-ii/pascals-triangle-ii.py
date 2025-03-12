class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def fib(num):
            if num==0 or num==1:
                return [1]*(num+1)

            nums=[1]*(num+1)  
            back=fib(num-1)
            for i in range(1,num):
                nums[i]=back[i-1]+back[i]
            return nums
        return fib(rowIndex)