class Solution:
    def validPalindrome(self, s: str) -> bool:
        # after deleting the element check if the len of the array is odd or even 
        left=0
        right=len(s)-1
        left_mismatch=0
        right_mismatch=0
        if s==s[::-1]:
            return True 
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                left_mismatch=left
                right_mismatch=right
                break
        return ((s[:left_mismatch]+s[left_mismatch+1:])==(s[:left_mismatch]+s[left_mismatch+1:])[::-1] or (s[:right_mismatch]+s[right_mismatch+1:])==(s[:right_mismatch]+s[right_mismatch+1:])[::-1])


        