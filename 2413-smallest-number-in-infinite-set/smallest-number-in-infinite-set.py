class SmallestInfiniteSet:

    def __init__(self):
        self.container=set()
        self.next_smallest=1
        # self.container=[]
        

    def popSmallest(self) -> int:
        if self.container:
            val=min(self.container)
            self.container.remove(val)
            return val

        else:
            val=self.next_smallest
            self.next_smallest+=1
            return val
           

    def addBack(self, num: int) -> None:
        if num<self.next_smallest and num not in self.container:
            self.container.add(num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)