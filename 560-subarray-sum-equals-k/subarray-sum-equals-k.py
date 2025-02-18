class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        current_sum=0
        sub_arr=defaultdict(int)
        sub_arr[0]=1
        count=0
        for num in nums:
            current_sum+=num
            count+=sub_arr[current_sum-k]
            sub_arr[current_sum]+=1
        return count

        