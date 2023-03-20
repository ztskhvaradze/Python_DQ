class WeatherForecast:
    def __init__(self, _city, _forecast_date, _high_temperature,
                 _low_temperature, _conditions):
        self.city = _city
        self.forecast_date = _forecast_date
        self.high_temperature = _high_temperature
        self.low_temperature = _low_temperature
        self.conditions = _conditions

    def write_weather(self, filename):
        with open(filename, 'a') as f:
            f.write((f"Weather forecast -------------\n"
                     f"{self.publish_forecast()}\n"
                     "------------------------------\n"))

    def publish_forecast(self):
        forecast_info = (
            f"Forecast for {self.city} on {self.forecast_date}:\n"
            f"High temperature: {self.high_temperature} celsius\n"
            f"Low temperature: {self.low_temperature} celsius\n"
            f"Conditions: {self.conditions}"
        )
        return forecast_info
