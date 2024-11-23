
from flask import Flask

app = Flask(__name__)
#route de base 
@app.route('/')
def hello_world():
    return 'Hello World'
#route health check
@app.route('/health')
def health_check():
    return 'health check is ok ', 200  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
