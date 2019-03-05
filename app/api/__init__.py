from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow  import Marshmallow
from flask_cors import CORS,cross_origin
from flask_cache  import Cache
from flask import jsonify
from .models.users import User
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

'''测试用例'''
class testApi(Resource):
    def get(self, username):
        if(username=='all'):
           user = User.query.all()
           return jsonify(data=[i.serialize for i in user])
        else:
           user = User.query.filter_by(username=username).first()
           print(user)
           return jsonify(data=user.serialize)

'''加入API'''
api.add_resource(testApi, '/<string:username>')

