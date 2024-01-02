import scraping_global_blue
from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to Web Scraping API!'


@app.route('/check_gb_tf_form/<docId>/<purchaseAmount>')
def check_document(docId=None, purchaseAmount=None):
    scraping = scraping_global_blue.ScrapingBlobalBlue()
    result = scraping.run_scraping(docId=docId, purchaseAmount=purchaseAmount)
    print(result)
    return result


"""
The entry point
Warning: Use 0.0.0.0 instead of 127.0.0.1 to avoid issue when use docker container   
"""
if __name__ == '__main__':
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5400")
    # Production
    http_server = WSGIServer(('', 5400), app)
    http_server.serve_forever()
