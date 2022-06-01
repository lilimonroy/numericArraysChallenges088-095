# ----------*CHALLENGE 095* ----------* 
# Create an array of five numbers between 10 and 100 which each have two decimal places. 
# Ask the user to enter a whole number between 2 and 5. If they enter something outside of that
# range, display a suitable error message and ask them to try again until they
# enter a valid amount. Divide each of the numbers in the array by the number the user entered 
# and display the answers shown to two decimal places.

from array import *

numbers = array('f', [94.19, 70.21, 49.26, 15.11, 5.5])
is_ok = False

while is_ok == False:
    whole_number = float(input("Enter a number between 2 and 5: "))
    if whole_number>=2 and whole_number<=5:
        for each_item in numbers:
            newnumber= round(each_item/whole_number,2)
            print("The division of",each_item,"divided by",whole_number,"is",newnumber)
            is_ok = True
    else:
        print("Your answer is incorrect. Try again")
        is_ok = False