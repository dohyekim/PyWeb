from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

class Radiobutton:
    def __init__(self, radioid, name, value, text, checked=''):
        self.radioid = radioid
        self.name = name
        self.value = value
        self.text = text
        self.checked = checked

lst = []
for i in range(1,6):
    radioid = 'radiobutton' + str(i)
    name = 'radioname'
    value = 'radiovalue' + str(i)
    text = str(i) + '번째 option'
    checked = ''
    if i == 4:
        checked = 'checked'
    lst.append(Radiobutton(radioid, name, value, text, checked))

# print(lst)
now = datetime.now()
# print(type(str(now)))
d = datetime.strptime('2019-02-01', '%Y-%m-%d')
a = d.strftime('%y-%m-%d')
nextDay = d + relativedelta(days=1)
nextMonth = d + relativedelta(months=1)

# for i in range(365):
#     d = d + timedelta(days=1)
#     print(d)

# print(d)
# print(nextDay)
# print(nextMonth)

dt = datetime.strptime('2019-02-02', '%Y-%m-%d')

# print(((now-dt).seconds)/60/60)

# d = datetime.strptime('2019-01-01', '%m-%d')
# a = 1
# for i in range(365):
#     d = d + relativedelta(days=1)
#     print(d)
    # a += 1
    # if a % 31 ==0:
    #     b = 0 
    #     print(d.weekday()-4)
    #     b += 1
    # if b == 1:
    #     a
# d = datetime.strptime('2019-03-01', '%Y-%m-%d')
# print(d.month)
# # print(timedelta(days=1,hours=1))
# # print(((d+relativedelta(months=1)) - timedelta(days=1)).day)

# startdate = d.weekday() * -1
# enddate = (d+relativedelta(months=1) - timedelta(days=1)).day
# print(startdate, type(startdate))
# print(enddate, type(enddate))


# for i in range (1,13):
#     d = datetime.strptime('2019-{:02d}-01'.format(i), '%Y-%m-%d')
#     print(d)

sdt = 2
d = datetime.strptime('2019-{:02d}-01'.format(sdt), '%Y-%m-%d')
startddate = d.weekday() * -1
print(startddate)