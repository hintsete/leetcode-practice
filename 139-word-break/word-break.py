class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

        
    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=TrieNode()

            node=node.children[ch]

        node.is_end=True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie=Trie()
        for word in wordDict:
            trie.insert(word)
        n=len(s)
        dp=[False] *(n+1)
        dp[0]=True
        for i in range(n):
            if not dp[i]:
                continue

            node=trie.root
            for j in range(i,n):
                ch=s[j]
                if ch not in node.children:
                    break
                node=node.children[ch]
                if node.is_end:
                    dp[j+1]=True

        return dp[n]


        
        