class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        count=0
        left=0
        right=0
        while left< len(seats) and right< len(students):
            count+=abs(seats[left]-students[right])
            left+=1
            right+=1
        return count

        