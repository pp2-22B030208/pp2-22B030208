'''#1
from datetime import datetime,date, timedelta, time
print(datetime.now()+timedelta(days=-5))'''


'''#2

from datetime import datetime,date, timedelta
print(datetime.now()-timedelta(days=1))
print(datetime.now())
print(datetime.now()+timedelta(days=1))'''

'''#3
import datetime
from datetime import datetime,date,timedelta

def drop():
    print(datetime.now().replace(microsecond=0))

drop() '''

'''#4
from datetime import date, datetime,timedelta,time
a = datetime.today()
b = datetime.strptime("2 March 2022, 07:00:00", "%d %B %Y, %H:%M:%S")
c = (a-b).seconds
print(datetime.today())
print(c) '''

