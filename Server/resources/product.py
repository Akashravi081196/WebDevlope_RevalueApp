from importlib.resources import Resource
from flask import Response, request, jsonify
from flask_restful import Resource
from .db import mysql

class ProductsApi(Resource):
    def __init__(self) -> None:
        self.connection = mysql.connect()
        self.cursor = self.connection.cursor()
        
    def get(self):
        self.cursor.execute("SELECT * FROM product")
        data = self.cursor.fetchall()

        products = []
        for d in data: products.append({ "id":d[0], "name": d[1], "price": d[2], "description": d[3], "userid": d[4]})
        return products, 200

    def post(self):
        body = request.get_json()
        print(body)
        self.cursor.execute('INSERT INTO product (name, price, description, userid) VALUES (%s, %s, %s, %s)', (body['name'], body['price'], body['description'], body['userid']))
        self.connection.commit()
        return { "id": "" }, 200

    def put(self):
        body = request.get_json()
        print(body)
        self.cursor.execute("UPDATE product SET name = %s, price = %s, description = %s WHERE id = %s", (body['name'], body['price'], body['description'], body['id']))
        self.connection.commit()
        return { "id": "" }, 200

class ProductApi(Resource):
    def __init__(self) -> None:
        self.connection = mysql.connect()
        self.cursor = self.connection.cursor()
    
    def get(self, id):
        self.cursor.execute("SELECT * FROM product WHERE userid = %s", id)
        data = self.cursor.fetchall()
        
        print(data)
        products = []
        for d in data: products.append({ "id":d[0], "name": d[1], "price": d[2], "description": d[3], "userid": d[4]})
        return products, 200

    def delete(self, id):
        self.cursor.execute("DELETE FROM product WHERE id = %s", id)
        self.connection.commit()
        return "", 200
    
