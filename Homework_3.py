import re

task = """
homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# I tryied to do this task by braking down the process into small pieces.

# part_1: first of all, before any transformations, I found number of whitespaces
no_whitespaces = len(re.findall(r'\s', task))  # "\s" represents a whitespace character including spaces, tabs, and newlines.
print("Number of whitespaces in the text = ", no_whitespaces)

# part_2: get all the characters lowercase
task = task.lower()

# part_3: split the sentence based on whitespaces and get the list of the words
list = re.split(r'\s+', task)

# part_4: find the "iz" and replace it with "is"
for i in list: # Loop through the elements in the list
    if re.match(r'^i.*?z$', i): # Check if the element matches the pattern '^i.*?z$'
        index = list.index(i) # When match is found, find the index of the match in the list
        list[index] = i.replace('z', 's') # Replace 'z' with 's' in the match

# part_5: Join the list and get the whole sentence + add capitalization of the first symbol after period.

task = ' '.join(list) # Join the elements in the list with a space character as the separator
task = task.strip() # Remove whitespaces from the string
sentences = task.split(". ") # Split the sentence into separate sentences based on the period
capitalized = [sentence.capitalize() for sentence in sentences] # Capitalize the first letter of each word in each sentence
task = ". ".join(capitalized) # Join the sentences back together

# Print the final result
print(task)
