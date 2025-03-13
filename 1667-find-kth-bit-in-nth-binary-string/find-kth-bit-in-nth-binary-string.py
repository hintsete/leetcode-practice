class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def inverse(s):
            inversed=""
            for ch in s:
                if ch=="0":
                    inversed+="1"
                else:
                    inversed+="0"
            return inversed[::-1]
        def binary_str(n):
            if n==1:
                return "0"
            prev=binary_str(n-1)
            binary=prev+"1"+inverse(prev)
            return binary
        print(binary_str(n))
            
        return binary_str(n)[k-1]

        

        