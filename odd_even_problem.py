import math
import os
import random
import re
import sys


# if __name__ == '__main__':
#
#     n = int(input().strip())
#     check = {True: "Not Weird", False: "Weird"}
#
#     print(check[
#           n % 2 == 0 and (
#                   n in range(2, 6) or
#                   n > 20)
#           ])
# n= int(input().strip())
# if n%2==0:
#     if n in range(2,5):
#         print("Not Werid")
#     elif n in range(6,20):
#         print("Werid")
#     else:
#         print("Not Werid")
# else:
#     print("Weried")
#

x ="     My name is ziddi engineer       "
print(x.strip())  # it is used to remove space at the begining and end
number = input("Enter a number :  ")
x = int(number)%2
if x == 0:
    print(" The number is Even ")
else:
    print(" The number is odd ")