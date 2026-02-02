import calendar

month, day, year = map(int, input().split())

day = calendar.day_name[calendar.weekday(year, month, day)].upper()

print(day)
