#n Python, we use dictionaries to store data in the form of key-value pairs. You can find the value
# from the dictionary by searching for the key.

# Example of dictionanry
alphabetDict = {
    "a":"apple",
    "b" :"ball",
    "c":"cat",
    "d":"doll"
}
print(alphabetDict)

# python do not allow duplicate key
num_dict = {
    1:11,2:22,2:22,3:33,3:33,3:33
}

print(num_dict)

# Python allow duplicate valus

num_dict = {
    1:11,2:22,3:22,4:33,5:33,6:33
}

print(num_dict)

# clearing the key and value of dicitionary
print(f"before clering dictionary : {num_dict} ")

num_dict.clear()
print(f"After clearing dictionary : {num_dict}")

# Getting value by key
programmingLangauges = {1:"Python",2:"CSharp",3:"PHP"}

#if value exists, it returns the value
print(programmingLangauges.get(1))
print(alphabetDict.get("b"))

#if value doesn't exist, it returns None
print(programmingLangauges.get(4))

# Getting the keys and values from a dictionary using items() method

print(programmingLangauges.items())

# Getting the keys from a dictionary using keys() method

print(programmingLangauges.keys())

# Getting the keys from a dictionary using values() method

print(programmingLangauges.values())

# Popping out items from a Python dictionary using pop() method
#The method pop(key) removes the key from the dictionary and returns its value.
print(programmingLangauges.pop(2))
print(programmingLangauges.pop(1))
print(programmingLangauges.pop(3))
print(programmingLangauges)

#Converting two lists to a dictionary in Python

letters = ['a','b','c','d']
numbers = [1,2,3,4]

myDict1 = dict(zip(letters,numbers))
myDict2 = dict(zip(numbers,letters))
print(myDict1)
print(myDict2)

# Deleting elements from a dictionary using del

programmingLangauges = {1:"Python",2:"CSharp",3:"PHP"}

if 3 in programmingLangauges:
     del programmingLangauges[3]

print(programmingLangauges)

#  Sorting elements in a Python dictionary

programmingLangauges = {1:"Python",5:"Java",3:"PHP"}

for key in sorted(programmingLangauges):
    print(key,programmingLangauges[key])

#  Finding the sum of all values in a Python dictionary

myDict = {"n1":100,"n2":200,"n3":300}
print(sum(myDict.values()))

#  Example of the fromkeys() method in Python
# In Python, the fromkeys() method returns a dictionary with the specified keys and the specified value.

p = ("p1","p2","p3")
q = 5
r=3

myDict = dict.fromkeys(p,r)
print(myDict)

# Finding the min and max of values in a Python dictionary

myDict = {"n1":100,"n2":200,"n3":300}

print(max(myDict.values()))
print(min(myDict.values()))

#  Python dictionary of square of numbers

squareDict ={}

for i in range(1,10):
    squareDict[i] = i**2
print(squareDict)