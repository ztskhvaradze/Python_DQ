from classes.Ad import Ad as Ad
from classes.News import News as News
from classes.WeatherForecast import WeatherForecast as WeatherForecast
import datetime as dt

class Records:
    def __init__(self, filename):
        self.filename = filename

    def write_news(self, text, city):
        create_date = dt.datetime.now().strftime('%d/%m/%Y %H.%M')
        news = News(text, city, create_date)
        news.publish_news()
        with open(self.filename, 'a') as f:
            f.write(
f"""
News -------------------------
{news.publish_news()}
------------------------------
\n
""")

    def write_ad(self, text, user_date):
        days_left = (user_date - dt.date.today()).days
        ad = Ad(text, user_date, days_left)
        ad.publish_ad()
        with open(self.filename, 'a') as f:
            f.write(f"""
Private ad -------------------
{ad.publish_ad()}
------------------------------\n
""")


    def write_weather(self, city, user_date, high_temperature, low_temperature, conditions):
        # Convert the date object to string using strftime method
        user_date_str = user_date.strftime('%d-%m-%Y')
        # create a WeatherForecast object with the given input options
        weather = WeatherForecast(city, user_date_str, high_temperature, low_temperature, conditions)
        # append the forecast to a file
        with open(self.filename, 'a') as f:
            f.write(f"""
Weather forecast -------------
{weather.publish_forecast()}
------------------------------\n
""")

if __name__ == '__main__':
    record = Records()
    greeting = input("Hello, please select data type. 'News', 'Ad' or 'Weather': ")

    if greeting.lower() == 'news':
        text = input("Please input some text: ")
        city = input("Please enter city: ")
        record.write_news(text, city)

    elif greeting.lower() == 'ad':
        text = input("Please input some text: ")
        user_input_date = input("Please advertising's end date (in DD-MM-YYYY format): ")
        record.write_ad(text, user_input_date)

    elif greeting.lower() == 'weather':
        city = input("Please enter city: ")
        user_input_date = input("Please enter forecasted date (in DD-MM-YYYY format): ")
        high_temperature = input("Please enter max temp: ")
        low_temperature = input("Please enter min temp: ")
        conditions = input("Please enter weather conditions (like sunny, rainy, etc.): ")
        record.write_weather(city, user_input_date, high_temperature, low_temperature, conditions)

    else:
        print("Sorry, I didn't understand your request, because your answer did not match any of the provided options, please try again")
