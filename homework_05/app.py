"""
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
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
