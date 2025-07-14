class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited=set()
        stack=[]
        last_occur={ch:i for i,ch in enumerate(s)}
        print(last_occur)
        for i,ch in enumerate(s):
            if ch in visited:
                continue
            while stack and ch<stack[-1] and i<last_occur[stack[-1]]:
                popped=stack.pop()
                visited.remove(popped)

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)
