from DSA import LKL
linked_list=LKL()
v=10
for i in range(12):
    linked_list.node(v)
    v+=10
linked_list.traverse()
linked_list.insert_before(30,25)
linked_list.traverse()
linked_list.insert_after(30,35)
linked_list.traverse()
linked_list.insert_before(100,90)
linked_list.traverse()
linked_list.delete(30)
linked_list.traverse()
linked_list.delete(100)
linked_list.traverse()
linked_list.truncate()
linked_list.traverse()