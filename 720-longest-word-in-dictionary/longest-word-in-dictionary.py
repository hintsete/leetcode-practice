class TrieNode:
    def __init__(self):
        self.children=[None for _ in range(26)]
        self.is_end=False


    
    
class Solution:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for ch in word:
            idx=ord(ch)-ord('a')
            if node.children[idx] is None:
                node.children[idx]=TrieNode()

            node=node.children[idx]

        node.is_end=True
    def search(self,word):
        node=self.root
        for ch in word:
            idx=ord(ch)-ord('a')
            if node.children[idx] is None :
                return False

            node=node.children[idx]
            if not node.is_end:
                return False

        return True


        
    def longestWord(self, words: List[str]) -> str:
        if not words:
            return ""
        for word in words:
            self.insert(word)
        sorted_words=sorted(words,key=lambda x:(-len(x),x))
        for word in sorted_words:
            if self.search(word):
                return word

        return ""
       
        
        