class News:
    def __init__(self, _text, _city, _create_date):
        self.text = _text
        self.city = _city
        self.create_date = _create_date

    def write_news(self, filename):  # Remove the 'city' parameter from here
        with open(filename, 'a') as f:
            f.write((f"News -------------------------\n"
                     f"{self.publish_news()}\n"
                     "------------------------------\n"))

    def publish_news(self):
        news_article = (f"{self.text}\n"
                        f"{self.city}, {self.create_date}")
        return news_article


