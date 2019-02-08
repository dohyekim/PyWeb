# __init__.py는 자동 실행되니까 바로 import app하면 됨.
from helloflask import app

app.run(host='0.0.0.0') #127.0.0.1 (즉 localhost)