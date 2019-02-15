from helloflask.classes import Radiobutton, Selectbutton, Rec
from datetime import datetime, date, timedelta
from flask import Response, make_response, request, render_template, Markup, session
from helloflask.util import ymd

def py():
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

    sels = []
    for j in range(1,6):
        selvalue = 'value' + str(j)
        seltext = 'text' + str(j)
        selected = ''
        if j == 1:
            selected = 'selected'
        sels.append(Selectbutton(selvalue, seltext, selected))
    
    today = datetime.now()
    sdate = '2019-02-12 23:03'
    s2date = '2019-02-13 23:03'
    d = datetime.strptime('2019-01-01', '%Y-%m-%d')
    return render_template('py.htm', lst = lst, sels = sels, today = today, sdate = sdate, s2date=s2date)

def t():
    #templates 폴더는 default 폴더이기 때문에 index.html을 그냥 바로 불러도 됨
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

def wc():
    key = request.args.get('key')
    value = request.args.get('val')
    res = Response('Done',200)
    res.set_cookie(key, value)
    # session[key] = value
    session['Token'] = '123X'
    return make_response(res)

def setsess():
    # session의 key값
    session['Token'] = '123X'
    return "Session이 설정됐습니다"

def rc():
    key = request.values.get('key')
    val = request.cookies.get(key)
    return "cookie value --> " + val + session.get('Token')
    # return request.cookies.get('UserToken')

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

def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d'))
    return "우리나라 시간 형식: " + str(datestr)
