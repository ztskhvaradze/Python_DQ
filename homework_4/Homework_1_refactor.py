import random

# Task_1: create list of 100 random numbers from 0 to 1000
# using "random" library, generated random numbers from 0 to 1000 and using "for" listed 100 of those numbers
""" Following function accepts 3 numeric values, minimum, maximum and number (quantity) of "numbers" 
    and returns the random list of numbers based on the input values
"""
def generate_rand_numbers (min_digit, max_digit, num_quantity):
    return [random.randint(min_digit,max_digit) for i in range(num_quantity)]

rand_numbers = generate_rand_numbers(0,1000,100)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
""" Following function accepts list as argument and sorts the list by ascending order
"""
# Task_2: sort list from min to max (without using sort())
def sort_list(input_list):
   # sorted_rand_numbers = num_lst #create new variable which holds rand_number values and will be sorted afterwards
    for i in range(len(input_list)): # create the locator which will tell which position in the list we are currently
        for x in range(i + 1, len(input_list)): # compare the value at the current position with all values after it in the list.
            if input_list[i] > input_list[x]: # If the value at the current position is greater than the value at a next position, than
                input_list[i], input_list[x] = input_list[x], input_list[i] # the two values are swapped using tuple unpacking
    return input_list

sorted_rand_numbers = sort_list(rand_numbers)
print(sorted_rand_numbers)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------#
""" Following function accepts list as argument and returns average value for even and odd numbers
"""
# Task_3: calculate average for even and odd numbers
def get_average_even_odd(input_lst):
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
    return round(average_even, 2), round(average_odd, 2)

print(get_average_even_odd(sorted_rand_numbers))
