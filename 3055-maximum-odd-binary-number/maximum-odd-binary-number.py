class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zero=0
        one=0
        for ch in s:
            if ch=="1":
                one+=1
            else:
                zero+=1
        if one==1:
            return zero*"0"+"1"
        else:
            return (one-1)*"1"+(zero * "0")+"1"
        