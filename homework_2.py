import random
import string

"""
Task_1. create a list of random numbers of dicts (from 2 to 10)
dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}] 
"""
random_numbers = []  # create empty list which will contain the list of dict.
for _ in range(random.randint(2, 10)):  # loop 2 to 10 times to generate 2 to 10 dictionaries
    random_dict = {}  # create empty dict.
    for x in range(3):  # this range is used to define how many key-value pairs will be in the dict
        key = random.choice(string.ascii_lowercase)  # generate random keys in lowercase
        value = random.randint(0, 100)  # generate random integer values
        random_dict[key] = value  # assign for every random "key" a random "value"
    random_numbers.append(random_dict)  # finally append the created dict to the variable which holds all the dicts.

print(random_numbers)

"""
Task_2. get previously generated list of dicts and create one common dict:

if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
"""
result = {}  # create empty dict.
for i, d in enumerate(random_numbers):  # loop through the list of dictionaries
    for key, value in d.items():  # loop through the key-value pairs in each dictionary
        if key in result:  # check if the key is already in the result dictionary
            if value > result[key]:  # if the value is greater than the current value,
                del result[key]  # remove the key from the result dictionary
                # rename the key with the dict number (+1 used because numbering starts from 0)
                new_key = f"{key}_{i + 1}"
                result[new_key] = value  # set the new value for the key
        else:
            result[key] = value  # if the key is not in the result dictionary, add it
print(result)
