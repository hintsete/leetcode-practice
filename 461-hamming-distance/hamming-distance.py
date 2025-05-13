class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        tot=x^y
        count=0
        while tot>0:
            count+=tot%2
            tot=tot//2
        return count

        
       