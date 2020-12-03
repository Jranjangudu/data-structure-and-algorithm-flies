class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def Add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def disp(self):
        if self.head is None:
            print("linked list if empty")
            return
        n=self.head
        while (n != None):
            print(n.data,end="----->")
            n=n.ref

            
    
l=LinkedList()
l.Add_begin(10)
l.Add_begin(20)
l.Add_begin(50)
l.Add_begin(110)
l.disp()