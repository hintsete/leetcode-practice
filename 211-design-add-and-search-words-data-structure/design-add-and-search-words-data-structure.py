class TrieNode:
    def __init__(self):
        self.children =[None for _ in range(26)]
        self.is_end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            idx=ord(ch)-ord('a')
            if node.children[idx] is None:
                node.children[idx]=TrieNode()

            node=node.children[idx]
        node.is_end=True
        

    def search(self, word: str) -> bool:
        def dfs(node,idx):
            if idx==len(word):
                return node.is_end

            ch=word[idx]
            if ch==".":
                for child in node.children:
                    if child and dfs(child,idx+1):
                        return True
                return False
            else:
                i=ord(ch)-ord('a')
                if node.children[i] is None:
                    return False
                # node=node.children[idx]
                return dfs(node.children[i], idx+1)
        return dfs(self.root,0)

                
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)