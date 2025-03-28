class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def div(s):
            if len(s)<=1:
                return ""

            seen=set(s)
            for idx, char in enumerate(s):
                opposite_chr=char.swapcase()
                if opposite_chr not in seen:
                    left=div(s[:idx])
                    right=div(s[idx+1:])
                    if len(left)>=len(right):
                        return left

                    else:
                        return right
            return s

               
        return div(s)


        # print(ord("a"))
        # print(ord("A"))
        # print(ord("b"))
        # print(ord("B"))
#         if len(s)==1 or len(s)==0:
#             return ""
#         l=0
#         max_len=float(-inf)
#         r=len(nums)
#         for r in range(len(nums)):
            
# aaA
