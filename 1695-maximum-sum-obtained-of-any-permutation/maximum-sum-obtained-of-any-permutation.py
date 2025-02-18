class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq=[0]*(len(nums)+1)
        for start, end in requests:
            freq[start]+=1
            freq[end+1]-=1
        for i in range(1,len(freq)):
            freq[i]+=freq[i-1]
        nums.sort(reverse=True)
        freq.sort(reverse=True)
        res=0
        
        for num,c in zip(nums,freq):
            res+=num*c
        return res%((10**9)+7)
            

        