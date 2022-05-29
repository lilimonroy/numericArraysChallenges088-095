# ----------*CHALLENGE 088 ----------* 
# Ask the user for a list of five integers. Store them in an array. 
# Sort the list and display it in reverse order.

from array import *
from audioop import reverse

integers = array ('i', [])
newnumber = int(input("Enter five integer numbers.\nEnter the first number: "))
integers.append(newnumber)
for i in range(0,4):
    newnumber = int(input("Enter the next number: "))
    integers.append(newnumber)
integers = sorted(integers)
integers.reverse()
print(integers)