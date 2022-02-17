from datetime import time, date, datetime


print(time(hour=5, microsecond=30, second=20))

print(date.today())

date_20210123 = date.fromisoformat("2021-01-23")
print(date_20210123)

date_20210124 = datetime.strptime("2021 Oct 24", "%Y %b %d")
print(date_20210124)

