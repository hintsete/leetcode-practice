class Solution:
    def punishmentNumber(self, n: int) -> int:
        def is_punishment_num(i):
            s = str(i * i)
            def dfs(s, target):
                if not s and target == 0:
                    return True
                for j in range(1, len(s)+1):
                    num = int(s[:j])
                    if num > target:
                        continue
                    if dfs(s[j:], target - num):
                        return True
                return False
            return dfs(s, i)
        
        ans = 0
        for i in range(n, 0, -1):  
            if is_punishment_num(i):
                ans += i * i
        return ans
            



            
        