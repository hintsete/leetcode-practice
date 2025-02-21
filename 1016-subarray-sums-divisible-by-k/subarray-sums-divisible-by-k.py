class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=defaultdict(int)
        prefix[0]=1
        count=0
        running_sum=0
        for num in nums:
            running_sum+=num
            r=running_sum%k
            if r<0:
                count+=k
            count+=prefix[r]
            prefix[r]+=1
        return count
        
