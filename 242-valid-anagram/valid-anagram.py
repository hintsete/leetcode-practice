class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=list(s)
        print(s)
        s_map=Counter(s)
        print(s_map)

        t=list(t)
        print(t)
        t_map=Counter(t)
        print(t_map)

        if len(t)!=len(s):
            return False

        for ch in t:
            if ch in s_map:
                t_map[ch]-=1
                s_map[ch]-=1
            if t_map[ch]==0:
                del t_map[ch]
            if s_map[ch]==0:
                del s_map[ch]
        return len(t_map)==0 and len(s_map)==0
        