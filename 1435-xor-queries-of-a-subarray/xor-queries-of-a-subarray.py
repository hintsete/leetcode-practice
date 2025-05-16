class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[0]+list(accumulate(arr,operator.xor))
        ans=[]
        for l,r in queries:
            ans.append(prefix[r+1]^prefix[l])

        return ans 

       


      
        