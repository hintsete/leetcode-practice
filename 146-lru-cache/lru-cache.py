# class ListNode:
#     def __init__(self,key,next,val):


# class LRUCache:

#     def __init__(self, capacity: int):
        

#     def get(self, key: int) -> int:
        

#     def put(self, key: int, value: int) -> None:
        


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)

class LRUCache:
    def __init__(self, capacity: int):
        self.recency = []
        self.elements = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.elements:
            return -1
        
        self.recency.remove(key)
        self.recency.append(key)
          
        return self.elements[key]

    def put(self, key: int, value: int) -> None:
        if key in self.elements:
            self.elements[key] = value
            self.recency.remove(key)
            
        else:
            if self.capacity == len(self.elements):
                to_be_deleted = self.recency[0]
                self.recency.pop(0)
                self.elements.pop(to_be_deleted)
            
            self.elements[key] = value
             
        self.recency.append(key)
        