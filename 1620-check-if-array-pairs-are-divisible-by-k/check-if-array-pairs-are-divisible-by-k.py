class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq=[0 for i in range(k)]
        for num in arr:
            freq[num%k]+=1

        if freq[0] %2 !=0:
            return False

        for i in range(1,(k//2)+1):
            if i==k-1:
                if freq[i] %2 !=0:
                    return False

            else:
                if freq[i]!=freq[k-i]:
                    return False
                    
        return True
