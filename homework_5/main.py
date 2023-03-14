# Import the functions that handle user input and file input
from classes.actions import take_from_text_file, take_from_user_input

# Import the Records class
from classes.records import Records


# Ask the user to select a source for records
source = input("Please select a source for records. 'Text file' or 'User input': ")

if source.lower() == 'text file':
    # If the user selects "Text file", call the take_from_text_file function and capture the result
    take_from_text_file()

    records = Records('file.txt')

    # Call the count_words method on the records instance to get the word counts
    word_counts = records.count_words()

    # Call the count_letters method on the records instance to get the letter counts
    letter_counts = records.count_letters()

    # Write the results to CSV files
    records.write_results_to_csv()

elif source.lower() == 'user input':
    # If the user selects "User input", call the take_from_user_input function
    take_from_user_input()
    # Create an instance of the Records class, passing in the name of the text file as an argument
    records = Records('file.txt')

    # Call the count_words method on the records instance to get the word counts
    word_counts = records.count_words()

    # Call the count_letters method on the records instance to get the letter counts
    letter_counts = records.count_letters()

    # Write the results to CSV files
    records.write_results_to_csv()
