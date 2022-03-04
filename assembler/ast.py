from assembler.node import Node


class Ast:
    '''
    Abstract Syntax Tree

    The AST is a tree of nodes. Each node has a name, a value, and a list of
    children.
    '''

    root: Node = None
    current: Node = None

    def __init__(self, root: Node | None = None):
        '''
        Constructor.
        '''

        self.root = root
        self.current = root

    def add_node(self, node: Node):
        '''
        Add a node to the tree.

        Args:
            node (Node): The node to add.
        '''
        if self.root is None:
            self.root = node
            self.current = self.root
        else:
            self.current.add_child(node)
            self.current = node

    def print_tree(self):
        '''
        Print the tree.
        '''
        self.root.print_tree()
