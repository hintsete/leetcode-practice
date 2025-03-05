class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        left=0
        right=left+1
        count=0
        while left<len(flowerbed):
            if flowerbed[left]==1:
                left+=2
            else:
                if (left==0 or flowerbed[left-1]==0) and (right>=len(flowerbed) or flowerbed[right]==0 ):
                    count+=1
                    left+=2
                else:
                    left+=1
            right=left+1
        return n<=count
                    
        