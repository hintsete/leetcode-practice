class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        unfair=float("inf")
        # def valid(path):
        #     #if the number of unique elements in path is >= k it is valid
        #     #else not valid
        #     for p in path:
        #         if p==0:
        #             return False
                
        #     return True
        def backtrack(path,idx):
            nonlocal unfair
            if max(path)>=unfair:
                return
            if idx==len(cookies):
                curr_unfairness=(max(path))
                unfair=min(unfair,curr_unfairness)
                return
            for i in range(k):
                path[i]+=cookies[idx]
                backtrack(path,idx+1)
                path[i]-=cookies[idx]

                #if valid
                # path[0].append(cookies[i])
                # backtrack(path)
                # path.pop()
                
            
                # path.append(candidate)
                # backtrack(path)
                # unfair(max(sum(cookies[:idx+1]),sum(cookies[idx+1:])))
                # path.pop()

        backtrack([0]*k,0)
        return unfair




        