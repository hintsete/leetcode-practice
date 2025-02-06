class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=defaultdict(list)
        for s in strs:
            s_sorted="".join(sorted(s))
            anagram[s_sorted].append(s)

        output=[]
        for val in anagram.values():
            output.append(val)
        return output
        
        





