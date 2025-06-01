class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        l=0
        r=len(answerKey)
        ans=0
        def valid(mid):
            flip=0
            for i in range(mid):
                if answerKey[i]!="T":
                    flip+=1
            if flip<=k:
                return True

            for i in range(mid,len(answerKey)):
                if answerKey[i]!="T":
                    flip+=1
                if answerKey[i-mid]!="T":
                    flip-=1

                if flip<=k:
                    return True
            flip=0
            for i in range(mid):
                if answerKey[i]!="F":
                    flip+=1
            if flip<=k:
                return True

            for i in range(mid,len(answerKey)):
                if answerKey[i]!="F":
                    flip+=1
                if answerKey[i-mid]!="F":
                    flip-=1

                if flip<=k:
                    return True
            return False


        while l<=r:
            mid=(l+r)//2
            if valid(mid):
                ans=mid
                l=mid+1

            else:
                r=mid-1

        return ans

            



        