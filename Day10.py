
#STACK
#USING LiST
stack=[]
def push():
    e=int(input("Enter element:"))
    stack.append(e)
    print(stack)
def popele():
    if not stack:
        print("Stack is empty")
    else:
        ele=stack.pop()
        print("Removed element:",ele)
        print(stack)
while True:
    print("Select operation 1.push 2.pop 3.quit")
    choice=int(input("Enter choice:"))
    if choice==1:
        push()
    elif choice==2:
        popele()
    else:
        break


#Stack using linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
     def __init__(self):
        self.head=None
     def push(self,data):
         newnode=Node(data)
         if self.head==None:
             self.head=newnode
         else:
             newnode.next=self.head
             self.head=newnode
     def display(self):
         temp=self.head
         if temp==None:
             print("Underflow")
         else:
             while temp!=None:
                 print(temp.data,end=" ")
                 temp=temp.next
                 if(temp!=None):
                     print("->",end=" ")
     def pop(self):
         temp=self.head
         if temp==None:
             print("Underflow")
         else:
             self.head=self.head.next
             temp.next=None
                     
s=stack()
s.push(11)
s.push(22)
s.push(33)
s.push(44)
s.display()
s.pop()
s.pop()
print("\n")
s.display()



s=input()
st=[]
balanced=True
for i in s:
    if(i=='{' or i=='[' or i=='('):
        st.append(i)
    elif(i=='}'):
        if(len(st) and st.pop()!='{'):
            balanced=False
            break
    elif(i==']'):
        if(len(st) and st.pop()!='['):
            balanced=False
            break
    elif(i==')'):
        if(len(st) and st.pop()!='('):
            balanced=False
            break
    else:
        balanced=False
        break
if(balanced==False or len(st)):
    print("Not balanced")
else:
    print("Balanced")
 

#Queue using list
queue=[]
def enqueue():
    e=int(input("Enter element:"))
    queue.append(e)
    print(queue)
def dequeue():
    if not queue:
        print("Stack is empty")
    else:
        ele=queue.pop(0)
        print("Removed element:",ele)
        print(queue)
def display():
    print(queue)
while True:
    print("Select operation 1.push 2.pop 3.display")
    choice=int(input("Enter choice:"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    else:
        break


print("queue using queue module")
import queue
L=queue.Queue(maxsize=5)
L.put(10)
L.put(20)
print(L.get())
print(L.get())

print("stack using queue module")
from queue import LifoQueue
s=LifoQueue()
print(s.qsize())
s.put('a')
s.put('b')
s.put('c')
print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())
print(s.empty())



class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
 
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
 
    def dequeue(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
 
a= Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'enqueue':
        a.enqueue(int(do[1]))
    elif operation == 'dequeue':
        dequeued = a.dequeue()
        if dequeued is None:
            print('Queue is empty.')
        else:
            print('Dequeued element: ', int(dequeued))
    elif operation == 'quit':
        break

        
#removing duplicates from linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
    def get_prev_node(self, ref_node):
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
 
    def remove(self, node):
        prev_node = self.get_prev_node(node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
 
    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
 
 
def remove_duplicates(llist):
    current1 = llist.head
    while current1:
        data = current1.data
        current2 = current1.next
        while current2:
            if current2.data == data:
                llist.remove(current2)
            current2 = current2.next
        current1 = current1.next
 
 
a_llist = LinkedList()
 
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_llist.append(int(data))
 
remove_duplicates(a_llist)
 
print('The list with duplicates removed: ')
a_llist.display()
