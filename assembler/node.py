'''
    A Node class definition
'''

from assembler.token import Token

class Node:
    '''
    Node class.
    '''

    def __init__(self, value: Token):
        '''
        Constructor.

        Args:
            value (str): The value of the node.
        '''
        self.value = value
        self.children: list[Node] = []

    def add_child(self, child):
        '''
        Add a child node to the node.

        Args:
            child (Node): The child node to add.
        '''
        self.children.append(child)

    def print_tree(self, depth=0):
        '''
        Print the tree.

        Args:
            depth (int, optional): The depth of the node. Defaults to 0.
        '''
        print('\t' * depth + str(self))
        for child in self.children:
            child.print_tree(depth + 1)

    def __str__(self):
        '''
        String representation of the node.

        Returns:
            str: The string representation of the node.
        '''
        return f'({self.value})'

    def __repr__(self):
        '''
        String representation of the node.

        Returns:
            str: The string representation of the node.
        '''
        return self.__str__()
