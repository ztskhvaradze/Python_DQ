import datetime as dt

from .ad import Ad
from .news import News
from .weather_forecast import WeatherForecast


class Records:
    def __init__(self, filename):
        self.filename = filename

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
