 
"""l=[2,3,"jay",89.567,-2]
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
"""




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
