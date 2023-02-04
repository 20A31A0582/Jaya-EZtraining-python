#Exception Handling
'''When there is exception the developer doesnot want interuption or disturbance in the program flow
to achieve this we are using exception handling
TYPES:
compile time error...Syntax error
Logical..Wrong output'''


a=int(input("a:"))
b=int(input("b:"))
try:
    print(a/b)
except Exception as e:
    print("Divison By zero error",e)
finally:
    print("...")

l=list(map(int,input().split()))
try:
    print(l[7])
except IndexError as e:
    print(e)
print("exit")

#handling multiple errors
a=int(input("Enter a:"))
try:
    b=int(input("Enter b:"))
    print(a/b)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except Eception as e:
    print(e)
finally:
    print("exit")

x=int(input("Enter a:"))
if x%2!=0:
    raise Exception("X  should be even")
else:
    print(x,"is Even")'''

#OOPS-OBJECT ORIENTED PROGRAMMING STRUCTURE
'''iTS AN EFFICIENT CONCEPT USED IN ALL OBJECT ORIENTED PROGRAMMING LANGUAGES LIKE JAVA AND PYTHON . FOR MULTIPLE REASONS WE USE OOPS CONCEPTS For example code reusability,data security,hiding data
CLASS-Its a blue pirnt example laptops,birds
OBJECT-Its a thing created based on class #note:1 class can have multiple objects
example:
class is birds ..Objects are aprrot,peacock,crow
class is laptop..objects are lenovo,hp,dell

class computer:
    def config(self):
        print("Yes")
lenova=computer() #objectname=classname()
lenova.config()#accessing methods inside class

dell=computer()
dell.config()
