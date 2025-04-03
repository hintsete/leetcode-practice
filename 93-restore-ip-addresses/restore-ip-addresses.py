class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # return []
        if len(s)>12:
            return []
        ans=[]

        
        def backtrack(path,idx):
            #basecase
            if len(path)==4 and idx==len(s):
                ans.append(".".join(path))
                return

            if len(path)==4:
                return
            

            
            for seg_len in range(1,4):
                if seg_len+idx>len(s):
                    break

                segment=s[idx:idx+seg_len]
                if (segment[0]=="0" and len(segment)>1) or int(segment)>255:
                    continue




                path.append(segment)
                backtrack(path,idx+seg_len)
                path.pop()
            return ans
        return backtrack([],0)
        
                    

        