class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def dfs(element,path):
            ans.append(path[:])

            for i in range(element,len(nums)):
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
        dfs(0,[])
        return ans
            
    
        