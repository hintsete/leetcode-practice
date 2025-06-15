class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l=0
        r=1
        n=len(intervals)
        intervals.sort(key=lambda x:x[0])
        res=[]
        curr=intervals[0]
        while r<n:
            st1,ed1=curr
            st2,ed2=intervals[r]
            if st2<=ed1:
                curr=st1,max(ed1,ed2)
        

            else:
                res.append(curr)
                curr=intervals[r]

            l+=1
            r+=1

            # else:
                # res.append([st1,ed1])
                # res.append([st2,ed2])

        res.append(curr)
        return res

        
            



       
      

