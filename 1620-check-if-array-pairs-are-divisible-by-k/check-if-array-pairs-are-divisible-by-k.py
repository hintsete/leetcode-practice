class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq=[0 for i in range(k)]
        for num in arr:
            freq[num%k]+=1

        for i in range(1,k):
            if i== k-i and freq[i] & 1:
                return False
            if freq[i] != freq[k-i]:
                return False

        return True
       