class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=["a","e","i","o","u","A","E","I","O","U"]
        left=0
        my_list=[]
        for ch in s:
            my_list.append(ch)
        print(my_list)
        right=len(my_list)-1
        while left<right:
            if my_list[left] in vowels and my_list[right] in vowels:
                my_list[left],my_list[right]=my_list[right],my_list[left]
                left+=1
                right-=1
            elif my_list[left] in vowels and my_list[right] not in vowels:
                right-=1
            elif my_list[left] not in vowels and my_list[right] in vowels:
                left+=1
            else:
                left+=1
                right-=1
        return "".join(my_list)


        