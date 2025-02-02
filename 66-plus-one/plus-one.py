class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      str_digits=list(map(str,digits))
      joined="".join(str_digits)
      num=int(joined)
      num+=1
      return [int(digit) for digit in str(num)]
