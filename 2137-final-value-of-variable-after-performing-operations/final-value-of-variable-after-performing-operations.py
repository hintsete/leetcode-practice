class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        X=0
        for char in operations:
            if char=="X--" or char=="--X":
                X-=1
            elif char=="X++" or char=="++X":
                X+=1

        return X
        