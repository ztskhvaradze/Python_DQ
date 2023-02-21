import re

task = """
homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""

# I tryied to do this task by braking down the process into small pieces.

# part_1: first of all, before any transformations, I found number of whitespaces
# function to find whitespaces in the given text
def count_whitespaces(some_text):
    nof_whitespaces = len(re.findall(r'\s', some_text))  # "\s" represents a whitespace character including spaces, tabs, and newlines.
    return f"Number of whitespaces in the text = {nof_whitespaces}"

print(count_whitespaces(task))

# part_2: get all the characters lowercase
task = task.lower()

# part_3: split the sentence based on whitespaces and get the my_list of the words
# function to split text based on whitespaces
def split_text(some_text):
    return re.split(r'\s+', some_text)

my_list = split_text(task) #create list which holds splited words
#print(my_list)

# part_4: find the "iz" and replace it with "is"
for i in my_list: # Loop through the elements in the my_list
    if re.match(r'^i.*?z$', i): # Check if the element matches the pattern '^i.*?z$'
        index = my_list.index(i) # When match is found, find the index of the match in the list
        my_list[index] = i.replace('z', 's') # Replace 'z' with 's' in the match

# part_5: Join the my_list and get the whole sentence + add capitalization of the first symbol after period.
# function to capitalize the first symbol after period given the list of words
def text_capitalize(some_lst_of_words):
  task = ' '.join(some_lst_of_words) # Join the elements in the my_list with a space character as the separator
  task = task.strip() # Remove whitespaces from the string
  sentences = task.split(". ") # Split the sentence into separate sentences based on the period
  capitalized = [sentence.capitalize() for sentence in sentences] # Capitalize the first letter of each word in each sentence
  task = ". ".join(capitalized) # Join the sentences back together
  return task

task = text_capitalize(my_list)
print(task)

# part_6: print last word of every sentence
def last_words_func(some_text):
  sentences = some_text.split(". ") # split sentence based on full stop 
  last_word_sentence = [] # make empty list to hold last words
  for sentence in sentences: # Loop through each sentence 
      words = sentence.split()  # Split the sentence into separate words
      last_word = words[-1] # Get the last word of the sentence
      last_word_sentence.append(last_word) # Add the last word to the created list
  last_word_sentence = " ".join(last_word_sentence) # Join last words together based on whitespace in order to form sentence
  return f"Sentence created from last words is: {last_word_sentence}"

print(last_words_func(task))
