from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from flask import Flask, g, Response, make_response, request, session, render_template, Markup, url_for
import os
from helloflask.init_db import init_database, db_session


app = Flask(__name__)
import helloflask.views
import helloflask.filters
app.debug = True  

app.config.update(
	# salt
    SECRET_KEY='X1243yRH!mMwf',
	SESSION_COOKIE_NAME='pyweb_flask_session',
	PERMANENT_SESSION_LIFETIME=timedelta(31)      # 31 days
)
def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
    
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

@app.before_first_request
def beforeFirstRequest():
    init_database()
# app.jinja_env.trim_blocks = True

@app.teardown_appcontext
def teardown(exception):
    db_session.remove()