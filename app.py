from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total Requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return "Hello Prometheus!"

if __name__ == "__main__":
    start_http_server(8000)
    app.run(port=5000)