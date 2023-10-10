from datetime import datetime
import calendar
def convdate(my_string):
    # Create date object in given time format yyyy-mm-dd
    my_date = datetime.strptime(my_string, "%Y-%m-%d")

    # to get name of day from date
    return calendar.day_name[my_date.weekday()]
