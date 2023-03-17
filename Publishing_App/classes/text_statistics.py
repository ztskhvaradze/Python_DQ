from collections import Counter
import csv
import os
import string


class TextStatistics:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write('')

    def count_words(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            words = [word for line in lines[1:] for word in line.split()]
        ascii_words = [word.translate(str.maketrans('', '', string.punctuation)).lower() for word in words]
        ascii_words = [word for word in ascii_words if word.isascii() and not word.isdigit() and len(word) > 1]
        word_counts = Counter(ascii_words)
        return dict(word_counts)

    def count_letters(self):
        with open(self.filename, 'r') as f:
            # Read the contents of the file
            contents = f.read()

            # Skip the first line if it exists
            if '\n' in contents:
                contents = contents.split('\n', 1)[1]

        count_all = len(contents)
        count_uppercase = sum(1 for c in contents if c.isupper() and c.isalpha())
        count_lowercase = sum(1 for c in contents if c.islower() and c.isalpha())
        count_space = sum(1 for c in contents if c.isspace())
        count_letters = count_all - count_space
        percentage_uppercase = 0 if count_letters == 0 else count_uppercase / count_letters * 100
        percentage_lowercase = 0 if count_letters == 0 else count_lowercase / count_letters * 100

        return {
            'count_all': count_all,
            'count_uppercase': count_uppercase,
            'count_lowercase': count_lowercase,
            'count_letters': count_letters,
            'percentage_uppercase': round(percentage_uppercase, 2),
            'percentage_lowercase': round(percentage_lowercase, 2)
        }

    def write_results_to_csv(self):
        # Write word counts to CSV
        word_counts = self.count_words()
        with open('word_counts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Word', 'Count'])
            for word, count in word_counts.items():
                writer.writerow([word, count])

        # Write letter counts to CSV
        letter_counts = self.count_letters()
        with open('letter_counts.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Count type', 'Count'])
            writer.writerow(['All', letter_counts['count_all']])
            writer.writerow(['Uppercase', letter_counts['count_uppercase']])
            writer.writerow(['Lowercase', letter_counts['count_lowercase']])
            writer.writerow(['Letters', letter_counts['count_letters']])
            writer.writerow(['Percentage uppercase', letter_counts['percentage_uppercase']])
            writer.writerow(['Percentage lowercase', letter_counts['percentage_lowercase']])

    @classmethod
    def write_processed_records(cls, records_text):
        if records_text is not None:
            # Get the directory where the application is located
            app_dir = os.path.dirname(os.path.abspath(__file__))
            # Construct the file path for the output file relative to the application directory
            output_file_path = os.path.join(app_dir, 'records_from_file.txt')
            # Open the output file in write mode
            with open(output_file_path, 'w') as f:
                # Write the records text to the file
                f.write(records_text)
        else:
            print("Failed to read records from file.")

