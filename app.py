from flask import Flask
from flask_restful import Api, Resource, reqparse
from pymemcache.client import base
from binary_tree import BinaryTree
from lca import LCA


client = base.Client(('localhost', 11211))
client.set('some_key', 'some value')

print(client.get('some_key'))


app = Flask(__name__)
api = Api(app)

api.add_resource(BinaryTree, '/push/')
api.add_resource(LCA, '/lca/')

app.run(debug=True)
