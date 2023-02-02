#swap with temp variable
a=int(input())
b=int(input())
print("Before Swapping:")
print(a,b)
t=a
a=b
b=t
Print("After Swapping:")
print(a,b)

#swap without temp
a=int(input())
b=int(input())
print("Before Swapping:")
print(a,b)
a,b=b,a
Print("After Swapping:")
print(a,b)

#print perimeter and area of rectangle
a=int(input())
b=int(input())
print("Perimeter:")
print(2*(a+b))
print("Area:")
print(a*b)

#number game using random
import random
n=random.randrange(1,50)
guess=int(input("Enter a number:"))
while n!=guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again:"))
    elif guess > n:
        print("too high")
        guess =int(input("Enter number again"))
    else:
      break
print("You guessed it right!!")
               

