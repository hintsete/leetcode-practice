class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
        values=[]
        for val in count.values():
            values.append(val)
        values.sort(reverse=True)
        processed=set()
        res=[]
        for i in range(len(values)):
            for key,val in count.items():
                if val==values[i] and key not in processed:
                    res.append(key*val)
                    print(res)
                    processed.add(key)
        return "".join(res)
                    




        