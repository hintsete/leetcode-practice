class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count=Counter(arr)
        half=len(arr)//2
        value=[]
        # key=[]
        for idx,val in count.items():
            value.append(val)
        value.sort(reverse=True)
        prefix=list(accumulate(value))
        print(value)
        print(prefix)
        i=0
        c=0
        while i<len(arr):
            if prefix[i]>=half:
                # key.append(prefix[i])
                c+=1
                break

            i+=1
            c+=1
        return c
        # for i in range(len(arr)):
        #     if 
            # if value[i]>=half:
            #     return len(arr)-value[i]
            # else:
            #     key.append(value[i])

        