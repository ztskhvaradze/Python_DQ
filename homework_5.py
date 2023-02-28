import datetime as dt

# Prompt the user to select a data type ('News', 'Ad', or 'Weather') and store their input in the 'greeting' variable.
greeting = input("Hello, please select data type. 'News', 'Ad' or 'Weather': ")

# If the user selected 'News', prompt them to input some text and the city name.
#  Get the current date and time and store it in 'create_date' variable using the strftime method.
if greeting.lower() == 'news':
    text = input("Please input some text: ")
    city = input("Please enter city: ")
    create_date = dt.datetime.now().strftime('%d/%m/%Y %H.%M')
# If the user selected 'Ad', prompt them to input some text and the end date of the ad in the format 'DD-MM-YYYY'.
# Convert the user-inputted date to a datetime object and calculate the number of days left until the ad expires.
elif greeting.lower() == 'ad':
    text = input("Please input some text: ")
    user_input_date = input("Please advertising's end date (in DD-MM-YYYY format): ")
    user_date = dt.datetime.strptime(user_input_date, '%d-%m-%Y').date()
    days_left = (user_date - dt.date.today()).days

# If the user selected 'Weather', prompt them to input the city, forecasted date in the format 'DD-MM-YYYY',
# high and low temperature, and weather conditions.
elif greeting.lower() == 'weather':
    city = input("Please enter city: ")
    user_input_date = input("Please enter forcasted date (in DD-MM-YYYY format): ")
    user_date = dt.datetime.strptime(user_input_date, '%d-%m-%Y').date()
    high_temperature = input("Please enter max temp: ")
    low_temperature = input("Please enter min temp: ")
    conditions = input("Please enter weather conditions (like sunny, rainy, etc.): ")

# Define a News class with three instance variables: 'text', 'city', and 'create_date'.
# Also, define a method called 'publish_news' that returns a string containing the news article.  
class News:
    def __init__(self, text, city, create_date):
        self.text = text
        self.city = city
        self.create_date = create_date

    def publish_news(self):
        news_article = f"{self.text}\n{self.city}, {self.create_date}\n"
        return news_article

# Define an Ad class with three instance variables: 'text', 'ad_date', and 'days_left'.
# Also, define a method called 'publish_ad'
class Ad():
    def __init__(self, text, ad_date, days_left):
        self.text = text
        self.ad_date = ad_date
        self.days_left = days_left
    
    def publish_ad(self):
        ad_info = f"{self.text}\nActual until, {self.ad_date}, {self.days_left} days left"
        return ad_info
# Define an WeatherForecast class with three instance.
# Also, define a method called 'publish_forecast'
class WeatherForecast:
    def __init__(self, city, forecast_date, high_temperature, low_temperature, conditions):
        self.city = city
        self.forecast_date = forecast_date
        self.high_temperature = high_temperature
        self.low_temperature = low_temperature
        self.conditions = conditions
    
    def publish_forecast(self):
        forecast_info = f"Forecast for {self.city} on {self.forecast_date}:\nHigh temperature: {self.high_temperature} celsius\nLow temperature: {self.low_temperature} celsius\nConditions: {self.conditions}"
        return forecast_info

# check if the user input is 'News'
if greeting.lower() == 'news':
    # create a News object with the given text, city, and creation date
    news = News(text, city, create_date)
     # publish the news
    news.publish_news()
    # append the news to a file called 'records_notebook.txt'
    with open('recors_notebook.txt', 'a') as f:
        f.write(f"""
News -------------------------
{news.publish_news()}
------------------------------\n
""")
# doing the same thing with other 2 options
elif greeting.lower() == 'ad':
    ad = Ad(text, user_date, days_left)
    ad.publish_ad()
    with open('recors_notebook.txt', 'a') as f:
        f.write(f"""
Private ad -------------------
{ad.publish_ad()}
------------------------------\n
""")
elif greeting.lower() == 'weather':
    weather = WeatherForecast(city, user_input_date, high_temperature, low_temperature, conditions)
    weather.publish_forecast()
    with open('recors_notebook.txt', 'a') as f:
        f.write(f"""
Weather forecast -------------
{weather.publish_forecast()}
------------------------------\n
""")

