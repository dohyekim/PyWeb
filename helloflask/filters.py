from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from helloflask import app

@app.template_filter('ymdfilter')
def datetime_ymd(dt, fmt='%y-%m-%d %H:%M:%S'):
    if isinstance(dt, date):
        return dt.strftime(fmt)
    else:
        return dt

@app.template_filter('symdfilter')
def simple_ymd(dt):
    now = datetime.now()
    if not isinstance(dt, date):
        dt = datetime.strptime(dt, '%Y-%m-%d %H:%M') 
    if (now-dt).days < 1:
        return dt.strftime('%H:%M')
    elif (now-dt).days >= 1:
        return '<strong>%s</strong>'%dt.strftime('%m-%d')

@app.template_filter('sdtfilter')
def startdate(sdt):
    # if not isinstance(dt, date):
    #     dt = datetime.strptime(dt, '%Y-%m-%d %H:%M') 
    d = datetime.strptime('2019-{:02d}-01'.format(sdt), '%Y-%m-%d')
    startdate = d.weekday() * -1
    return 1 if startdate == (-6) else startdate

@app.template_filter('edtfilter')
def enddate(edt):
    d = datetime.strptime('2019-{:02d}-01'.format(edt), '%Y-%m-%d')
    enddate = (d+relativedelta(months=1) - timedelta(days=1)).day
    return enddate
