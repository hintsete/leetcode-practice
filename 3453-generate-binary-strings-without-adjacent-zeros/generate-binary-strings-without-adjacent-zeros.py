class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans=[]
        def dfs(path,idx):
            if len(path)==n:
                ans.append("".join(path))
                return
            path.append("1")
            dfs(path,idx+1)
            path.pop()
            if not path or path[-1]!="0":
                path.append("0")
                dfs(path,idx+1)
                path.pop()


        dfs([],0)
        return ans

        