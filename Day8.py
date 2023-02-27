def happy(n):
    s=r=0
    while(n>=0):
        for i in range(0,len(str(n))+1):
            r=n%10
            s=s+r**2
            n=n//10
        return s
n=int(input("Enter:"))
res=n
while(res!=1 and res!=4):
    res=happy(res)
if res==1:
    print("Happy Number")
else:
    print("NO")

#protected

class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("Encap function-accessing protected")
        print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)


#private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("Encap function")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)

#Polymorphism:One item or same item used for different purposes
#Types:1.Overloading--->a.Operator over loading  b.Method Overloading
#       2.Overriding

#Method overloading
class moverload:
    def display(self,a=None,b=None):
        print(a,b)
obj=moverload()
print("without arguments")
obj.display()
print("With two arguments")
obj.display(2,3)
print("With one argument")
obj.display(1)

#If a method is defective or cannot be used inside derived class it will take it from its base class or parents class


#Polymorphism
class vijayawada():
    def placename(self):
        print("Vijayawada place name is KLU")
    def student(self):
        print("Yes-Viajyawada")
    def which_year(self):
        print("3 rd Year")
class hyd():
    def placename(self):
        print("Hyd place name is HYD-KLU")
    def student(self):
        print("Yes-Hyd")
    def which_year(self):
        print("3 rd Year-HYD")
obj_vij=vijayawada()
obj_hyd=hyd()
for details in (obj_vij,obj_hyd):
    details.placename()
    details.student()


#DAtastructutres -->Linear:arrays(static),linkedlist(Dyanamic),stacks(dyn),queues(Dyn)
#                 -->Nonlinear:Trees,graphs,tables,sets
#Linked list real timeexample:Train
#as the name says list of items which rae linkled with one another is called as linkedlist
#types:Singly linkd list,doubly linkedlist,circular linkedlist
#CREATING LINKEDLIST
#STEP1:CREATE THE NODE
#STEP2:PARTITION THE NODE WITH 2 SEGMENTS DATA AND NONE
#STEP3:ADD VALUE INTO THE BLANK NODE
#STEP4:MARK THE NODE AS HEAD
#STEP5:CREATE THE NEXT NODE BY FOLLOWING THE ABOVE STEPS
#ESTABLISH LINK BETWEEN FIRST NODE AND SECOND NODE
##DISPLAYING LINKEDLIST
#tRAVERSAL IS REQUIRED FROM FIRST NODE TILL TAIL NODE INORDER TO DISPLAY EXISTING LINKEDLIST
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("W")
obj.head=n
n1=Node("I")
obj.head.next=n1
n2=Node("N")
n1.next=n2
n3=Node("N")
n2.next=n3
n4=Node("E")
n3.next=n4
n5=Node("R")
n4.next=n5
 
obj.display()       

#Operations
#insertion:Beg end pos
#Deletion
#Search

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_Atend(self,data):
        nb=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=nb
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("W")
obj.head=n
n1=Node("I")
obj.head.next=n1
n2=Node("N")
n1.next=n2
n3=Node("N")
n2.next=n3
n4=Node("E")
n3.next=n4
n5=Node("R")
n4.next=n5
obj.insert_beginning("Saranya")
obj.insert_Atend("Hai")
obj.display()        

#INsert at pos

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(self):
        self.head=None
    def insertatpos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
obj=singlelinkedlist()
n=Node("W")
obj.head=n
n1=Node("I")
obj.head.next=n1
n2=Node("N")
n1.next=n2
n3=Node("N")
n2.next=n3
n4=Node("E")
n3.next=n4
n5=Node("R")
n4.next=n5
obj.insertatpos(3,100)
obj.display()        


#insertion at runtime
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class singlelinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def addNode(self, data):
        if self.tail is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_Atend(self,data):
        nb=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=nb
    def insertatpos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("Linkedlist is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->")
                temp=temp.next
obj=singlelinkedlist()
n = int(input('enter the number of elements in linked list : '))
for i in range(n):
    data=input("Enter data:")
    obj.addNode(data)
obj.insert_beginning("saranya")
obj.insert_Atend("Hai")
obj.insertatpos(3,100)
obj.display()     
















































 



























































                                                                                                           
