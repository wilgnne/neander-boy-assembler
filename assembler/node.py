'''
    A Node class definition
'''

from assembler.token import Token, TokenType, INITIALIZABLE_DATA_TYPES


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

    def compile(self, simbol_table: dict[str, str], memory: list | None = None) -> list:
        '''
        Compile the node.

        Args:
            simbol_table (dict[str, str]): The simbol table.
            memory (list | None): The memory.

        Returns:
            list: The memory.
        '''

        if memory is None:
            memory = []

        if self.value.value == 'TEXT':
            return self.compile_text(simbol_table, memory)
        elif self.value.value == 'DATA':
            return self.compile_data(simbol_table, memory)
        else:
            raise ValueError('Unknown segment.')

    def compile_text(self, simbol_table:  dict[str, str], memory: list) -> list:
        '''
        Compile the TEXT segment.

        Args:
            simbol_table (dict[str, str]): The simbol table.
            memory (list | None): The memory.

        Returns:
            list: The memory.
        '''

        for child in self.children:
            if child.value.type == TokenType.LABEL:
                simbol_table[child.value.value] = len(memory)
            elif child.value.type == TokenType.UPCODE:
                memory.append(child.value.value)
            elif child.value.type == TokenType.IMEDIATE:
                memory.append(child.value.value)
            elif child.value.type == TokenType.REFERENCE:
                memory.append(child.value.value)
            else:
                raise ValueError('Unknown token type.')

        return memory

    def compile_data(self, simbol_table: dict[str, str], memory: list) -> list:
        '''
        Compile the DATA segment.

        Args:
            simbol_table (dict[str, str]): The simbol table.
            memory (list | None): The memory.

        Returns:
            list: The memory.
        '''

        for index, child in enumerate(self.children):
            if child.value.type == TokenType.LABEL:
                simbol_table[child.value.value] = len(memory)
            elif child.value.type in INITIALIZABLE_DATA_TYPES:
                memory.append(child.value.value)
            elif child.value.type == TokenType.ADDR:
                prev = self.children[index - 1]

                if prev.value.type == TokenType.LABEL:
                    simbol_table[prev.value.value] = child.value.value
                else:
                    raise ValueError('Invalid address.')
            else:
                raise ValueError('Unknown token type.')

        return memory

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
