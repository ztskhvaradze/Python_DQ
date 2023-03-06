from classes.records import Records
import datetime as dt


# create main function to execute the functionality
def create_notebook():

    # Prompt the user to input a filename for the notebook.
    filename = input(
        "Please enter a filename for the notebook where"
        "results will be saved (without file extension): ")

    # If the filename is not provided, use a default filename.
    if not filename:
        filename = "notebook"

    # Add the file extension to the filename.
    filename = f"{filename}.txt"

    record = Records(filename)
    # Prompt the user to select a data type ('News', 'Ad', or 'Weather')
    # and store their input in the 'greeting' variable.
    greeting = input(
        "Hello, please select data type. 'News', 'Ad' or 'Weather': ")

    # If the user selected 'News', prompt them to input
    #  some text and the city name.
    #  Get the current date and time and store it in
    #  'create_date' variable using the strftime method.
    if greeting.lower() == 'news':
        text = input("Please input some text: ")
        city = input("Please enter city: ")

        record.write_news(text, city)

    # If the user selected 'Ad', prompt them to input some text and
    #  the end date of the ad in the format 'DD-MM-YYYY'.
    # Convert the user-inputted date to a datetime object and
    #  calculate the number of days left until the ad expires.
    elif greeting.lower() == 'ad':
        text = input("Please input some text: ")
        user_input_date = input(
            "Please advertising's end date (in DD-MM-YYYY format): ")
        if not user_input_date:
            # Get tomorrow's date as default if user input was empty string
            user_input_date = (dt.datetime.now() +
                               dt.timedelta(days=1)).strftime('%d-%m-%Y')
        user_date = dt.datetime.strptime(user_input_date, '%d-%m-%Y').date()

        record.write_ad(text, user_date)
    # If the user selected 'Weather', prompt them to input the city,
    #  forecasted date in the format 'DD-MM-YYYY',
    # high and low temperature, and weather conditions.
    elif greeting.lower() == 'weather':
        city = input("Please enter city: ")
        user_input_date = input(
            "Please enter forcasted date (in DD-MM-YYYY format): ")
        if not user_input_date:
            # Get tomorrow's date as default if user input was empty string
            user_input_date = (dt.datetime.now() +
                               dt.timedelta(days=1)).strftime('%d-%m-%Y')
    # Add the file extension to the filename.
        filename = f"{filename}.txt"
        user_date = dt.datetime.strptime(user_input_date, '%d-%m-%Y').date()
        high_temperature = input("Please enter max temp: ")
        low_temperature = input("Please enter min temp: ")
        conditions = input(
            "Please enter weather conditions (like sunny, rainy, etc.): ")

        record.write_weather(
            city, user_date, high_temperature, low_temperature, conditions)
    else:
        print("Sorry, I didn't understand your request,"
              "because your answer did not match any of the provided options."
              " Please, try again")


if __name__ == '__main__':
    create_notebook()

#some small change