class GetBirthDay:
    def __init__(self, day, month, year):
        date_sections = [day, month, year]
        if len(list(filter(lambda x: x >= 0, date_sections))) < 3:
            raise ValueError 
        self.day = day
        self.month = month
        self.year = year
    

    def getBirthDay(self):
        return 6