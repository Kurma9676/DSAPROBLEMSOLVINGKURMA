#linked list
# A linked list is a type of linear data structure similar to arrays. It is a collection of nodes that are linked with each other.
# A node contains two things first is data and second is a link that connects it with another node. Below is an example of a linked list with four nodes and each node contains character data and a link to another node.
# Our first node is where head points and we can access all the elements of the linked list using the head.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insertAtbegin(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head=newnode
    def insertAtend(self,data):
        newnode=Node(data)
        current=self.head
        while(current.next!=None):
            current=current.next
            if(current.next==None):
                current.next=newnode
                newnode.next=None
    def deleteAtbegin(self):
        self.head=self.head.next
    def deleteAtend(self):
        current=self.head
        while(current.next!=None and current.next.next!=None):
            current=current.next
        current.next=None 
    # Method to add a node at any index
# Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            return

        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")
    def display(self):
        current=self.head
        while(current):
            print(current.data,end="->")
            current=current.next
s1=Linkedlist()
s1.insertAtbegin(1)
s1.insertAtbegin(2)
s1.insertAtbegin(3)
s1.insertAtbegin(4)
s1.insertAtend(0)
s1.insertAtend(1)
s1.insertAtend(2)
s1.deleteAtbegin()
s1.deleteAtend()
s1.deleteAtend()
s1.deleteAtend()
s1.insertAtIndex(5,2)
s1.insertAtIndex(6,4)
s1.display()
        
        
    
