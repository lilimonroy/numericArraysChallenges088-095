# ----------*CHALLENGE 089 ----------* 
# Ask the user to enter numbers. If they enter a number between 10 and 20, save it in the array,
# otherwise display the message “Outside the range”. Once five numbers have been successfully added, display the message “Thank
# you” and display the array with each item shown on a separate line.


from array import *

numbers = array('i', [])

for every_number in range(0,5):   
    is_ok = False
    while is_ok == False:
        newnumber = int(input("Enter a number: "))
        if newnumber >= 10 and newnumber <=20:
            numbers.append(newnumber)
            is_ok = True
        else:
            print("Outside the range.")
            is_ok = False
            
print("Thank you!")
for every_item in numbers:
    print(every_item)