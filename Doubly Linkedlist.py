class Node:
    def __init__(self,data):
        self.Pref=None
        self.data=data
        self.Nref=None
class LinkedList:
    def __init__(self):
        self.head=None
    def Forword(self):
        if self.head is None :
            print("Linkedlist is empty.....")
            return 
        n=self.head
        while (n!=None):
            print(n.data,"--forword-->",end="")
            n=n.Nref
    def Backword(self):
        if self.head is None :
            print("Linkedlist is empty.....")
            return 
        n=self.head
        while (n.Nref != None):
            n=n.Nref
        while (n!=None):
            print(n.data,'<--Backword---',end='')
            n=n.Pref
        
    def Add_beging(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            new_node=Node(data)
            new_node.Nref=self.head
            self.head.Pref=new_node
            self.head=new_node
            
    def  Add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        n=self.head
        while n.Nref is not None:
            n=n.Nref
        new_node.Pref=n
        n.Nref=new_node
    
    def Add_After(self,data,target):
        if self.head is None:
            print("LinkedList is empty you can't Added the node")
            return
        n=self.head
        while (n != None):
            if (n.data==target):
                break
            n=n.Nref
        if (n is None):
            print("given node is not present ... try next time.")
        else:
            new_node=Node(data)
            new_node.Nref=n.Nref
            new_node.Pref=n
            if n.Nref is not None:
                n.Nref.Pref=new_node
            n.Nref=new_node
    def Add_Befor(self,data,target):
        if self.head is None:
            print("LinkedList is empty you can't Added the node")
            return
        n=self.head
        while (n is not  None):
            if (n.data == target):
                break
            n=n.Nref
        if (n is None):
            print("given node is not present ... try next time.")
        else:
            new_node=Node(data)
            new_node.Nref=n
            new_node.Pref=n.Pref
            if (n.Pref is not None):
                n.Pref.Nref=new_node
            else:
                self.head=new_node
            n.Pref=new_node
            
    def Delete_begining(self):
        if self.head is None:
            print("linkedlist is empty you can't delete")
        else:
            if ((self.head.Nref == None) and (self.head.Pref ==None)):
                self.head = None
                print("First node deleted successfully ....")
                return
            self.head.Nref.Pref=None
            self.head=self.head.Nref
            print("First node deleted successfully ....")
    def Delete_end(self):
        n=self.head
        while (n.Nref != None):
            n=n.Nref
        if ((self.head.Nref == None) and (self.head.Pref ==None)):
                self.head = None
                print("last node delete successfully ....")
                return
        n.Pref.Nref=None
        print("last node deleted successfully ....")
        
    def Delete_by_value(self,x):
        if (self.head.data == x):
            if ((self.head.Nref == None) and (self.head.Pref ==None)):
                self.head = None
                print("First node deleted successfully ....")
                return
            self.head=self.head.Nref
            self.head.Pref=None
            return
        n=self.head
        while (n != None):
            if (n.data == x):
                break
            n=n.Nref
        if (n is None):
            print('Node not founds') 
        elif(n.Nref == None):
            n.Pref.Nref=None
        else:
            n.Pref.Nref=n.Nref
            n.Nref.Pref=n.Pref
             
        
        
L=LinkedList()
L.Add_beging(10)
L.Add_beging(20)
L.Add_beging(30)
L.Add_beging(40)
L.Delete_end()
L.Delete_by_value(40)
L.Forword()
print()
print()
L.Backword()           