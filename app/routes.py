from flask import render_template
from flask import request

from app import app
import BD_conn


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')  # запрос к данным input
        phone = request.form.get('phone')

    if "submit" in request.form:  # если нажата кнопка добавить
        if name and phone:
            print(name, phone)
            cursor = BD_conn.get_cursor()
            BD_conn.add_data(cursor=cursor, data=[name, phone])
    return render_template('index.html', title='Home')


@app.route("/show")
def show():
    cursor = BD_conn.get_cursor()
    rows = BD_conn.get_data(cursor=cursor)
    return render_template('show.html', title='DB', rows=rows)
