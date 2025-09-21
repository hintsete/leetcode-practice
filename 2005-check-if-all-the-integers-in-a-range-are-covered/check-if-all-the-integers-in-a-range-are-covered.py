class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        _set=set()
        interval=set()
        for i in range(left,right+1):
            interval.add(i)

        for item in ranges:
            start=item[0]
            end=item[-1]
            for i in range(start,end+1):
                _set.add(i)
        print(_set)
        print(interval)
        # return left in _set and right in _set
        return interval.issubset(_set)