# ----------*CHALLENGE 094* ----------* 
# Display an array of five numbers. Ask the user to select one of the numbers.
# Once they have selected a number, display the position of that item in the array. 
# If they enter something that is not in the array, ask them to try again until they select a relevant item.


from array import *

array_numbers = array('i', [5,26,15,21,11])
print(array_numbers)

number_selected = int(input("Select a number of the array: "))

if number_selected in array_numbers:
    index_selected = array_numbers.index(number_selected)
    print("The index of the number",number_selected,"is",index_selected)
else:
    print("The number selected doesn't exist.")