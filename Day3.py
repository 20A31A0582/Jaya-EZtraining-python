#LIST-ordedred,duplicates allowed 
l=[2,3,"jay",89.567,-2]
print(l)
print(l[0])
print(l[2:3])
print(l[-3:-2])
print(l[::-1])
print(l[:3])
type(l)
'''remove=removes item with specified value'''
print(l.remove("jay"))
'''count=counts no of times each item occured'''
print(l.count(2))
'''pop=removes item with specified index'''
print(l.pop(3))
'''appends an item to list'''
print(l.append(23))
'''sorts given list in ascending order'''
print(l.sort())
'''copies'''
l1=l.copy()
print(l1)
'''extend=append a list to another list'''
print(l.extend(l1))
'''Reverse=reverses entire list'''
print(l.reverse())
'''insert=inserts elements at specified position'''
print(l.insert(0,"hai"))





#create list with 10 items and print one by one
l=[1,2,3,4,5,6]
for i in l:
    print(i)

#create a list with 5 float numbers find and dispaly sum and avg of list

l=[1.0,2.0,3.0,4.0]
print(sum(l)/len(l))


#after creating list with 6 elements from the user extract only even numbers and print
l=list(map(int,input("Enter:").split()))
for i in l:
    if i%2==0:
        print(i)




'''get list from user and print product if prod<750 else print sum'''
'''
l=list(map(int,input().split()))
p=1
for i in l:
    p=p*i
if p<750:
    print(p)
else:
    print(sum(l))


#list comprehensions
print([x for x in "Jayasri"])
l1=[2**x for x in range(1,10)]
print(l1)
l2=[a for a in range(100,201,20)]
print(l2)
l3=[1,2,3,4,5,6,7,8,9,0]
l4=[x for x in l3 if x<5]
print(l4)'''


#SET-unordered-unindexed-no duplicates-mutable
s={1,1,12,3,4,5,6,7,8}
print(type(s))
print(s)
#add =one eleemnt
s.add(55)
print(s)
#update=to add more tahn one element
s.update((90,0,11))
print(s)
#discard=to remove element
s.discard(55)  #no remove method
print(s)
s1={1,2,3,4,5,6,7}
s2={1,2,8,9,0,10}
#union ==combines both sets
print(s1|s2) #or s1.union(s2)
#intersection-returns elements which are common in both sets
print(s1&s2) #s1.imntersection(s2)
print(s1-s2)
print(s2-s1)
#superset=set must have all elemnts of other set
p={1,2,3}
q={1,2,3,4,5}
print(q.issuperset(p))

#symmetricdiff

s4={1,2,3,4,5,10}
s5={4,1,9,2,10}
print(s4^s5)
#or
print(s4.symmetric_difference(s5))


#TUPLE-INDEX,COUNT ,ORDERED,UNCHANGABLE --methods==count and index

t=(4,5,6,7,8,4,4)
print(type(t))
print(t.count(4))
print(t.index(4))#returns  index where the element first occurered



#DICTIONARY:It contains elements with two units key and values .Keys must be unique

d={1:'one',2:'two'}
print(d)
print(d.keys())
print(d.values())
print(d.items())
print(d.get(1))

li=['hi','hello']
print(dict.fromkeys(li))
d.setdefault(3,'three')
d.setdefault(4)
d.update({5:'five'})
d.pop(2)
d.popitem()
print(d)
