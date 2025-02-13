class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        output=[]
        block_comment=False


        temp=""
        
        for i in range(len(source)):
            s=source[i]
            right=0
            while right<len(s):
                if s[right:right+2]=="/*" and not block_comment:
                    block_comment=True
                    right+=1
                elif s[right:right+2]=="*/" and block_comment:
                    block_comment=False
                    right+=1
                elif not block_comment and s[right:right+2]=="//":
                    break
                elif not block_comment:
                    temp+=s[right]
                right+=1

            if not block_comment and temp != "":
                output.append(temp)
                temp=""
        return output
        #     if "//" not in source[i] and "/*" not in source[i] and "*/" not in source[i]:
        #         output.append(source[i])
        # return output
        # # i=0
        # # while i+1<len(source):
        # #     if "//" not in source[i] and "/*" not in source[i] and "*/" not in source[i]:
        # #         output.append(source[i])
        # #     i+=1

        