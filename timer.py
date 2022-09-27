from datetime import datetime, date
import sys

class timer:
    def __init__(self, end_date):
        self.end_date = end_date

    def validate_date(self):
        self.convert_to_date = datetime.strptime(self.end_date, "%Y-%m-%d")
        self.today = datetime.today()
        if self.convert_to_date <= self.today:
            sys.exit('End date has to be in the future')    
        return self.convert_to_date, self.today
    
    def calculate_diff(self):
        self.time_left = self.convert_to_date - self.today
        return self.time_left

