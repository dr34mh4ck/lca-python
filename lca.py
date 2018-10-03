from node import Node
from flask_restful import Resource, reqparse
from pymemcache.client import base

class LCA(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('node1', type=int, required=True, help='Must provide a pair of nodes!')
    parser.add_argument('node2', type=int, required=True, help='Must provide a pair of nodes!')


    def get(self):
        data = LCA.parser.parse_args()
        client = base.Client(('localhost', 11211))
        tree = client.get('tree')
        path1 = tree.path_to(int(data['node1']))
        path2 = tree.path_to(int(data['node2']))
        path1_nodes = path1.split('-')
        lca = None
        for value in path1_nodes:
            if lca is not None:
                break
            if path2.find(value) >= 0:
                lca = value
        return {'LCA':lca}, 200
