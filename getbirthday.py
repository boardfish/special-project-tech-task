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
        date_sections = [day, month, year]
        if len(list(filter(lambda x: x >= 0, date_sections))) < 3:
            raise ValueError
        self.year = year
        if month > 12:
            raise ValueError
        self.month = month
        if (day > self.get_upper_limit_for_month()):
            raise ValueError
        self.day = day
    
    def is_leap_year(self, year = None):
        if not year:
            year = self.year
        year_divisible_by_4 = year % 4 == 0
        year_divisible_by_100 = year % 100 == 0
        year_divisible_by_400 = year % 100 == 0
        return ((year_divisible_by_4 and not year_divisible_by_100) \
            or year_divisible_by_400)

    def get_upper_limit_for_month(self):
        upperLimits = [31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (self.month - 1) != 1:
            return upperLimits[self.month - 1]

        if self.is_leap_year():
            return 29
        return 28

    def get_start_of_month(self, month_number):
        if month_number < 0 or month_number > 11:
            raise ValueError
        leap_day = (self.is_leap_year() and month_number > 1) * 1
        return sum(list(self.MONTHS.values())[:month_number]) + leap_day

    def get_day_of_week(self, day_of_year):
        return (day_of_year % 7)
    
    def get_offset_for_year(self, year = None):
        if not year:
            year = self.year
        start_date_differences = [
            1 + (self.is_leap_year(year) * 1) for year in range(year, 2020)
            ]
        return self.get_day_of_week(2 - sum(start_date_differences))

    def day_index(self):
        offset = self.get_offset_for_year()
        return self.get_day_of_week(
            self.get_start_of_month(self.month - 1) + self.day - 1 + offset
        )