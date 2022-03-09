# Example 1
# n=1
# while n<5:
#     print("Hello Ziddi Enginer")
#     n=n+1
#     if n==3:
#         break

# Example 2
# n=1
# while n<5:
#     if n==2:  # only this condition continue
#         n=n+1
#         continue
#     print("Hello Ziddi Enginer")
#     n = n + 1

#example 3
# z=0
# while z <3:
#     if z==0:
#         print("Z is  : ",z)
#         z=+1
#     elif z==1:
#         print("Z is  : ", z)
#         z+=1
#     else:
#         print("Z is  : ", z)
#         z+=1

# Adding element to the list

# list1=[]
# i=0
# while len(list1)<5:
#     list1.append(i)
#     i += 1
# print(list1)
#
# # Print number series
# a=10
# while a<=100:
#     print(a , end=" " "\n")
#     a+=20

# Printing item using tuple
# mytuple = (10,20,30,40,50,60,70,80)
# i=0
# while i<len(mytuple):
#     print(mytuple[i] , end=" ")
#     i+=1

#sum of number in list

# list2=[]
# s=0
# while s<100:
#     s += 1
#     list2.append(s)
#
# print(list2)
#
# i=0
# sum=0
# while i <len(list2):
#     sum += list2[i]
#     i+=1
# print(sum)
#
# # sum of factriol of 1 to 20
# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n*(fact(n-1))
# list3=[]
# g=1
# h=fact(g)
# while g<20:
#     g+=1
#     list3.append(fact(g))
# print(list3)
# i=0
# sum=0
# while i<len(list3):
#     sum=sum+list3[i]
#     i+=1
# print(sum)
#
# # Poping out item from list
# fruitsList = ["Mango","Apple","Orange","Guava"]
# while fruitsList:
#     print(fruitsList.pop()) #The pop() will be accepting only one argument for its execution
# print(fruitsList)
#
# #Printing all later except
#
# i=0
# word = "Hello"
# #print except e and o
# while i<len(word):
#     if word[i]=='e' or word[i]=='o':
#         i+=1
#         continue
#     print("Returned latter :  " ,word[i])
#     i+=1

# Taking input

# n=int(input("Enter a number : "))
#
# while n!=0:
#
#     n= int(input("Enter 0 to quit "))

# Convert decimal to binary
# num= int(input("Enter a number : "))
# b=0
# p=1
# n=num
# while n>0:
#     rem=n%2  # give reminder
#     b+= rem*p
#     p=p*10
#     n=n//2  # floor division
# print("Binary Value : ",b)
# print(1%2)

#Average of 5 number
# p = 5
# sum = 0
# count = 0
#
# while p > 0:
#     count += 1
#     f = int(input("Enter the number :  "))
#     sum += f
#     p -= 1

# average = sum / count
# print("Average of given Numbers:", average)

# printing the squre
# n = 1
#
# while n <= 5:
#     squareNum = n**2 #squre of number
#     print(n,squareNum)
#     n += 1
#
# # Finding the number of multiple
# n = int(input("Enter an integer: "))
#
# i = 1
# while i <= 10:
#     mul = i*n
#     i += 1
#     print(mul)

#reversing the number
# n = int(input("Enter a number: "))
# rev = 0
#
# while n != 0:
#     r = n % 10
#     rev = rev * 10 + r
#     n = n // 10
#
# print("Reversed number:", rev)

# sum of even numbers
i = 0
sum = 0
n = int(input("Enter the number n: "))

while i <= n:
    if i % 2 == 0:
        sum += i
    i += 1

print("Sum of even numbers till n:", sum)

# Finding the factroil
n = int(input("Enter the number: "))
f =n
r = 1

while f != 0 :
    r *= f
    f -= 1
print("Factorial of",n,"is:",r)