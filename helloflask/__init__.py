from flask import Flask, g, Response, make_response

app = Flask(__name__)
app.debug = True  

app.config['SERVER_NAME'] = 'local.com:5000'

@app.route("/sd")
def helloworld_local():
    return "Hello Local.com!"

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