class Node:
    def __init__(self,val):
        self.val=val
        self.next=None



class MyLinkedList:
    

    def __init__(self):
        self.dummy=Node(-1)
        # self.tail=None
        # self.length=0
        
        

    def get(self, index: int) -> int:
        current=self.dummy.next
        for _ in range(index):
            if current is None:
                return -1
            current=current.next
        return -1 if current is None else current.val
        

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        new_node.next=self.dummy.next
        self.dummy.next=new_node
        

    def addAtTail(self, val: int) -> None:
        current=self.dummy
        while current.next is not None:
            current=current.next
        current.next=Node(val)
        


    def addAtIndex(self, index: int, val: int) -> None:
        current=self.dummy
        for _ in range(index):
            if current is None:
                return
            current=current.next
         
        if current is not None:    
            new_node=Node(val)
            new_node.next=current.next
            current.next=new_node
       
            
        

    def deleteAtIndex(self, index: int) -> None:
        current=self.dummy
        for _ in range(index):
            if current is None:
                return
            current=current.next

            
        if current is not None and current.next is not None:
            current.next=current.next.next
      
        
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)