#Lambda function -Is called as an anonymous function.When we want to use function concept without using function name their we apply concept of lambda function
"""L=[1,2,3]
r=map(lambda x:x+x,L)
res=map(lambda n:pow(n,2),L)
print(list(r))
print(list(res))
name="jay"
(lambda name:print(name))(name)
(lambda name:name)
print(name)
"""
# after creating a list with even numbers within the range 1,2,....,15 now apply lamda function and create a new list which should have square roots of the elements
"""import math
l=[x for x in range(1,15) if x%2==0]
res=map(lambda n:pow(n,1/2),l) 
print(list(res))
res=map(lambda n:math.sqrt(n),l) 
print(list(res))
"""

# Four pillars of oops :Abstraction,Encapsulation,Inheritance,Polymorphism
#Abstraction:Hiding the implementation part and showing what is required for the users  ex:exe file
#we can make class or method as abstract ,opposite to abstract is concrete
import abc
class abstractdemo(abc.ABC):
    @abc.abstractmethod #called decorator to make the method(function) abstract one
    def display(self):
        None
    @abc.abstractmethod
    def show(self):
        None
#changing abstract to concrete
class demo(abstractdemo):
    def display(self):
        print("Abstraction method")
    def show(self):
        print("2nd function")
obj=demo()
obj.display()
obj.show()



#Encapsulation:Binding data and function in to single unity
#variable scope or data security
#public----one class info can be accessed by any other class
#private---can used where it is declared/no in inherited class
#protected---can be accessed only where it got declared...which ever class inherited from this class there also we can use

"""Inheritance :Base class or main class ex:Parent  .....derived class:Child
Types
1.single inheritance
2.multiple  inheritance
3.multilevel  inheritance
4.heirarchial  inheritance
5.hybrid  inheritance
"""
class parent:
    def display(self):
        print("Parent class")
class child(parent):
    def show(self):
        print("child class")
c=child()
c.display()
c.show()
#Single inheritance
class A:
    n=10
class B(A):
    def calc(self):
        c=self.n+50
        print(c)
obj=B()
obj.calc()

#multiple inheritance
class mom:
    def mdisplay(self):
        print("Mom class")
class dad:
    def ddisplay(self):
        print("Dad class")
class child(mom,dad)     :
        def cdisplay(self):
            print("Child calss")
c1=child()
c1.cdisplay()
c1.ddisplay()
c1.mdisplay()



n=int(input())
t=n
while(t>1):
    s=0
    while(t>0):
        k=t%10
        s=s+k**2
        t=t//10
    t=s
if t==1:
    print("Happy Number")
else:
    print("NO")
