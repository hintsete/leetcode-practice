class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly=[1]
        i2=i3=i5=0
        while len(ugly)<n:
            n2,n3,n5=ugly[i2] *2, ugly[i3] *3,ugly[i5] *5
            new_ugly=min(n2,n3,n5)
            ugly.append(new_ugly)

            if new_ugly==n2:
                i2+=1
            if new_ugly==n3:
                i3+=1
            if new_ugly==n5:
                i5+=1

        return ugly[-1]

        