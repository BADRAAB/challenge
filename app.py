
from flask import Flask

app = Flask(__name__)
#route principale 
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World'
# Route de health check
@app.route('/health', methods=['GET'])
def health_check():
    return 'health check is ok', 200  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
