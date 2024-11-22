
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/health')
def health_check():
    return 'health check is ok ', 200  # Retourne un code HTTP 200 avec un message "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
