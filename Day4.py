d={n:n*n for n in range(1,5)}
print(d)

'comprehensions'
#calculating product price for 5 units
old={'rice':60,'dal':120,'oil':390}
new={product:price*5 for(product,price) in old.items()}
print(new)

#with checks
real={'sam':24,'angel':18,'kumar':35}
now={name:age for (name,age) in real.items() if age>20}
print(now)

#create a list with 8 customer names display a dictionary which has customers names along with discounts for them from a particular shop
import random
l=['A','B','C','D','E','F','G','H']
print({l[i]:random.randint(1,50) for i in range(len(l))})

#uismg zip
stu=['sam','bannu','sonu','jay']
marks=[100,91,89,76]
print({a:b for (a,b) in zip(stu,marks) if b>=90})

#STRINGS

s="Hai!This is \"jaya\""
print(s.lower()) #s.casefold()
print(s.islower())
print(s.capitalize())
print(s.replace('h','H'))
print(s.count('a'))# print(s.count('a',5,len(s))) starts from 5 th pos and checks till end of string
print(s.find('j'))
print(s.rfind('a',0,len(s)))#from rev first occ or last occcurence
s1="I\'m a Student"
print(s1.upper())
print(s*3)
print(s1+s)
print(max('a','b','c'))
print(min('a','b','c'))
print(s1.strip())#removes sapce at beg and end
a="hajdjnoij327389&jkj"
print(a.split("&")) #splits at specified pos and ret out as list  ['hajdjnoij327389', 'jkj']
print(a.center(60,'$'))# width,filled character

#mutable--list,set,tuple
#immutable--int,float,string,bool,tuple


#get one string as input along with a character find out and display whether the particular characater is in string or not
s=list(map(str,input("Enter:").split(" ")))
if s[1] in s[0]:
    print("Yes")
else:
    print("NO")
#another process
s=input("Enter:")
c=input("Enter:")
f=0
for i in s:
    if i==c:
        f=1
        #break
    else:
        f=0
if(f==1):
    print('Yes')
else:
    print('No')
#check palindrome or not

s=input("Enter:") 
r=s[::-1]
if s==r:
    print("Yes.It is a palindrome")
else:
    print("No")
#check given string contains space or not i yes count no of spaces and print
s=input("Enter:")
c=0
for i in s:
    if i==" ":
        c=c+1
print("{} occurs {} times".format('space',c))
#create a list with vowels  get string as input count vowels from string
v=['a','e','i','o','u','A','E','I','O','U']
c=0
s=input("Enter:")
for i in s:
    if i in v:
        c=c+1
print(c)
#math
import math
print("ceil value:",math.ceil(12.34))
print("floor value",math.floor(12.34))
print("factorial:",math.factorial(3))
print("Power:",math.pow(2,5))
print("Modulator:",math.fmod(20,3))
a,b=divmod(10,3)
print(a,b)
