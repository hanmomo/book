import datetime
today=datetime.date.today()
oneday=datetime.timedelta(days=1)
yesterday=today-oneday
tommorrow=today+oneday

print today,yesterday,tommorrow
