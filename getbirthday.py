class GetBirthDay:
    DAY_NAMES = ["Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday", "Sunday"]
    MONTHS = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    def __init__(self, day, month, year):
        # TODO: Validate the day, month and year, and raise a ValueError
        #       otherwise!
        self.year = year
        self.month = month
        self.day = day

    def day_index(self):
        # TODO: Figure out what day the date corresponds to, and return
        #       0-6 inclusive depending on what day it is - 0 is Monday, 1 is
        #       Tuesday, and so on.
        return 0