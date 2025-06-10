class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost_k(nums,k):

            n=len(nums) 
            count=0
            l=0
            window=defaultdict(int)
            unique=0
            for r in range(n):
                if window[nums[r]]==0:
                    unique+=1
                window[nums[r]]+=1
                while unique>k:
        
                    window[nums[l]]-=1
                    if window[nums[l]]==0:
                        unique-=1

                    l+=1
                count+=r-l+1

            
            return count


        return atmost_k(nums,k)-atmost_k(nums,k-1)       