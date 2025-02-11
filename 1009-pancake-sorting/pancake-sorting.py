class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # res=[]
        # for num in arr:
        #     arr=arr[:num].reverse()
        # print(arr)
        # return arr
        new_arr=sorted(arr)
        k=[]
        for i in range(len(arr)):
            b=new_arr[-1]
            max_idx=arr.index(b)
            k.append(max_idx+1)
            arr=arr[:max_idx+1 ][::-1]+arr[max_idx+1:]
            print(arr)
            k.append(len(arr))
            arr=arr[::-1]
            arr.pop()
            new_arr.pop()

        return k
        






        