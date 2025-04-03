class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        # parentheses=("("*n) + (")"*n)
        # print(parentheses)

        def backtrack(open_c,close_c,path):
            #basecase
            if len(path)==2*n:
                ans.append("".join(path[:]))
                return
            if open_c<n:
                path.append("(")
                backtrack(open_c+1,close_c,path)
                path.pop()
            if close_c<open_c:
                path.append(")")
                backtrack(open_c,close_c+1,path)
                path.pop()
           
            
            return ans
        return backtrack(0,0,[])

        