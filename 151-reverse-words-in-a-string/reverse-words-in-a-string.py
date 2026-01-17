class Solution:
    def reverseWords(self, s: str) -> str:
        # s=s.strip()
        # print(s)
        s_lst=s.split()
        print(s_lst)
        s_lst=s_lst[::-1]
        print(s_lst)
        return " ".join(s_lst)
     
