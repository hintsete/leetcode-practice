class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled=[""]*len(s)
        for i,j in zip(indices,s):
            shuffled[i]+=j
        return "".join(shuffled)

        