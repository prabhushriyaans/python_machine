from Node import Node
class LinkedList:
    def __init__(self,sz):
        self.size=sz
        self.head=None
    def add(self,data):
        new_node=Node(data=data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node
    def traverse(self):
        pointer=self.head
        while pointer is not None:
            print(pointer.data,end="--")
            pointer=pointer.next
    def delete(self,data):
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return 
        current=self.head
        while current.next is not None:
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next
l1=LinkedList(10)
l1.add(5)
l1.add(4)
l1.add(3)
l1.add(2)
l1.add(1)
l1.delete(1)
l1.traverse()