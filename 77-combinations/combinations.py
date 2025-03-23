class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def dfs(firstNum,path):
            if len(path)==k:
                ans.append(path[:])
                return
            for candidate in range(firstNum,n+1):
                # print(candidate)
                path.append(candidate)
                # print(path)
                dfs(candidate+1,path)
                # print(path)
                path.pop()
                # print(path)
        dfs(1,[])
        return ans 
       
      
        