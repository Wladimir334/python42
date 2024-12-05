from datetime import datetime
from datetime import time
from datetime import timedelta

print(datetime.today())  # print(datetime.today().month или .minute)

current_time = time(17, 25, 10)
print(current_time)

print(datetime.now())
today = datetime.today()
print(today.strftime("%d.%m.%y"))
print(today.strftime("%d/%m/%Y"))
print(today.strftime("%d %B %Y (%A)"))
print(today.strftime("%d.%m.%y %H:%M:%S"))


birthday = "2024-12-21"
birthday_date = datetime.strptime (birthday, "%Y-%m-%d")
print(birthday_date)
print(type(birthday_date))
print(birthday_date.strftime("%d-%m-%Y"))


today = datetime.now()
deadline = 15
deadline = timedelta(days=deadline)
print(today + deadline)


now = datetime.now()
deadline_1 = datetime(year=2024, month=12, day=20)

print(deadline_1 - now)

if deadline_1 < now:
    print('Срок вышел ')
else:
    print(f"Ещё {(deadline_1 - now).days} дней")