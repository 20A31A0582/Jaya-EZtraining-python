import random as r
x="I love my pet"
print(r.sample(x,6)) #returns out as list

#diff out every time
a=[1,2,3,4,5,6]
r.shuffle(a)
print(a)


a=[1,2,3,4,5,6]
print(r.choice(a))

b='welcome back'
print(r.choice(b))

 
a=r.random()
print(a)#prints any random number

print(r.randint(20,30))

a=[10,20,30,40,50]
print(r.choices(a,k=10))

s="Hello This is jay"
print(r.choices(s,k=3))

print(r.uniform(5,10))


print(dir(r))#used to identify diff functions available in particular module

import calendar
print(calendar.calendar(2023))
print(calendar.month(2023,2))

print("set fist day of week:")
calendar.setfirstweekday(calendar.FRIDAY)
print(calendar.month(2021,12))


#prg-dispaly date month

import datetime
a=datetime.datetime.now()
print(a)

sv=a.strftime("%y")
fv=a.strftime("%Y")
print("Short:",sv)
print("Long:",fv)


#predefined,builtin,system defined - random,count,ceil,floor,print,.......

#functions
Classifications-Predefined functions
            -User defined functions
for code reusability we use functions,,,write once.. include inside func ,and can call it where ever we need it
TYPES:
1.fun without argum without return value
2.fun without argum with return value
3.fun with argum with return value
4.fun with argum without return value


def sample():
    print("Great day")
    print("HAppy time")
sample()
print("Today")
sample()

#fun without argum without return value
def multi():
    n1=int(input("Enter:"))
    n2=int(input("Enter:"))
    n3=int(input("Enter:"))
    p=n1*n2*n3
    print(p)
multi()

#fun without argum with return value
def multi():
    n1=int(input("Enter:"))
    n2=int(input("Enter:"))
    n3=int(input("Enter:"))
    p=n1*n2*n3
    return p
r=multi()
print(r)'''

#fun with argum without return value
def multi(a,b,c):
    p=a*b*c
    print(p)
multi(1,2,3)

#or to take input from user

def multi(a,b,c):
    p=a*b*c
    print(p)
n1=int(input("Enter:"))
n2=int(input("Enter:"))
n3=int(input("Enter:"))
multi(n1,n2,n3)
#fun with argum with return value
def multi(a,b,c):
    p=a*b*c
    return p
n1=int(input("Enter:"))
n2=int(input("Enter:"))
n3=int(input("Enter:"))
r=multi(n1,n2,n3)
print(r)


#find factors of given number using type 2

def fac():
    n=int(input("Enter n:"))
    c=0
    for i in range(1,n):
        if n%i==0:
            c=c+1
    return c
r=fac()
print(r)
    
#print multiplication table of given number using fun type 4
def mul(a):
    for i in range(1,11):
        p=a*i
        print(a,"*",i,"=",p)
n=int(input("Enter:"))
mul(n)
    
#findout sum of digits of given number usinf func type 4

#Recursive function -A function whihch calls itself

'''def display():
    n=int(input("Enter:"))
    if n==1:
        display()
    else:
        print("Over")
display()

#factorial using recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=int(input("Enter a number:"))
r=fact(n)
print(r)'''

n=int(input("Enter:"))
a=0
b=1
s=0
c=1
while(c<=n):
    print(s,end="")
    c=c+1
    a=b
    b=s
    s=a+b

