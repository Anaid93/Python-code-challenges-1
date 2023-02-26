'''Create a function that calculates and returns 
how many days there are between two strings 
representing dates.
- A string representing a date has the format ''dd/MM/yyyy''.
- The function will receive two Strings and return an Int.
- If one of the two text strings does not represent 
a correct date an exception will be thrown.'''

from datetime import datetime
from datetime import date


def string_date(date_1:date, date_2:date):
    try:
        date_11 = datetime.strptime(date_1, '%d/%m/%Y')
        date_22 = datetime.strptime(date_2, '%d/%m/%Y')
        print(date_11 - date_22)
    except:
        print('Text string does not represent a date correctly')
    
string_date('31/12/2022', '230/11/2022') 
string_date('31/12/2022', '23/11/2022')
