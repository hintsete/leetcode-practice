class Solution:
    def judgeCircle(self, moves: str) -> bool:
        direction={"L":-1,"D":-1,"U":1,"R":1}
        x=0
        y=0
        for ch in moves:
            if ch=="L" or ch=="R":
                x+=direction[ch]
            elif ch=="D" or ch=="U":
                y+=direction[ch]
        return x==0 and y==0
        
       
        