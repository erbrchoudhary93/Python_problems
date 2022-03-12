# Example of using if-else ladder in Python------------------------------------------------------------

z = 1000

if z == 100:
    print('z is 100')
elif z == 200:
    print('z is 200')
elif z == 300:
    print('z is 300')
elif z == 1000:
    print('z is 1000')
else:
    print('z is unknown')


# Python if-else statements using relational operators-------------------------------------------------

m = 25
n = 25
if m > n:
    print('m is greater than n')
elif m == n:
    print('m is equal to n')
else:
    print('m is less than n')


# Python if-else statements using True or False-----------------------------------------------------------

if False:
    print("Statement is True")
else:
    print("Statement is False")

# Python nested if-else statements----------------------------------------------------------------------

z = 10

if z<0:
    print("z is less than 0")
else:
    if z < 5:
        print("z is less than 5")
    else:
        print("z is greater than 5")


count = 200

if count < 400:
    print('The count is below 400')
    if count < 300:
        print('The count is below 300')
    else:
        print('The count is less than 400 and greater than or equal to 300')

# Python if-else statements using membership operators (in, not in)------------------------------------------

letter = "t"

if letter in 'Python':
    print("Yes")
else:
  print("No")

if letter not in 'Java':
    print("Yes")
else:
  print("No")

# Python shorthand if-else statements (if-else in one line)------------------------------------------

x = 55
y = 110
print("X") if x > y else print("Y")

s = 200
r = 400

print("s is not equal to r") if s!=r else print("s is equal to r")

# Python if-else statements using and operator--------------------------------------------------------

s=3000
t=1000

if s>t and t%2 == 0:
    print('Both conditions are true')

# Python if-else statements using or operator---------------------------------------------------------------

x = 200
y = 1000

if ((x < y) or (y%11 == 0)):
    print("Atleast one condition is true")

# Using pass inside if-else statements in Python----------------------------------------------------------

x = 100
y = 10

if x > y:
    pass    #pass the condition

# Python if-else statements using lambda function------------------------------------------------------------

h = lambda k : k**5 if k % 5 == 0 else k**7
print(h(5))
print(h(7))

# Python if-else statements using input taken from the user----------------------------------------------

print("Enter a number: ")
number = int(input())

if number < 20:
    print("The number is less than 20")
elif number == 20:
    print("The number is equal to 20")
else:
    print("The number is greater than 20")

#  Python program to check if the number is divisible by 5 or not----------------------------------------------

d = int(input("Enter a number: "))

if (d%5 == 0):
    print("Number is divisible by 5")
else:
    print("Number is not divisible by 5")

#  Python program to check if the number is odd or even-------------------------------------------------------------

number = int(input("Enter a number: "))

if number%2 == 0:
    print("Given number is Even")
else:
    print("Given number is Odd")

# Python program to check if the number is divisible by both 5 and 7 or not-------------------------------------------

number = int(input("Enter a number: "))

if (number%5 == 0) and (number%7 == 0):
    print("Number is divisible by both 5 and 7")
else:
    print("Number is not divisible by both 5 and 7")