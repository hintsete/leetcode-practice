class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunk=0
        while numBottles>=numExchange:
            numBottles-=numExchange
            numBottles+=1
            drunk+=numExchange
        return numBottles+drunk

        