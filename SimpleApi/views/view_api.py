__author__ = 'abhilash'
from SimpleApi.config.application_config import app
from SimpleApi.models.model_api import Product
from flask import jsonify, request
from flask_restful import Resource, Api

api = Api(app)

class Products(Resource):

    def get(self,):
        product = Product.objects.all()
        return jsonify({'Procucts': product})

    def put(self):
        p = request.form['data']
        Product(name=p).save()
        return jsonify({'msg': "Added"})


api.add_resource(Products, '/api/v1/product/')

