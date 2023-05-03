import datetime as dt
def function(a):
    today = dt.date.today()
    return today + dt.timedelta(days=int(a))

def get_day_of_week(date_str):
    date_object = dt.datetime.strptime(date_str, '%d,%m,%Y')
    date_of_week = date_object.weekday()
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day_str = days[date_of_week]
    return day_str






# def function2(date):
#     today = date.today()
#     data = today + timedelta(date=int(date))
#     date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
#     return data
# x = calendar.day_name[data.weekday()]






