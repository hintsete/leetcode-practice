class Solution:
    def removeStars(self, s: str) -> str:
        # traverse through the string while adding and removing at O(n)
        stack=[]
        for ch in s:
            if ch=="*" and stack:

                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)
        