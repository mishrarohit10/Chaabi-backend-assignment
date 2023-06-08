from datetime import datetime, timedelta

def func(from_date, to_date, diff):
    format = '%Y/%m/%d'

    from_date = datetime.strptime(from_date, format)
    to_date = datetime.strptime(to_date, format)

    delta = abs(to_date - from_date)
    if delta.days < diff:
        return True
    else:
        return False

# str_d1 = '2021/10/20'
# str_d2 = '2022/2/20'
# diff = 10


str_d1 = str(input('Enter from date in yyyy/mm/dd -> '))
str_d2 = str(input('Enter to date in yyyy/mm/dd -> '))
diff = int(input("Enter difference"))


print(func(str_d1, str_d2 , diff))
