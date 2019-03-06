# coding=utf-8
from flask import Blueprint
from norwhale import app
from flask import jsonify
from norwhale.api.models.user import User

'''
获取用户信息
'''
# 定义蓝图
blueprint_User = Blueprint('blueprint_User', __name__)
# 定义路由
@app.route('/api/getAllUser')
def getAllUser():
    user = User.query.all()
    print(jsonify(data=[i.serialize for i in user]))
    return jsonify(data=[i.serialize for i in user])
