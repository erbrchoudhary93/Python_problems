# finding power of number
def power(base,exp):
    if exp==1:
        return base
    else:
        return base *power(base,(exp-1))

a=int(input("Enter the base value  :  "))
b=int(input("Enter the exponent value : "))
print(f" Result is  : ",power(a,b))

# Combination --  n^C^r= n!/(r!(n-r)!)  Here, n is the total number of items and r is the number of combinations needed
def fact(a):
    if a==1:
        return a
    else:
        return a*fact(a-1)

def combination(n,r):
    return fact(n)/(fact(r)*fact(n-r))

n= int(input("Entr n : "))
r= int(input("Entr r : "))

if r>n:
    print("Enter the valid value or r ")
else:
    print("Combination is : ",combination(n,r))

