
from flask import Flask

app = Flask(__name__)
#route principale 
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World'
#route health check
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
