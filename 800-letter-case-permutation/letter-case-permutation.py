class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=[]
        def backtrack(path, idx):
            #basecase
            if idx==len(s):
                ans.append("".join(path))
                return

            char=s[idx]
            if char.isalpha():

                path.append(char.upper())
                backtrack(path,idx+1)
                path.pop()
                
                path.append(char.lower())
                backtrack(path,idx+1)
                path.pop()

            else:
                path.append(char)
                backtrack(path,idx+1)
                path.pop()
            

           
           
        backtrack([],0)
        return ans
            
        