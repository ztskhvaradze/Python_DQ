import random

# Task_1: create list of 100 random numbers from 0 to 1000
# using "random" library, generated random numbers from 0 to 1000 and using "for" listed 100 of those numbers
rand_numbers = [random.randint(0,1000) for i in range(100)]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Task_2: sort list from min to max (without using sort())
sorted_rand_numbers = rand_numbers #create new variable which holds rand_number values and will be sorted afterwards
for i in range(len(sorted_rand_numbers)): # create the locator which will tell which position in the list we are currently
    for x in range(i + 1, len(sorted_rand_numbers)): # compare the value at the current position with all values after it in the list.
        if sorted_rand_numbers[i] > sorted_rand_numbers[x]: # If the value at the current position is greater than the value at a next position, than
            sorted_rand_numbers[i], sorted_rand_numbers[x] = sorted_rand_numbers[x], sorted_rand_numbers[i] # the two values are swapped using tuple unpacking

print(sorted_rand_numbers)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Task_3: calculate average for even and odd numbers
even_numbers = [] # create empty list which will hold even numbers
odd_numbers = [] # create empty list which will hold odd numbers
average_even = 0 # create variable with default value of 0 which will be changed afterwards and hold the average value for even nums
average_odd = 0 # create variable with default value of 0 which will be changed afterwards and hold the average value for odd nums
#next, iterating through generated numbers and if the remainder of the number equals to 0, than it is even num, if not than odd
for i in sorted_rand_numbers: 
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
# Finally, changing the default value of variables with average value (rounded to 2 decimal points for better visual)
average_even = sum(even_numbers) / len(even_numbers)
average_odd = sum(odd_numbers) / len(odd_numbers)

print("average value for even numbers is", round(average_even, 2))
print("average value for odd numbers is", round(average_odd, 2))
