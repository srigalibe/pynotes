from flask import (
    Flask,
    request,
    render_template,
    url_for,
    redirect,
    flash,
    session
)
import logging
from logging.handlers import RotatingFileHandler
import pymysql
import os


app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            flash("Successfully logged in")
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = "Incorrect username and password"
            app.logger.warning("Incorrect username and password for user ({})".
            format(request.form.get('username')))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

def valid_login(username, password):
    # mysql
    MYSQL_DATABASE_HOST = os.getenv('IP')
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'sri08'
    MYSQL_DATABASE_DB = 'my_flask_app'
    conn = pymysql.connect(
        host=MYSQL_DATABASE_HOST,
        user=MYSQL_DATABASE_USER,
        passwd=MYSQL_DATABASE_PASSWORD,
        db=MYSQL_DATABASE_DB
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE username='{}' AND password='{}'".format(
        username, password))
    
    data = cursor.fetchone()
    if data:
        return True
    else:
        return False

@app.route('/')
def welcome():    
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.secret_key = '1Ft\xe3b\x05\n\x9b,\xa1\x7f-f\x88\x15\x1aY\xa5G\x88\x1dA\x87\x16'
    
    # logging
    handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()