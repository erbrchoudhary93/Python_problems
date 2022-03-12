# Python list of strings

groceryList = ["Rice","Wheat","Barley"]
print(groceryList)

# . Python list of numbers

myNumbers = [1,5,9,16,28]
print(myNumbers)

#   Python list with duplicate values------------------------------------------------------

myNumbers = [1,5,5,9,9,9,16,28]
print(myNumbers)

#  Python list that contains different data type values---------------------------------------

heterogeneousList = ["Python",123,24.5,True,35,"a"]
print(heterogeneousList)

# Finding the length of a list in Python-------------------------------------------------------

ProgrammingList = ["CSharp","Python","PHP","R"]
print(len(ProgrammingList))

# Finding the index of items in a Python list------------------------------------------------

fruits = ["apple","banana","mango"]
bananaIndex = fruits.index("banana")
mangoIndex = fruits.index("mango")
print(bananaIndex)
print(mangoIndex)

pythonList = ["p","y","t","h","o","n"]

# to get the 1st item
print(pythonList[0])

#to get the 4th item
print(pythonList[3])

# Negative indexing to get last item
print(pythonList[-1])

# To get second last item
print(pythonList[-2])

#  Slicing of lists in Python --------------------------------------------------------

myList = ['p','y','t','h','o','n','i','s','t','a']

# elements from 5 to 8
print(myList[4:8])

# from 1st element to 4th element
print(myList[:4])

# from 8th element to last element
print(myList[7:])

# from 1st to last elements
print(myList[:])

# negative slicing
print(myList[-1:-9])

print(myList[-5:])

print(myList[:-4])

# Adding items to a list using insert() and append() in Python-----------------------------------------------

numbers = [10,20,30,40,50,60]

numbers.append(70)
print(numbers)

#  Merging two lists using extend method in Python-----------------------------------------------------------

list1 = ["Apple","Orange","Mango"]
list2 = ["Grape","Strawberry"]

l1= list1.extend(list2)
print(list1)
print(l1)  # none output in l1

# Removing items from a list using pop() in Python----------------------------------------

x = [23,45,67,89,34,12]

# removing the last element
x.pop()  # remove last item
print(x)

# removing the 0th index element
x.pop(0)  # remove 1st item
print(x)

#  Removing items from a list using remove() in Python--------------------------------------

dryFruits = ["Cashew nuts","Dates","Almonds","Raisins"]

dryFruits.remove("Raisins")
print(dryFruits)

#  Remove all the elements from a list in Python------------------------------------------------------

dryFruits = ["Cashew nuts","Dates","Almonds","Raisins"]

dryFruits.clear()
print(dryFruits)

#  Creating a copy of a list in Python------------------------------------------------------------

dryFruits = ["Cashew nuts","Dates","Almonds","Raisins"]

d = dryFruits.copy()
print(d)

#  Finding the number of times an item is present in a list------------------------------------------------

myList = [1,2,2,3,3,3,4,4,4,4]

count1 = myList.count(4)
count2 = myList.count(3)
print(count1)
print(count2)

# Reversing a list in Python---------------------------------------------------------------------------------

myList = ["Pen","Pencil","Book"]

myList.reverse()
print(myList)

#  Sorting a list in Python-----------------------------------------------------------------------

myList = ["Pen","Pencil","Book","Eraser"]

myList.sort()
print(myList)

# Deleting items in a list using del keyword--------------------------------------------------------------

colorList = ["Red","Blue","Green","Yellow","Orange","Purple"]

# deleting an item
del colorList[2]
print(colorList)

# deleting multiple items
del colorList[1:3]
print(colorList)

# deleting the entire list
del colorList
#print(colorList)  # can't print becouse list deleted

# Nested list in Python------------------------------------------------------------------------------------

nestedList = ["Apple",["Ball",1,2.5],['a',128]]  # list inside list

print(nestedList)
print(nestedList[0])
print(nestedList[1])
print(nestedList[2])

# Creating a list using the list() constructor---------------------------------------------------------------

myList = list(("Mac","Windows","Linux"))
print(myList)

# Checking whether an item exists in a list or not---------------------------------------------------------------

myList = list(("Mac","Windows","Linux"))

if "Mac" in myList:
    print("Yes")
else:
    print("No")

if "Linux" not in myList:
    print("Yes")
else:
    print("No")


#   Concatenating lists in Python--------------------------------------------------------------

myList1 = ["Mac","Windows","Linux"]
myList2 = ["Book","Pencil","Pen"]

combinedList = myList1 + myList2

print(combinedList)

#  Repeating a list in Python---------------------------------------------------------------

myList1 = ["Mac","Windows"]

combinedList = myList1 * 3
print(combinedList)

# Python list of numbers of the power of 2

myList = [2**x for x in range(10)]
print(myList)