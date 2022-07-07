from importlib.resources import Resource
from flask import Response, request, jsonify
from flask_restful import Resource
from .db import mysql

class UserApi(Resource):
    def __init__(self) -> None:
        self.connection = mysql.connect()
        self.cursor = self.connection.cursor()
    
    def post(self):
        body = request.get_json()
        print(body)
        self.cursor.execute('SELECT * FROM user WHERE username=%s and password=%s', (body['username'], body['password']))
        data = self.cursor.fetchone()

        print(data)
        if(data == None or len(data) == 0): return {}, 401
        user = { "id": data[0], "username": data[1], "password": data[2]}
        return user, 200    
