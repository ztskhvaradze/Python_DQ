import random

# Task_1: create list of 100 random numbers from 0 to 1000
# using "random" library, generated random numbers from 0 to 1000 and using "for" listed 100 of those numbers
""" Following function accepts 3 numeric values, minimum, maximum and number (quantity) of "numbers" 
    and returns the random list of numbers based on the input values
"""
def rand_numbers_func(min_digit, max_digit, num_quantity):
    return [random.randint(min_digit,max_digit) for i in range(num_quantity)]

rand_numbers = rand_numbers_func(0,1000,100)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
""" Following function accepts list as argument and sorts the list by ascending order
"""
# Task_2: sort list from min to max (without using sort())
def sort_func(num_lst):
   # sorted_rand_numbers = num_lst #create new variable which holds rand_number values and will be sorted afterwards
    for i in range(len(num_lst)): # create the locator which will tell which position in the list we are currently
        for x in range(i + 1, len(num_lst)): # compare the value at the current position with all values after it in the list.
            if num_lst[i] > num_lst[x]: # If the value at the current position is greater than the value at a next position, than
                num_lst[i], num_lst[x] = num_lst[x], num_lst[i] # the two values are swapped using tuple unpacking
    return num_lst

sorted_rand_numbers = sort_func(rand_numbers)
print(sorted_rand_numbers)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
""" Following function accepts list as argument and returns average value for even and odd numbers
"""
# Task_3: calculate average for even and odd numbers
def average_func(input_lst):
    even_numbers = [] # create empty list which will hold even numbers
    odd_numbers = [] # create empty list which will hold odd numbers
    average_even = 0 # create variable with default value of 0 which will be changed afterwards and hold the average value for even nums
    average_odd = 0 # create variable with default value of 0 which will be changed afterwards and hold the average value for odd nums
    #next, iterating through generated numbers and if the remainder of the number equals to 0, than it is even num, if not than odd
    for i in input_lst: 
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    # Finally, changing the default value of variables with average value (rounded to 2 decimal points for better visual)
    average_even = sum(even_numbers) / len(even_numbers)
    average_odd = sum(odd_numbers) / len(odd_numbers)
    return "Average value for even numbers is: " + str(round(average_even, 2)) + "\nAverage value for odd numbers is: " + str(round(average_odd, 2))

print(average_func(sorted_rand_numbers))
