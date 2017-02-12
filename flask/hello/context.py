
from flask import Flask, request, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/<pr>')
def hello_world(pr):
    ua = request.headers.get('User-Agent')
    my_list = [1,2,3.4,6.8901]
    return render_template('index.html', list=my_list, param=pr, user_agent=ua)

@app.route('/context')
def context():
    ua = request.headers.get('User-Agent')
    return 'your browser is %s' % ua

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
