class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        my_list=[]
        for i,j in ranges:
           for n in range(i,j+1):
            my_list.append(n)
        for num in range(left,right+1):
            if num not in my_list:
                return False
            
        return True
      
                    
            
