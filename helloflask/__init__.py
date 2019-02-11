from datetime import datetime, date, timedelta
from flask import Flask, g, Response, make_response, request, session, render_template, Markup

app = Flask(__name__)
app.debug = True  

app.config.update(
	# salt
    SECRET_KEY='X1243yRH!mMwf',
	SESSION_COOKIE_NAME='pyweb_flask_session',
	PERMANENT_SESSION_LIFETIME=timedelta(31)      # 31 days
)

# app.jinja_env.trim_blocks = True


@app.route('/tmpl')
def t():
    #templates 폴더는 default 폴더이기 때문에 index.html을 그냥 바로 불러도 됨
    dic = {'A':'a', 'B':'b', 'C':'c'}
    # Example: Markup()
    a = "<h1>iii = <i>%s</i>" % "Italic"
    # h = a % 'Italic'
    b = "<strong>%s</strong></h1>" % '몰라'
    
    mu = Markup(a) + Markup(b)
    # h = mu % "Italic"

    # print("h=", h) # h=<h1>iii = <i>Italic</i><h1>
    # return render_template("index.html", markup=Markup(h))

    return render_template('index.htm', title="제목", name=Markup("<strong>이름</strong>"), dic = dic, mu=mu)




#다음 형태로 요청했을때 해당 key로 Cookie를 굽는 코드를 작성하시오.
# http://localhost:5000/wc?key=token&val=abc

@app.route('/wc')
def wc():
    key = request.args.get('key')
    value = request.args.get('val')
    res = Response('Done',200)
    res.set_cookie(key, value)
    # session[key] = value
    session['Token'] = '123X'
    return make_response(res)

@app.route('/setsess')
def setsess():
    # session의 key값
    session['Token'] = '123X'
    return "Session이 설정됐습니다"

@app.route('/getsess')
def getsess():
    return "Token is " + session.get('Token')

# 다음과 같이 요청했을때 해당 key의 Cookie Value를 출력하는 코드를 작성하시오.
# http://localhost:5000/rc?key=token

@app.route('/rc')
def rc():
    key = request.values.get('key')
    val = request.cookies.get(key)
    return "cookie value --> " + val + session.get('Token')
    # return request.cookies.get('UserToken')


@app.route('/req_param')
def req_param():
    print("is_xhr --> ", request.is_xhr)
    print("endpoint --> ", request.endpoint)
    print("get_json --> ", request.get_json())
    print("max content length --> ", request.max_content_length)
    return ('REQUEST_METHOD: %(REQUEST_METHOD) s <br>'
            'SCRIPT_NAME: %(SCRIPT_NAME) s <br>'
            'PATH_INFO: %(PATH_INFO) s <br>'
            'QUERY_STRING: %(QUERY_STRING) s <br>'
            'SERVER_NAME: %(SERVER_NAME) s <br>'
            'SERVER_PORT: %(SERVER_PORT) s <br>'
            'SERVER_PROTOCOL: %(SERVER_PROTOCOL) s <br>'
            'wsgi.version: %(wsgi.version) s <br>'
            'wsgi.url_scheme: %(wsgi.url_scheme) s <br>'
            'wsgi.input: %(wsgi.input) s <br>'
            'wsgi.errors: %(wsgi.errors) s <br>'
            'wsgi.multithread: %(wsgi.multithread) s <br>'
            'wsgi.multiprocess: %(wsgi.multiprocess) s <br>'
            'wsgi.run_once: %(wsgi.run_once) s') % request.environ

# 예시: localhost:5000/dt?date=2019-02-09
def ymd(fmt):
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans


@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식: " + str(datestr)

@app.route("/sd")
def helloworld_local():
    return "Hello Local.com!"

# app.config['SERVER_NAME'] = 'local.com:5000'
#g.local.com
@app.route("/sd", subdomain="g")
def helloworld():
    return "Hello G.Local.com!!!"


@app.route('/test/<tid>')
def test3(tid):
	return "tid is %s" % tid

@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [ ('Content-Type', 'text/plain'), 
					('Content-Length', str(len(body))) ]
        start_response('200 OK', headers)
        return [body]

    return make_response(application)

@app.route("/res1")
def res1():
    custom_res = Response("Custom Response", 200, {'test': 'ttt'})
    return make_response(custom_res)
# @app.before_request
# def before_request():
#     print("before_request!!!")
#     # g 는 application context 영역, 요청을 보내는 모든 사람들이 공유하는 공간
#     g.str = "한글"

# #localhost:5000/gg
# @app.route("/gg")
# def helloworld2():
#     #
#     return "Hello World!" + getattr(g, 'str', '111')

# @app.route("/")
# def helloworld():
#     return "Hello Flask World!!!!!!!!!"

@app.before_request
def before_request():
    # print("before_request!!!")
    g.str = "한글"

@app.route("/")
def hello_world():
    return "Hello World!" + getattr(g, 'str', '111')
