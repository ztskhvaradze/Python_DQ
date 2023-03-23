import pyodbc

class DBConnection:
    """
    This class has three methods for inserting records into
    the news, ads, and weather tables respectively. It also has a
    get_records_object method that retrieves all records from the database
    and returns them as a dictionary.
    """
    def __init__(self, database_name):
        self.conn = pyodbc.connect(f"Driver=SQLite3 ODBC Driver;Database={database_name};")
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS news (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT,
                city TEXT,
                created_at TEXT
            )
        """)
        self.conn.commit()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS ads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT,
                end_date TEXT
            )
        """)
        self.conn.commit()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                forecast_date TEXT,
                high_temp REAL,
                low_temp REAL,
                conditions TEXT
            )
        """)
        self.conn.commit()

    def insert_news(self, title, content, city, created_at):
        self.cur.execute("INSERT INTO news (title, content, city, created_at) VALUES (?, ?, ?, ?)",
                          (title, content, city, created_at))
        self.conn.commit()

    def insert_ad(self, title, content, end_date):
        self.cur.execute("INSERT INTO ads (title, content, end_date) VALUES (?, ?, ?)",
                          (title, content, end_date))
        self.conn.commit()

    def insert_weather(self, city, forecast_date, high_temp, low_temp, conditions):
        self.cur.execute("INSERT INTO weather (city, forecast_date, high_temp, low_temp, conditions) VALUES (?, ?, ?, ?, ?)",
                          (city, forecast_date, high_temp, low_temp, conditions))
        self.conn.commit()

    def get_records_object(self):
        records = {
            "News": [],
            "Ad": [],
            "Weather forecast": []
        }
        # Retrieve records from the database
        self.cur.execute("SELECT * FROM news")
        for row in self.cur.fetchall():
            records["News"].append(row)
        self.cur.execute("SELECT * FROM ads")
        for row in self.cur.fetchall():
            records["Ad"].append(row)
        self.cur.execute("SELECT * FROM weather")
        for row in self.cur.fetchall():
            records["Weather forecast"].append(row)
        return records
