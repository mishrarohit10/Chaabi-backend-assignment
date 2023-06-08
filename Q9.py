from datetime import datetime, timedelta

def func(from_date, to_date, diff):
    format = '%Y/%m/%d'

    from_date = datetime.strptime(from_date, format)
    to_date = datetime.strptime(to_date, format)

    delta =  to_date - from_date 
    if delta.days < diff:
        return True
    else:
        return False

str_d1 = '2021/10/20'
str_d2 = '2021/10/20'
diff = 10

print(func(str_d1, str_d2 , diff))
