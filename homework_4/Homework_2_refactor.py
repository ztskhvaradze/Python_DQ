import string 
import random

"""
Task_1. create a list of random numbers of dicts (from 2 to 10)
dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}] 
"""

# define function to generate random integer values
def random_func(min_value, max_value):
    return random.randint(min_value, max_value)

# define variables which will hold the minum and maximum number for integers to be present in dictionaries
min_int_num = int(input('enter minum interger num: '))
max_int_num = int(input('enter maximum interger num: '))

# define the main function which accepts minimum and maximum number of dictioneries to generate
def rand_dict_func(min_dict_num, max_dict_num):
    my_lst_of_dicts = [] # create empty list which will contain the list of dict.
    for _ in range(random_func(min_dict_num, max_dict_num)): # loop 2 to 10 times to generate 2 to 10 dictionaries
        random_dict = {} # create empty dict.
        for x in range(3): # this range is used to define how many key-value pairs will be in the dict
            key = random.choice(string.ascii_lowercase) # generate random keys in lowercase
            value = random_func(min_int_num, max_int_num)
            random_dict[key] = value # assign for every random "key" a random "value"
        my_lst_of_dicts.append(random_dict) # finally append the created dict to the variable which holds all the dicts.
    return my_lst_of_dicts

my_lst_of_dicts = rand_dict_func(2,10)
print(my_lst_of_dicts)

"""
Task_2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
"""
def dict_merge(lst_of_dicts):
    result = {} # create empty dict.
    for i, d in enumerate(my_lst_of_dicts): # loop through the list of dictionaries
        for key, value in d.items(): # loop through the key-value pairs in each dictionary
            if key in result: # check if the key is already in the result dictionary
                if value > result[key]: # if the value is greater than the current value,
                    del result[key] # remove the key from the result dictionary
                    new_key = f"{key}_{i+1}" # rename the key with the dict number (+1 used because numbering starts from 0)
                    result[new_key] = value # set the new value for the key
            else:
                result[key] = value # if the key is not in the result dictionary, add it
    return result
print(dict_merge(my_lst_of_dicts))