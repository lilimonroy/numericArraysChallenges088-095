# ----------*CHALLENGE 093* ----------* 
# Ask the user to enter five numbers. Sort them into order and present them to the user.
# Ask them to select one of the numbers. Remove it from the original array and save it in a new array.

from array import *

array_number = array('i',[])
new_array = array('i', [])

for new_item in range(1,6):
    numbers = int(input("Enter a number: "))
    array_number.append(numbers)

sorted_array = sorted(array_number)
print(sorted_array)
remove_item = int(input("Which item do you wanna remove?: "))

sorted_array.remove(remove_item)

print("The new array is:")
print(sorted_array)