from classes.actions import take_from_text_file, take_from_user_input

source = input("Please select a source for records. 'Text file' or 'User input': ")

if source.lower() == 'text file':
    take_from_text_file()
elif source.lower() == 'user input':
    take_from_user_input()
