# ----------*CHALLENGE 092* ----------* 
# Create two arrays (one containing three numbers that the user enters and one containing a set of five random numbers). 
# Join these two arrays together into one large array. Sort this large array and display it so that each number appears
# on a separate line.

from array import *


array_1 = array('i',[5,26,15,21,11])
array_2 = array('i', [])

for every_number in range (1,4):
    newNumber = int(input("Enter a number: "))
    array_2.append(newNumber)

new_array = array_1 + array_2
sorted_array = sorted(new_array)

for every_item in sorted_array:
    print(every_item)