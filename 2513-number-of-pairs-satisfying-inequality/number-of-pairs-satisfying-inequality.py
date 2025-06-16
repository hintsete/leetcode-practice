class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.count=0
        # nums1[i]+nums2[i]<=nums1[j]+nums2[j]+diff
        n=len(nums1)
        arr=[nums1[i]-nums2[i] for i in range(n)]

        def mergesort(l,r):
            if l>=r:
                return [arr[l]]

            mid=(l+r)//2
            left_half=mergesort(l,mid)
            right_half=mergesort(mid+1,r)
            # return merge(left_half,right_half)
            j=0
            for i in range(len(left_half)):
                while j<len(right_half) and left_half[i]>right_half[j]+diff:
                    j+=1

                self.count+=len(right_half)-j

            merged=[]
            i=0
            j=0
            while i<len(left_half) and j<len(right_half):
                if left_half[i]<=right_half[j]:
                    merged.append(left_half[i])
                    i+=1

                else:
                    merged.append(right_half[j])
                    j+=1

            merged.extend(left_half[i:])
            merged.extend(right_half[j:])
            return merged

        mergesort(0,n-1)

        return self.count
        
      


        