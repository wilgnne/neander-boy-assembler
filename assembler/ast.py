from assembler.node import Node


def link(simbol_table: dict[str, str], memory: list) -> list[int]:
    '''
    Link references.

    Args:
        simbol_table (dict[str, str]): The simbol table.
        memory (list): The memory.

    Returns:
        list: The memory.
    '''

    return list(map(simbol_table.get, memory, memory))


class Ast:
    '''
    Abstract Syntax Tree

    The AST is a tree of nodes. Each node has a name, a value, and a list of
    children.
    '''

    root: Node = None
    text: Node = None

    def __init__(self, root: Node = None):
        '''
        Constructor.
        '''

        self.root = root

    def sort(self):
        '''
        Make TEXT the first segment.
        '''
        self.root.children.sort(
            key=lambda x: 0 if x.value.value == 'TEXT' else 1)

    def compile(self, simbol_table: dict[str, str], debug: bool = False) -> list[int]:
        '''
        Compile the tree.

        Args:
            debug (bool): If True, print the compiled code.
        '''
        self.sort()

        text, data = self.root.children

        memory = text.compile(simbol_table)
        memory = data.compile(simbol_table, memory)
        memory = link(simbol_table, memory)

        if debug:
            print('SIMBOL TABLE:', simbol_table, '\n')
            print(memory)

        return memory

    def print_tree(self):
        '''
        Print the tree.
        '''
        self.root.print_tree()
