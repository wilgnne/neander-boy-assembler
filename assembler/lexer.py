'''
    A lexer definition
'''

from assembler.token import Token, TokenType


def is_label(line: str) -> bool:
    '''
    Check if a line is a label.
    '''

    return line.count(':') > 0


def is_segment(line: str) -> bool:
    '''
    Check if a line is a segment.
    '''

    return line.startswith('.DATA') or line.startswith('.TEXT')


def is_type(line: str) -> bool:
    '''
    Check if a line is a type.
    '''

    return line.count('.') > 0


def is_comment(line: str) -> bool:
    '''
    Check if a line is a comment.
    '''

    return line.count(';') > 0


def is_empty(line: str) -> bool:
    '''
    Check if a line is empty.
    '''

    return line.strip() == ''


def lexer(entry: str) -> list[Token]:
    '''
    Lexical analysis.
    '''

    lines = [line.strip() for line in entry.split('\n')]
    tokens = []

    for line in lines:
        if is_empty(line) or is_comment(line):
            continue
        elif is_segment(line):
            tokens.append(Token(TokenType.SEGMENT, line.split('.')[1]))
        elif is_label(line):
            label = line.split(':')[0].strip()
            tokens.append(Token(TokenType.LABEL, label))

            if is_type(line):
                tmp = line.split('.')[1].strip().split(' ')
                type_name = tmp[0]
                value = tmp[1]

                if value.startswith('0X'):
                    value = int(value, 16)
                elif value.startswith('0B'):
                    value = int(value, 2)
                else:
                    value = int(value)

                tokens.append(Token(TokenType[type_name], value))
        elif is_type(line):
            tmp = line.split('.')[1].strip().split(' ')

            type_name = tmp[0]
            value = tmp[1]

            if value.startswith('0X'):
                value = int(value, 16)
            elif value.startswith('0B'):
                value = int(value, 2)
            else:
                value = int(value)

            tokens.append(Token(TokenType[type_name], value))

        else:
            tmp = line.split(' ')
            upcode, operands = tmp[0], tmp[1:]

            upcode_token = Token(TokenType.UPCODE, upcode)
            tokens.append(upcode_token)

            for operand in operands:
                value_token = None
                if operand.startswith('0X'):
                    value_token = Token(TokenType.IMEDIATE, int(operand, 16))
                elif operand.startswith('0B'):
                    value_token = Token(TokenType.IMEDIATE, int(operand, 2))
                else:
                    value_token = Token(TokenType.REFERENCE, operand)
                tokens.append(value_token)

    return tokens
