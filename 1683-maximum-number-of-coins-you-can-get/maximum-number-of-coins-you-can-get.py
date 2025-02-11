class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        coin=0
        piles.sort()
        n=[]
        i=0
        # while i<len(piles):
        #     n=[piles[0],piles[-2],piles[-1]]
        #     piles.remove(piles[0])
        #     piles.remove(piles[-2])
        #     piles.remove(piles[-1])
        #     coin+=n[1]
        #     i+=1
        # return coin
        l=0
        for pile in piles[len(piles)//3:]:
            
            if l%2==0:
                coin+=pile
            l+=1
        return coin


        