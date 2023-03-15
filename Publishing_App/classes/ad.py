class Ad:
    def __init__(self, _text, _ad_date, _days_left):
        self.text = _text
        self.ad_date = _ad_date
        self.days_left = _days_left

    def write_ad(self, filename):
        with open(filename, 'a') as f:
            f.write((f"Private ad -------------------\n"
                     f"{self.publish_ad()}\n"
                     "------------------------------\n"))

    def publish_ad(self):
        ad_info = (f"{self.text}\n"
                   f"Actual until, {self.ad_date}, "
                   f"{self.days_left} days left")
        return ad_info
