class GetBirthDay:

    def __init__(self, day, month, year):
        date_sections = [day, month, year]
        if len(list(filter(lambda x: x >= 0, date_sections))) < 3:
            raise ValueError
        self.year = year
        if month > 12:
            raise ValueError
        self.month = month
        if (day > self.getUpperLimitForMonth()):
            raise ValueError
        self.day = day

    def getUpperLimitForMonth(self):
        upperLimits = [31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (self.month - 1) != 1:
            return upperLimits[self.month - 1]

        if (((self.year % 4 == 0) and not (self.year % 100 == 0)) or (self.year % 400 == 0)):
            return 29
        return 28

    def getBirthDay(self):
        return 6
