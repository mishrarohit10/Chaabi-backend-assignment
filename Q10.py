from datetime import datetime , timedelta

def func(date,n):

    format = '%Y/%m/%d'

    curr_date = datetime.strptime(date,format)
    new_date = curr_date - timedelta(days=n)

    new_date = new_date.strftime(format)

    print(new_date)


# func('2023/01/10', 10)

curr_date = str(input("Enter date -> "))
diff = int(input("Enter number of days -> "))

func(curr_date,diff)

