# What is a Doubly Linked List?
# Doubly Linked List (DLL) is a special type of linked list in which each node contains a pointer to the previous node as well as the next node of the linked list.
# In a Doubly Linked List
# we can traverse in forward and backward direction using the next and previous pointer respectively.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DoubleLinkedlist:
    def __init__(self):
        self.head=None
    def insertD(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            self.head.prev=newnode
            newnode.next=self.head
            self.head=newnode
    def insertAtEnd(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newnode
            newnode.prev=current
    def deleteAtbegin(self):
         if self.head is None:
            print("List is empty")
            return
         if self.head.next is None:
            self.head = None  # Only one node, just delete it
         else:
            self.head = self.head.next
            self.head.prev = None
    def deleteAtend(self):
         if self.head is None:
            print("List is empty")
            return
         if self.head.next is None:
            self.head = None  # Only one node, just delete it
         else:
             current=self.head
             while(current.next):
                 current=current.next
             current.prev.next=None
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> " if temp.next else "")
            temp = temp.next
        print()
d=DoubleLinkedlist()
while(True):
    print("1.insertAtbegin 2.insertAtend 3.DeleteAtbegin 4.DeleteAtend 5.Display ")
    ch=int(input("Enter your choice:"))
    if ch==1:
        n=int(input("enter a value"))
        d.insertD(n)
        print("value inserted at beggining")
    elif ch==2:
        n=int(input("enter a value"))
        d.insertAtEnd(n)
        print("value inserted at ending")
    elif ch==3:
        d.deleteAtbegin()
        print("value delted from beggining")
    elif ch==4:
        d.deleteAtend()
        print("value deleted from the end of linked list")
    elif ch==5:
        print("the linked list is:")
        d.display()
    else:
        break
        
    
        
