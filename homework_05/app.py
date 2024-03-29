from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', endpoint='index')
def hello_world():
    return render_template('index.html')


@app.route('/about/', endpoint='about')
def text():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
