class Solution:
    def splitString(self, s: str) -> bool:
        def split(path,i):
            
            # for j in range(i,len(s)):
            if i==len(s):
                for j in range(1,len(path)):
                    if path[j-1]!=path[j]+1:
                        return False
                return len(path)>=2
            num=0
            for j in range(i,len(s)):
                num=num*10+int(s[j])
                # if not path or num==path[-1]-1:
                path.append(num)
                if split(path,j+1):
                    return True
                path.pop()
            return False
        return split([],0)
        # def valid(path):
        #     if len(path)<2:
        #         return False
        #     nums=[int(ch) for ch in s]
        #     for i in range(1,len(nums)):
        #         if nums[i-1]-nums[i]!=1:
        #             return False
        #     return True

        # def backtrack(start,path):
        #     if start==len(s):
        #         valid(path)
        #     for i in range(start+1,len(s)+1):
        #         sub_s=s[start:i]
        #         path.append(sub_s)
        #         if backtrack(i,path):
        #             return True
        #         path.pop()
        #     return False

        # return backtrack(0,[])
            

            
        