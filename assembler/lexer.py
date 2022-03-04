'''
    A lexer definition
'''

from assembler.token import Token
from assembler.node import Node
from assembler.ast import Ast


def lexer(entry: str) -> Ast:
    '''
    Lexical analysis.
    '''

    lines = entry.split('\n')

    ast = Ast(Node(Token('root', 'root')))

    state = None

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.isspace() or line in ['\n', '']:  # Skip empty lines.
            i += 1
        if state is None:
            if line.startswith('.text'):
                state = 'text'
            elif line.startswith('.data'):
                state = 'data'

        elif state == 'data':
            data_node = None
            if line.startswith('.data'):
                data_token = Token('DATA', line)
                data_node = Node(data_token)
                ast.root.add_child(data_node)
                i += 1
            while i < len(lines) and not lines[i].startswith('.text'):
                line = lines[i]

                if line.isspace() or line in ['\n', '']:  # Skip empty lines.
                    i += 1
                    continue

                label = line.split(':')[0]
                label_node = Node(Token('LABEL', label))

                tmp = line.split(':')[1].strip().split(' ')

                type_name  = tmp[0]

                value = tmp[1]
                if type_name == '.word':
                    value = int(value)

                value_token = Node(Token(type_name, value))

                label_node.add_child(value_token)
                data_node.add_child(label_node)

                i += 1
            state = None

        elif state == 'text':
            text_node = None
            if line.startswith('.text'):
                text_token = Token('TEXT', line)
                text_node = Node(text_token)
                ast.root.add_child(text_node)
                i += 1

            while i < len(lines) and not lines[i].startswith('.data'):
                line = lines[i]

                if line.isspace() or line in ['\n', '']:  # Skip empty lines.
                    i += 1
                    continue

                if line.count(':') == 1:
                    label_node = Node(Token('LABEL', line.split(':')[0]))
                    text_node.add_child(label_node)
                    i += 1
                    continue

                tmp = line.split(' ')
                upcode, operands = tmp[0], tmp[1:]

                upcode_node = Node(Token('UPCODE', upcode))

                for operand in operands:
                    value_token = None
                    if operand.startswith('0x'):
                        value_token = Node(Token('IMEDIATE', int(operand, 16)))
                    elif operand.startswith('0b'):
                        value_token = Node(Token('IMEDIATE', int(operand, 2)))
                    else:
                        value_token = Node(Token('LABEL', operand))
                    upcode_node.add_child(value_token)

                text_node.add_child(upcode_node)

                i += 1
            state = None

    return ast
