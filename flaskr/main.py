import sqlite3

from flaskr import app
from flask import render_template, request, redirect, url_for

DATABASE = 'database.db'

app.run(port=8000, debug=True)


@app.route('/')
def index():
    """
    :return: dict
        books = [
        {
            'title': 'ソフトウェアアーキテクチャの基礎',
            'price': 4180,
            'arrival_day': '2022年7月1日'
        },
        {
            'title': '達人のデータベース',
            'price': 2580,
            'arrival_day': '2022年7月3日'
        }
    ]
    """
    con = sqlite3.connect(DATABASE)
    book_qs = con.execute("SELECT * FROM book").fetchall()

    books = [
        {
            'title': book[0],
            'price': book[1],
            'arrival_day': book[2]
        } for book in book_qs
    ]

    return render_template('index.html', books=books)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/register', methods=['POST'])
def register():
    title = request.form['title'] or '無題'
    price = request.form['price'] or 0
    arrival_day = request.form['arrival_day'] or '未定'

    con = sqlite3.connect(DATABASE)
    con.execute('INSERT INTO book VALUES(?,?,?)',
                [title, price, arrival_day])
    con.commit()
    con.close()
    return redirect(url_for('index'))
