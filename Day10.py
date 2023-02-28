
"""#STACK
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
"""

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
