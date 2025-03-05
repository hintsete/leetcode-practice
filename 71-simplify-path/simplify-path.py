class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        paths=path.split("/")
        print(paths)
        for p in paths:
            if p=="" or p==".":
                continue
            elif  p==".." and stack:
                stack.pop()

            elif p!="..":
                stack.append(p)
        
        return "/"+"/".join(stack)
            
