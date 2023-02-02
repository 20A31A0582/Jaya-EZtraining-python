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
