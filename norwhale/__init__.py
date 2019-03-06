# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tst.db'

'''
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tst.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
'''

'''
导入蓝图定义
'''
from .api import blueprint_api


'''
注册蓝图
'''
app.register_blueprint(blueprint_api, subdomain='api')