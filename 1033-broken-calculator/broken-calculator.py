class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        half=ceil(target/2)
        count=0
        if startValue==target:
            return 0
        # return abs(half-startValue)+1
        while target>startValue:
            if target%2==0:
                target=target//2

            else:
                target+=1
            count+=1

       
        return count+(startValue-target)