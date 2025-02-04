class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count=Counter(s)
        my_value=set()
        for value in count.values():
            my_value.add(value)
        if len(my_value)>1:
            return False
        else:
            return True
        
        