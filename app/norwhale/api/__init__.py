# coding=utf-8
from .user import blueprint_User
from flask import Blueprint
from norwhale import app

blueprint_api = Blueprint('api', __name__)

'''
导入蓝图
'''

'''
注册蓝图
'''
app.register_blueprint(blueprint_User)
