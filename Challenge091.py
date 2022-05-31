# ----------*CHALLENGE 091* ----------* 
# Create an array which contains five numbers (two of which should be repeated). 
# Display the whole array to the user. Ask the user to enter one of the numbers from the array and
# then display a message saying how many times that number

from array import *

numbers = array('i',[15,11,26,15,21])

print(numbers)

check_number = int(input("Enter a number shown in the array: "))

if check_number in numbers:
    count = numbers.count(check_number)
    print("The number of repetiion of",check_number,"is",count)
else:
    print("The number doesn't exist in the array")