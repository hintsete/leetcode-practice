class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0
        while maxDoubles!=0 and target>1:
            if target%2!=0:
                target-=1
                count+=1
            else:
                target=target//2
                count+=1
                maxDoubles-=1
                
            print(target,count)
        print(target)
        if maxDoubles==0:
            count+=(target-1)
        return count

        # else:
        #     while maxDoubles>0:
        #         if target%2!=0:
        #             count+=1
        #             target-=1
        #         else:
        #             target=target//2
        #             maxDoubles-=1
        #         print(target,count)
        
        # return count
        