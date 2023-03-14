import datetime as dt
from collections import Counter
import csv
import os
import string
import re

from .ad import Ad
from .news import News
from .weather_forecast import WeatherForecast


class Records:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write('')

    def write_news(self, text, city):
        create_date = dt.datetime.now().strftime('%d/%m/%Y %H.%M')
        news = News(text, city, create_date)
        news.publish_news()
        with open(self.filename, 'a') as f:
            f.write((f"News -------------------------\n"
                     f"{news.publish_news()}\n"
                     "------------------------------\n"))

    def write_ad(self, text, user_date):
        days_left = (user_date - dt.date.today()).days
        ad = Ad(text, user_date, days_left)
        ad.publish_ad()
        with open(self.filename, 'a') as f:
            f.write((f"Private ad -------------------\n"
                     f"{ad.publish_ad()}\n"
                     "------------------------------\n"))

    def write_weather(self, city, user_date, high_temperature, low_temperature, conditions):
        # Convert the date object to string using strftime method
        user_date_str = user_date.strftime('%d-%m-%Y')
        # create a WeatherForecast object with the given input options
        weather = WeatherForecast(
            city, user_date_str, high_temperature, low_temperature, conditions)
        # append the forecast to a file
        with open(self.filename, 'a') as f:
            f.write((f"Weather forecast -------------\n"
                     f"{weather.publish_forecast()}\n"
                     "------------------------------\n"))

    def count_words(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            words = [word for line in lines[1:] for word in line.split()]
        ascii_words = [word.translate(str.maketrans('', '', string.punctuation)) for word in words]
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
        if count_letters == 0:
            return {
                'count_all': count_all,
                'count_uppercase': count_uppercase,
                'count_lowercase': count_lowercase,
                'count_letters': count_letters,
                'percentage_uppercase': 0,
                'percentage_lowercase': 0
            }
        return {
            'count_all': count_all,
            'count_uppercase': count_uppercase,
            'count_lowercase': count_lowercase,
            'count_letters': count_letters,
            'percentage_uppercase': count_uppercase / count_letters * 100,
            'percentage_lowercase': count_lowercase / count_letters * 100
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

