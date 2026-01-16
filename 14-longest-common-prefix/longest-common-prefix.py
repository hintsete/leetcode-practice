class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        pre=strs[0]
        for i in range(len(pre)):
            ch=pre[i]
            for word in strs[1:]:
                if i>=len(word) or word[i]!=ch:
                    return pre[:i]
        return pre

        