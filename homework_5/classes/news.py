class News:
    def __init__(self, _text, _city, _create_date):
        self.text = _text
        self.city = _city
        self.create_date = _create_date

    def publish_news(self):
        news_article = (f"{self.text}\n"
                        f"{self.city}, {self.create_date}")
        return news_article
