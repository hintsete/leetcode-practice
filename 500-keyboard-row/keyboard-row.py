class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output=[]
        first_row=set("qwertyuiop")
        second_row=set("asdfghjkl")
        third_row=set("zxcvbnm")

        for word in words:
            new_word=set(word.lower())
            if new_word.issubset(first_row) or new_word.issubset(second_row) or new_word.issubset(third_row):
                output.append(word)
            
           
         

        return output
        