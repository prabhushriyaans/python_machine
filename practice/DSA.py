class Stack:
    def __init__(self):
        self.S=[]
    def push(self,data):
        self.S.append(data)
    def pop(self):
        if len(self.S)==0 or self.S is None:
            print("Stack is Empty.")
        else:
            return self.S.pop()
    def top(self):
        if len(self.S)==0 or self.S is None:
            print("Stack is Empty.")
        else:
            return self.S[-1]
    def is_empty(self):
        return len(self.S)==0

class Queue:
    def __init__(self):
        self.Q=[]
    def enqueue(self,data):
        self.Q.append(data)
    def dqueue(self):
        if len(self.Q)==0 or self.Q is None:
            print("The Queue is Empty.")
        else:
            return self.Q.pop(0)
    def front(self):
        if len(self.Q)==0 or self.Q is None:
            print("The Queue is Empty.")
        else:
            return self.Q[0]
    def end(self):
        if len(self.Q)==0 or self.Q is None:
            print("The Queue is Empty.")
        else:
            return self.Q[-1]
    def bdqueue(self):
        if len(self.Q)==0 or self.Q is None:
            print("The Queue is Empty.")
        else:
            return self.Q.pop()
    def is_empty(self):
        return len(self.Q) == 0
    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node

    def delete(self,data):
        flag=False
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        current=self.head
        while current.next is not None:
            if current.next.data==data:
                current.next=current.next.next
                flag=True
                return
            current=current.next
        if not  flag:
            print(f"Element {data} not present.")

    def traverse(self):
        current=self.head
        while current is not None:
            print(current.data,end="--")
            current=current.next