import os
import datetime as dt
import json
from classes.text_file_records import TextFileRecords
from classes.text_statistics import TextStatistics
from classes.news import News
from classes.ad import Ad
from classes.weather_forecast import WeatherForecast
from classes.xml_file_records import XMLFileRecords
from classes.db_connection import DBConnection


def take_from_file(db_conn):
    # Prompt the user to enter the filename for the file
    filename = input("Please enter the filename of the file"
                     "(file should be in .txt .json or .xml format)"
                     "or the full path if file is in another directory: ")
    # Check if the file exists
    if not os.path.exists(filename):
        print("File not found.")
        return
    # Check the file extension to determine how to read the file
    if filename.endswith(".txt"):
        # Initialize a TextFileRecords object with the provided filename
        text_file_records = TextFileRecords(filename)
        # Read the records from the provided file
        records_text = text_file_records.read_records()
        # Get the directory where the application is located
        app_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the file path for the output file relative to the application directory
        output_file_path = os.path.join(app_dir, 'records_from_file.txt')
        # Save the records to a new file in the same directory as main.py
        TextFileRecords.write_processed_records(records_text, output_file_path)
        # Get the Records object from the TextFileRecords object
        records_object = text_file_records.get_records_object()
        # Write the results to CSV files
        records_object.write_results_to_csv()
    elif filename.endswith(".json"):
        with open(filename) as f:
            data = json.load(f)

        records_text = []
        for record_id, record_data in data.items():
            if record_data["publication_type"] == "news":
                # Create a News object and add the delimiter
                news = News(record_data["text"], record_data["city"], dt.datetime.now().strftime('%d/%m/%Y %H.%M'))
                records_text.append("News -------------------------")
                records_text.append(news.publish_news())
                records_text.append("------------------------------")

                news_title = news.title
                news_content = news.content
                news_city = news.city
                news_created_at = news.created_at
                db_conn.insert_news(title=news_title, content=news_content, city=news_city, created_at=news_created_at)


            elif record_data["publication_type"] == "ad":
                # If the publication type is "ad", create an Ad object
                ad_date = dt.datetime.strptime(record_data["date"], '%Y-%m-%d').date()
                days_left = (ad_date - dt.date.today()).days
                ad = Ad(record_data["text"], ad_date, days_left)
                records_text.append(
                    f"Ad ---------------------------\n{ad.publish_ad()}\n------------------------------")
            elif record_data["publication_type"] == "weather":
                # If the publication type is "weather", create a WeatherForecast object
                forecast_date = dt.datetime.strptime(record_data["forecast_date"], '%Y-%m-%d').date()
                forecast = WeatherForecast(record_data["city"], forecast_date, record_data["high_temperature"],
                                           record_data["low_temperature"], record_data["conditions"])
                records_text.append(f"Weather forecast -------------")
                records_text.append(forecast.publish_forecast())
                records_text.append("------------------------------")

                weather_city = forecast.city
                weather_forecast_date = forecast.forecast_date
                weather_high_temp = forecast.high_temperature
                weather_low_temp = forecast.low_temperature
                weather_conditions = forecast.conditions
                db_conn.insert_weather(city=weather_city, forecast_date=weather_forecast_date,
                                       high_temperature=weather_high_temp, low_temperature=weather_low_temp,
                                       conditions=weather_conditions)

    elif filename.endswith(".xml"):
        # Read records from XML file
        xml_file_records = XMLFileRecords(filename)
        records = xml_file_records.read_records()
        records_text = []
        for record in records:
            record_type = record.get("type")
            if record_type == "news":
                # Create a News object and add the delimiter
                news = News(record.find("text").text, record.find("city").text,
                            dt.datetime.now().strftime('%d/%m/%Y %H.%M'))
                records_text.append("News -------------------------")
                records_text.append(news.publish_news())
                records_text.append("------------------------------")

                news_title = news.title
                news_content = news.content
                news_city = news.city
                news_created_at = news.created_at
                db_conn.insert_news(title=news_title, content=news_content, city=news_city, created_at=news_created_at)

            elif record_type == "ad":
                # If the publication type is "ad", create an Ad object
                ad_date = dt.datetime.strptime(record.find("date").text, '%Y-%m-%d').date()
                days_left = (ad_date - dt.date.today()).days
                ad = Ad(record.find("text").text, ad_date, days_left)
                records_text.append(
                    f"Ad ---------------------------\n{ad.publish_ad()}\n------------------------------")

                ad_title = ad.title
                ad_content = ad.content
                ad_city = ad.city
                ad_created_at = ad.created_at
                db_conn.insert_ad(title=ad_title, content=ad_content, city=ad_city, created_at=ad_created_at)

            elif record_type == "weather":
                # If the publication type is "weather", create a WeatherForecast object
                forecast_date = dt.datetime.strptime(record.find("forecast_date").text, '%Y-%m-%d').date()
                forecast = WeatherForecast(record.find("city").text, forecast_date,
                                           record.find("high_temperature").text,
                                           record.find("low_temperature").text, record.find("conditions").text)
                records_text.append("Weather forecast -------------")
                records_text.append(forecast.publish_forecast())
                records_text.append("------------------------------")

                weather_city = forecast.city
                weather_forecast_date = forecast.forecast_date
                weather_high_temp = forecast.high_temperature
                weather_low_temp = forecast.low_temperature
                weather_conditions = forecast.conditions
                db_conn.insert_weather(city=weather_city, forecast_date=weather_forecast_date,
                                       high_temperature=weather_high_temp, low_temperature=weather_low_temp,
                                       conditions=weather_conditions)

        # Get the directory where the application is located
        app_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the file path for the output file relative to the application directory
        output_file_path = os.path.join(app_dir, 'records_from_file.txt')
        # Save the records to a new file in the same directory as main.py
        TextFileRecords.write_processed_records(records_text, output_file_path)
        # Write the results to CSV files
        records_object = TextStatistics(output_file_path)
        records_object.write_results_to_csv()

    # Prompt the user to choose whether to remove the source file
    remove_file = input("Do you want to remove the source file after it is processed? (y/n): ")
    if remove_file.lower() == 'y':
        os.remove(filename)


