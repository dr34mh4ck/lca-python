from flask_restful import Resource, reqparse
from flask import request
from node import Node
import json
from pymemcache.client import base


class BinaryTree(Resource):

    tree = Node()

    parser = reqparse.RequestParser()
    parser.add_argument('values', type=list, required=True, help='Must provide a list of values!')
    parser.add_argument('node1', type=int, required=True, help='Must provide a pair of nodes!')
    parser.add_argument('node2', type=int, required=True, help='Must provide a pair of nodes!')

    def post(self):
        values = request.json['values']
        [self.tree.push(int(float(value))) for value in values]
        print('----------------------------')
        print(request.json['node1'])
        path1 = self.tree.path_to(request.json['node1'])
        path2 = self.tree.path_to(request.json['node2'])
        path1_nodes = path1.split('-')
        lca = None
        for value in path1_nodes:
            if lca is not None:
                break
            if path2.find(value) >= 0:
                lca = value
        return {'LCA':lca}, 200


    @classmethod
    def is_valid_list(values):
        for value in values:
            if not isinstance(value, int):
                return False
        return True
