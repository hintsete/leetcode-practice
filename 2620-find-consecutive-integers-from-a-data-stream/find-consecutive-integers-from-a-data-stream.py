class DataStream:

    def __init__(self, value: int, k: int):
        self.stream=deque()
        self.k=k
        self.value=value
        self.count=0
        

    def consec(self, num: int) -> bool:

        self.stream.append(num)
        if num==self.value:
            self.count+=1
        # else:
        #     self.count=0
        if len(self.stream)>self.k:
            left=self.stream.popleft()
            if left==self.value:
                self.count-=1
        return self.count==self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)