def take_from_user_input(db_conn):
    # Prompt the user to input a filename for the notebook.
    filename = input("Please provide name for the notebook where results will be saved (without file extension). "
                     "Note: if file name is not provided, it will be saved in default 'log.txt' file\n"
                     "Please, enter name for the file: ")
    # If the filename is not provided, use a default filename.
    if not filename:
        filename = "notebook"
    # Add the file extension to the filename.
    filename = f"{filename}.txt"

    record = TextStatistics(filename)
    # Prompt the user to select a data type ('News', 'Ad', or 'Weather')
    # and store their input in the 'greeting' variable.
    greeting = input("Hello, please select data type. 'News', 'Ad' or 'Weather': ")

    if greeting.lower() == 'news':
        text = input("Please input some text: ")
        city = input("Please enter city: ")
        create_date = dt.datetime.now().strftime('%d/%m/%Y %H.%M')
        news = News(text, city, create_date)
        db_conn.insert_news(title=text, content=city, city=create_date, created_at=create_date)
        news.write_news(filename)

    elif greeting.lower() == 'ad':
        text = input("Please input some text: ")
        user_input_date = input("Please advertising's end date (in DD-MM-YYYY format): ")
        if not user_input_date:
            user_input_date = (dt.datetime.now() + dt.timedelta(days=1)).strftime('%d-%m-%Y')
        user_date = dt.datetime.strptime(user_input_date, '%d-%m-%Y').date()

        days_left = (user_date - dt.date.today()).days
        ad = Ad(text, user_date, days_left)
        db_conn.insert_ad(title=text, content=text, end_date=user_date)
        ad.write_ad(filename)

    elif greeting.lower() == 'weather':
        city = input("Please enter city: ")
        user_input_date = input("Please enter forecasted date (in DD-MM-YYYY format): ")

        if not user_input_date:
            # Get tomorrow's date as default if user input was empty string
            user_input_date = (dt.datetime.now() + dt.timedelta(days=1)).strftime('%d-%m-%Y')

        user_date = dt.datetime.strptime(user_input_date, '%d-%m-%Y').date()
        high_temperature = float(input("Please input the high temperature: "))
        low_temperature = float(input("Please input the low temperature: "))
        conditions = input("Please input the weather conditions: ")

        user_date_str = user_date.strftime('%d-%m-%Y')
        weather = WeatherForecast(city, user_date_str, high_temperature, low_temperature, conditions)
        db_conn.insert_weather(city=city, forecast_date=user_date_str, high_temp=high_temperature, low_temp=low_temperature, conditions=conditions)
        weather.write_weather(filename)

        # Write the results to CSV files
    record.write_results_to_csv()


def main():
    # Initialize the DBConnection instance
    database_name = "my_database.db"
    db_conn = DBConnection(database_name)

    # Ask the user to select a source for records
    source = input("Please select a source for records. 'Provide file' or 'User input': ")
    if source.lower() == 'provide file':
        # If the user selects "Provide file", call the take_from_file function and capture the result
        take_from_file(db_conn)
    elif source.lower() == 'user input':
        # If the user selects "User input", call the take_from_user_input function
        take_from_user_input(db_conn)


if __name__ == '__main__':
    main()