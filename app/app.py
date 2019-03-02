#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask import jsonify
from models import User

app = Flask(__name__)

@app.route('/')
def hello_world():
    #init_db()
    #print("DB has been created!!")
    #admin = User("admin","admin@app.com")
    #guest = User("guest", "guest@app.com")
    #db_session.add(admin)
    #db_session.add(guest)
    #db_session.commit()
    #print("User were added!!")
    return 'Completed!'

@app.route('/hello')
def next_step():
    user = User.query.all()
    print(jsonify(data=[i.serialize for i in user]))
    return jsonify(data=[i.serialize for i in user])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
