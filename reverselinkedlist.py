class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insertdata(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=newnode      
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            current=self.head
            while current is not None:
                print(current.data,end=" ")
                current=current.next
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next   # 1. Save the next node
            current.next = prev        # 2. Reverse the link
            prev = current             # 3. Move prev forward
            current = next_node        # 4. Move current forward
        self.head = prev 
o=Linkedlist()
o.insertdata(1)
o.insertdata(2)
o.insertdata(3)
o.insertdata(4)
o.display()
o.reverse()
o.display()
