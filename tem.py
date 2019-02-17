@app.route('/tmpl')
def t():
    #templates folder <-- default, which makes it possible to run index.html straight away
    dic = {'A':'a', 'B':'b', 'C':'c'}
    # Example: Markup()
    a = "<h1>iii = <i>%s</i>" % "Italic"
    # h = a % 'Italic'
    b = "<strong>%s</strong></h1>" % '몰라'
    
    mu = Markup(a) + Markup(b)

    lst = [("노래1", "가수1", True), ("노래2", "가수2", True), ("노래3", "가수3", False), ("노래4", "가수4", False)]
    # title="제목", name=Markup("<strong>이름</strong>"), dic = dic, mu=mu, lst = lst
    d = {'title': '제목', 'name' : Markup("<strong>이름</strong>"), 'dic' : dic, 'mu' :mu, 'lst' : lst}
    
    aa = (1, "만남1", "김건모", False, [])
    bb = (2, "만남2", "노사연", True, [aa])
    cc = (3, "만남3", "익명", False, [aa,bb])
    dd = (4, "만남4", "익명", False, [aa,bb,cc])

    pyth = Rec('파이썬', 'https://www.naver.com')
    jv = Rec('자바', 'https://www.naver.com')
    pl = Rec('프로그래밍 언어', 'https://www.naver.com', [pyth, jv])

    jj = Rec('Jinja', 'https://www.naver.com')
    gc = Rec('Genshi, cheetah', 'https://www.naver.com')
    flsk = Rec('플라스크','https://www.naver.com', [jj, gc])
    spr = Rec('스프링', 'https://www.naver.com')
    nd = Rec('노드', 'https://www.naver.com')
    wf = Rec('웹 프레임워크', 'https://www.naver.com', [flsk,spr,nd])

    daily = Rec('나의 일상', 'https://www.naver.com')
    board = Rec('이슈 게시판', 'https://www.naver.com')
    others = Rec('기타', 'https://www.naver.com', [daily, board])

    return render_template('index.htm', d = d, lst2 = [aa,bb,cc,dd], navs = [pl, wf, others])

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
    return "Session has been set"

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


@app.route('/dt')
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "Korea: " + str(datestr)

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