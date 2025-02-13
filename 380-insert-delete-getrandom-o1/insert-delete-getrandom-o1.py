class RandomizedSet:

    def __init__(self):
        self.map={}
        self.my_list=list()
        

    def insert(self, val: int) -> bool:
        # if not(val  in self.my_set):
        #     self.my_set[val]=len(self.my_list)
        #     self.my_list.append(val)
        #     return True
        # return False
        res= val not in self.map
        if  res:
            self.map[val]=len(self.my_list)
            self.my_list.append(val)
        return res
        
      
        

    def remove(self, val: int) -> bool:
        # if val in self.my_set:
        #     remove_index=self.my_set[val]
        #     del 
        #     self.my_list[self.my_list[-1]]=

        #     return True
        # else:
        #     return False
        res= val in self.map
        if res:
            idx=self.map[val]
            lastval=self.my_list[-1]
            self.my_list[idx]=lastval
            self.my_list.pop()
            self.map[lastval]=idx
            del self.map[val]
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.my_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()