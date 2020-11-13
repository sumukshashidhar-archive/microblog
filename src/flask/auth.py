from flask import Flask, request
from app import app
import sqlite3

def hash_password(passw):
    return passw



@app.route('/createUser', methods=['POST'])
def create_user():
    uname = request.form['username']
    passw = request.form['password']
    passw = hash_password(passw)
    try:
        conn = sqlite3.connect('./../../db/dbase.db')
        CREATE_STRING = f'INSERT INTO users (userid, username, password) VALUES (1, "{uname}", "{passw}")'
        conn.execute(CREATE_STRING)
        conn.commit()
        conn.close()
    except:
        return 500
    return 200
