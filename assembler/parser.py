'''
    A parser definition
'''

from shutil import ExecError
from assembler.node import Node
from assembler.token import Token, TokenType, DATA_TYPES
from assembler.ast import Ast

DECODER = {
    'NOP': 0b0000_0000,
    'STA': 0b0000_0001,
    'LDA': 0b0000_0010,
    'ADD': 0b0000_0011,
    'OR': 0b0000_0100,
    'AND': 0b0000_0101,
    'NOT': 0b0000_0110,
    'SUB': 0b0000_0111,
    'JMP': 0b0000_1000,
    'JN': 0b0000_1001,
    'JZ': 0b0000_1010,
    'JNZ': 0b0000_1011,
    'LDI': 0b0000_1110,
    'HLT': 0b0000_1111,
}


def parser(tokens: list[Token]) -> tuple[Ast, dict[str, str]]:
    '''
    Parses the tokens and returns the AST.
    '''
    ast = Ast()

    # Create the root node.
    root = Node('ROOT')
    ast.root = root

    # Create the current node.
    current = root

    # Create the symbol table.
    labels = [(token.value, None)
              for token in tokens if token.type == TokenType.LABEL]
    simbol_table = dict(labels)

    for token in tokens:
        if token.type == TokenType.SEGMENT:
            # Create a new node childred the root node.
            current = Node(token)
            root.children.append(current)
        elif token.type == TokenType.LABEL:
            if current.value.type != TokenType.SEGMENT:
                raise ExecError('Labels can only be defined in a segment.')

            # Create a new node childred the current node.
            label_node = Node(token)
            current.add_child(label_node)

        elif token.type in DATA_TYPES:
            if current.value.type != TokenType.SEGMENT or current.value.value != 'DATA':
                raise ExecError(
                    'Data can only be defined in the DATA segment.')
            # Create a new node childred the current node.
            data_node = Node(token)
            current.add_child(data_node)

        elif token.type == TokenType.UPCODE:
            if current.value.type != TokenType.SEGMENT or current.value.value != 'TEXT':
                raise ExecError(
                    'Instructions can only be defined in the TEXT segment.')
            # Create a new node childred the current node.
            instruction_node = Node(token)
            current.add_child(instruction_node)

            # Decode the instruction.
            instruction_node.value.value = DECODER[token.value]

        elif token.type == TokenType.IMEDIATE:
            if current.value.type != TokenType.SEGMENT or current.value.value != 'TEXT':
                raise ExecError(
                    'Imediate values can only be defined after an instruction.')
            # Create a new node childred the current node.
            data_node = Node(token)
            current.add_child(data_node)

        elif token.type == TokenType.REFERENCE:
            if current.value.type != TokenType.SEGMENT or current.value.value != 'TEXT':
                raise ExecError(
                    'References can only be defined after an instruction.')
            # Create a new node childred the current node.
            data_node = Node(token)
            current.add_child(data_node)

    return ast, simbol_table
