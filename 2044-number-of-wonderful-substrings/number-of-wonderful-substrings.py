class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count=0
        prefix_count=defaultdict(int)
        prefix_count[0]=1
        state=0
        visited=set()
        for ch in word:
            idx=ord(ch)-ord("a")
            state^=1<<idx
            count+=prefix_count[state]
            for i in range(10):
                new_state= state ^ 1<<i
                count+=prefix_count[new_state]
            prefix_count[state]+=1

        return count