# ----------*CHALLENGE 089 ----------* 
# Create an array which will store a list of integers.
# Generate five random numbers and store them in the array. 
# Display the array (showing each item on a separate line).

import random
from array import *

integers = array('i',[])

for every_num in range(0,6):
    num_random = random.randint(1,100)
    integers.append(num_random)

integers = sorted(integers)
#print(integers)
for every_int in integers:
    print(every_int)
