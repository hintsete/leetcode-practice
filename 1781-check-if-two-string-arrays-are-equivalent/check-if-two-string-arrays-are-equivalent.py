class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        res1=""
        res2=""
        for ch in word1:
            res1+=ch

        for ch in word2:
            res2+= ch
        
        return res1==res2

        

        