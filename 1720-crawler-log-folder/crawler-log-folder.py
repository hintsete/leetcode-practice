class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for log in logs:
            if log !="../" and log!="./":
                stack.append(log)
            elif log=="../":
                if stack:
                    stack.pop()
                
            elif log=="./":
                continue
        return len(stack)

        