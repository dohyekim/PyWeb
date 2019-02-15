import os
from flask import Flask, url_for
from datetime import timedelta
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
# Flask(module 이름)이 들어가야 함
app = Flask('helloflask')
app.debug = True  

app.config.update(
	# salt
    SECRET_KEY='X1243yRH!mMwf',
	SESSION_COOKIE_NAME='pyweb_flask_session',
	PERMANENT_SESSION_LIFETIME=timedelta(31)      # 31 days
)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
    
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
