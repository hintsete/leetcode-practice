class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bit=bin(num2).count("1")
        print(set_bit)
        res=0
        
        for i in range(31,-1,-1):
            if num1>>i & 1:
                res|=1<<i
                set_bit-=1

            if set_bit==0:
                break

        if set_bit>0:
            for i in range(32):
                if res>>i &1:
                    continue
                res|=1<<i
                set_bit-=1
                if set_bit==0:
                    break

        return res
            

    