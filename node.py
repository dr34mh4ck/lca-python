'''
*** Binary tree structure is composed by Nodes (left and right) with a
*** reference to its parent and the value the Node holds
'''
class Node:


    value = None
    left = None
    right = None
    parent = None


    '''
    *** empty initialization for the Node
    '''
    def __init__(self):
        pass



    '''
    *** Checks wether this node has value assigned or not
    '''
    def is_empty(self):
        return self.value is None

    '''
    *** Inserts a Node into the tree assigning the correct parent for the Node
    '''
    def push_impl(self, _value, _parent):
        if self.value is None:
            self.value = _value
            self.parent = _parent
        elif self.value < _value:
            if self.right is None:
                self.right = Node()
            self.right.push_impl(_value, self)
        elif self.value > _value:
            if self.left is None:
                self.left = Node()
            self.left.push_impl(_value, self)


    '''
    *** Inserts a Node into the tree
    '''
    def push(self, _value):
        self.push_impl(_value, None)

    def print_pre_order(self):
        self.print_pre_order_impl('')

    '''
    *** Prints the tree with preorder path
    '''
    def print_pre_order_impl(self, prefix):
        if self.value is None:
            print('-')
        else:
            print(prefix + str(self.value))
            if self.left is not None:
                self.left.print_pre_order_impl(prefix + '  ')
            if self.right is not None:
                self.right.print_pre_order_impl(prefix + '  ')


    def path_to(self, _value):
        path = ''
        if self.value is None:
            return ''
        else:
            if self.value > _value:
                path += self.left.path_to(_value)
            elif self.value < _value:
                path += self.right.path_to(_value)
            path += str(self.value) + '-'
        return path
