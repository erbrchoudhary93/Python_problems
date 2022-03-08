# recursive function --In programming, recursion is a technique using a function or an algorithm
#                   that calls itself one or more times until a particular condition is met.
#Finding factroial number
def fact(n):
    if n==1:
        return n
    else:
        return n*(fact(n-1))

c =int(input("Enter the number : "))

if c<0:
    print("Negative number is not allowed")

elif c==0:
    print("Factroil is  :  1")

else:
    print("Factroil is  :  ",fact(c))


# fibonacci of any number--0 1 1 2 3 5 8 13 21
def feb(n):
    if n<=1:
        return n
    else:
        return feb(n-1)+feb(n-2)

count = int(input("Enter the limit: "))
if count <=0:
    print("Enter value grater then 1")
else:
    for i in range(count):
        print(feb(i) , end=" ")